import requests
import os
from dotenv import load_dotenv

class Trello:

    def criar_carta_e_anexar_imagem(self, cotacao_form, imagens_files):
        """
        Cria a carta no Trello (se solicitado) e anexa múltiplas imagens/documentos, se fornecido.
        Retorna (trello_card_id, status_msg, status_type)
        """
        trello_card_id = None
        status_msgs = []
        status_type = None
        # Só processa se a caixinha "colocar_trello" estiver marcada
        colocar_trello = cotacao_form.colocar_trello.data if hasattr(cotacao_form, 'colocar_trello') else False
        if not colocar_trello:
            return None, None, None
        # Cria carta no Trello
        trello_card_id = self.criar_carta(
            nome=cotacao_form.nome.data,
            documento=cotacao_form.documento.data,
            endereco=cotacao_form.endereco.data,
            data_nascimento=cotacao_form.data_nascimento.data,
            tempo_de_seguro=cotacao_form.tempo_de_seguro.data,
            tempo_no_endereco=cotacao_form.tempo_no_endereco.data,
            veiculos=[v.data for v in cotacao_form.veiculos],
            nome_conjuge=getattr(cotacao_form, 'nome_conjuge', None) and cotacao_form.nome_conjuge.data or None,
            data_nascimento_conjuge=getattr(cotacao_form, 'data_nascimento_conjuge', None) and cotacao_form.data_nascimento_conjuge.data or None,
            documento_conjuge=getattr(cotacao_form, 'documento_conjuge', None) and cotacao_form.documento_conjuge.data or None
        )
        if not trello_card_id:
            return None, 'Falha ao criar card no Trello.', 'danger'
        if imagens_files:
            import os, tempfile
            for imagem_file in imagens_files:
                if not imagem_file or not getattr(imagem_file, 'filename', None):
                    continue
                ext = os.path.splitext(imagem_file.filename)[1].lower()
                with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
                    temp_path = tmp.name
                    imagem_file.save(temp_path)
                try:
                    resp = self.anexar_imagem_trello(trello_card_id, temp_path)
                    status_code = resp.get('status_code', None) if isinstance(resp, dict) else getattr(resp, 'status_code', None)
                    if status_code == 200:
                        status_msgs.append(f'Arquivo "{imagem_file.filename}" anexado com sucesso!')
                        status_type = 'success'
                    else:
                        status_msgs.append(f'Falha ao anexar "{imagem_file.filename}".')
                        status_type = 'danger'
                except Exception as e:
                    status_msgs.append(f'Erro ao anexar "{imagem_file.filename}": {e}')
                    status_type = 'danger'
                finally:
                    try:
                        os.remove(temp_path)
                    except Exception:
                        pass
        status_msg = "\n".join(status_msgs) if status_msgs else None
        return trello_card_id, status_msg, status_type
    def __init__(self):
        load_dotenv()
        self.URL_TRELLO = os.getenv("URL_TRELLO")
        self.yourKey = os.getenv("TRELLO_KEY")
        self.yourToken = os.getenv("TRELLO_TOKEN")
        self.idList = os.getenv("TRELLO_ID_LIST") or "662d7f3ed2bd7931022f2ed6"


    def criar_carta(self, **kwargs):
        """
        Cria uma carta no Trello. Se houver dados de cônjuge, inclui na descrição.
        """
        veiculos = kwargs.get('veiculos', '')
        email = kwargs.get('email', '')
        nome_conjuge = kwargs.get('nome_conjuge')
        data_nascimento_conjuge = kwargs.get('data_nascimento_conjuge')
        documento_conjuge = kwargs.get('documento_conjuge')
        from app.util.data_funcoes import veiculo_vin
        veiculos_lista = []
        import json
        if isinstance(veiculos, str):
            try:
                veiculos_lista = json.loads(veiculos)
            except Exception:
                pass
        elif isinstance(veiculos, list):
            veiculos_lista = veiculos
        # Monta descrição dos veículos, cada info em uma linha
        veiculos_desc = ''
        if veiculos_lista:
            for idx, v in enumerate(veiculos_lista, 1):
                vin = v.get('vin', '-')
                financiado = v.get('financiado', '-')
                tempo = v.get('tempo_com_veiculo', '-')
                marca_modelo_ano = '-'
                if vin and vin != '-':
                    try:
                        marca_modelo_ano = veiculo_vin(vin)
                    except Exception:
                        marca_modelo_ano = '-'
                veiculos_desc += (
                    f"\nVeículo {idx}:"
                    f"\n  VIN: {vin}"
                    f"\n  {marca_modelo_ano}"
                    f"\n  Estado: {financiado}"
                    f"\n  Tempo: {tempo}\n"
                )
        else:
            veiculos_desc = str(veiculos)
        descricao = (
            f"doc: {kwargs.get('documento', '')}\n"
            f"{kwargs.get('endereco', '')}\n"
            f"{kwargs.get('data_nascimento', '')}\n"
            f"tempo de seguro: {kwargs.get('tempo_de_seguro', '')}\n"
            f"tempo no endereco: {kwargs.get('tempo_no_endereco', '')}\n"
            f"email: {email}\n"
            f"{veiculos_desc}\n"
        )
        if nome_conjuge:
            desc_conjuge = (
                f"NOME CÔNJUGE: {nome_conjuge}\n"
                f"DATA NASCIMENTO CÔNJUGE: {data_nascimento_conjuge}\n"
                f"DRIVER CÔNJUGE: {documento_conjuge}\n"
            )
            descricao = descricao + "\n----\n" + desc_conjuge
        params_create = {
            "key": self.yourKey,
            "token": self.yourToken,
            "idList": self.idList,
            "name": kwargs.get('nome', ''),
            "desc": descricao
        }
        response = requests.post(f"{self.URL_TRELLO}", params=params_create)
        if response.ok:
            return response.json().get("id")
        return None

    def anexar_imagem_trello(self, card_id, image_path):
        print("Tentando anexar imagem:", image_path)
        print("Card ID:", card_id)
        print("Arquivo existe?", os.path.exists(image_path))
        url = f"https://api.trello.com/1/cards/{card_id}/attachments"
        query = {
            'key': self.yourKey,
            'token': self.yourToken
        }
        with open(image_path, 'rb') as image_file:
            files = {
                'file': image_file
            }
            response = requests.post(url, params=query, files=files)
        print("Resposta Trello:", response.status_code, response.text)
        return response.json()
