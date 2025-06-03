import requests
import os
import json
from dotenv import load_dotenv
from app.util.data_funcoes import veiculo_vin


class Trello:
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
        pessoas = kwargs.get('pessoas', '')
        email = kwargs.get('email', '')
        nome_conjuge = kwargs.get('nome_conjuge')
        data_nascimento_conjuge = kwargs.get('data_nascimento_conjuge')
        documento_conjuge = kwargs.get('documento_conjuge')
        veiculos_lista = []
        pessoas_lista = []
        # Suporte para dict com veiculos e pessoas
        if isinstance(veiculos, str):
            try:
                vehicles_data = json.loads(veiculos)
                if isinstance(vehicles_data, dict):
                    veiculos_lista = vehicles_data.get('veiculos', [])
                    pessoas_lista = vehicles_data.get('pessoas', [])
                else:
                    veiculos_lista = vehicles_data
            except Exception:
                veiculos_lista = []
                pessoas_lista = []
        elif isinstance(veiculos, list):
            veiculos_lista = veiculos
        if isinstance(pessoas, str):
            try:
                pessoas_lista = json.loads(pessoas)
            except Exception:
                pass
        elif isinstance(pessoas, list):
            pessoas_lista = pessoas
        # Monta descrição dos veículos, cada info em uma linha
        veiculos_desc = ''
        if veiculos_lista:
            for idx, v in enumerate(veiculos_lista, 1):
                vin = v.get('vin', '-')
                financiado = v.get('financiado', '-')
                tempo = v.get('tempo_com_veiculo', '-')
                placa = v.get('placa', '-')
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
                    f"\n  Tempo: {tempo}"
                    f"\n  Placa: {placa}\n"
                )
        else:
            veiculos_desc = str(veiculos)
        # Monta descrição das pessoas, cada info em uma linha
        pessoas_desc = ''
        if pessoas_lista:
            for idx, p in enumerate(pessoas_lista, 1):
                pessoas_desc += (
                    f"\n-- {p.get('parentesco', '-')} --"
                    f"\n  Nome: {p.get('nome', '-') }"
                    f"\n  Gênero: {p.get('genero', '-') }"
                    f"\n  Documento: {p.get('documento', '-') }"
                    f"\n  Data de Nascimento: {p.get('data_nascimento', '-') }\n"
                )
        descricao = (
            f"doc: {kwargs.get('documento', '')}\n"
            f"{kwargs.get('endereco', '')}\n"
            f"{kwargs.get('data_nascimento', '')}\n"
            f"tempo de seguro: {kwargs.get('tempo_de_seguro', '')}\n"
            f"tempo no endereco: {kwargs.get('tempo_no_endereco', '')}\n"
            f"email: {email}\n"
            f"{veiculos_desc}\n"
            f"{pessoas_desc}\n"
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
        if response.ok:
            return response.json()
        return None
