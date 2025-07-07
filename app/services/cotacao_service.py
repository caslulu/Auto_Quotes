from app.util.data_funcoes import formatar_data, separar_nome, separar_documento, separar_endereco, formatar_com_virgula
from app.extensions import db
from app.models.cotacao_db import Cotacao
from app.services.trello_service import Trello
import json

class CotacaoService:
    def __init__(self, taxa=320.00):
        self.TAXA = taxa

    def extrair_dados_formulario(self, cotacao_form):
        veiculos = [
            {
                'vin': v.vin.data,
                'tempo_com_veiculo': v.tempo_com_veiculo.data,
                'financiado': v.financiado.data,
                'placa': v.placa.data
            }
            for v in cotacao_form.veiculos.entries
        ]
        pessoas = [
            {
                'nome': p.nome.data,
                'documento': p.documento.data,
                'data_nascimento': p.data_nascimento.data,
                'parentesco': p.parentesco.data,
                'genero': p.genero.data
            }
            for p in getattr(cotacao_form, 'pessoas', []).entries
        ]
        return {
            "genero": cotacao_form.genero.data,
            "nome": cotacao_form.nome.data,
            "documento": cotacao_form.documento.data,
            "endereco": cotacao_form.endereco.data,
            "tempo_de_seguro": cotacao_form.tempo_de_seguro.data,
            "data_nascimento": cotacao_form.data_nascimento.data,
            "tempo_no_endereco": cotacao_form.tempo_no_endereco.data,
            "estado_civil": cotacao_form.estado_civil.data,
            "nome_conjuge": cotacao_form.nome_conjuge.data,
            "data_nascimento_conjuge": cotacao_form.data_nascimento_conjuge.data,
            "documento_conjuge": cotacao_form.documento_conjuge.data,
            "veiculos": veiculos,
            "pessoas": pessoas
        }

    def criar_cotacao(self, form):
        """
        Cria uma nova cotação a partir dos dados do formulário e salva no banco de dados.
        """
        dados = self.extrair_dados_formulario(form)
        cotacao = Cotacao(
            genero=dados['genero'],
            nome=dados['nome'],
            documento=dados['documento'],
            endereco=dados['endereco'],
            tempo_de_seguro=dados['tempo_de_seguro'],
            data_nascimento=dados['data_nascimento'],
            tempo_no_endereco=dados['tempo_no_endereco'],
            estado_civil=dados['estado_civil'],
            nome_conjuge=dados['nome_conjuge'],
            data_nascimento_conjuge=dados['data_nascimento_conjuge'],
            documento_conjuge=dados['documento_conjuge'],
            vehicles_json=json.dumps(dados['veiculos']),
            pessoas_json=json.dumps(dados.get('pessoas', [])),
            trello_card_id=None
        )
        db.session.add(cotacao)
        db.session.commit()
        return cotacao

    def gerar_email(self, nome_completo):
        """Gera um email a partir do nome completo, removendo espaços e convertendo para minúsculas."""
        return f"{nome_completo.lower().replace(' ', '')}@outlook.com"

    def processar_cotacao(self, primeiro):
        veiculos, pessoas = [], []
        if hasattr(primeiro, 'vehicles_json') and primeiro.vehicles_json:
            try:
                data = json.loads(primeiro.vehicles_json)
                if isinstance(data, dict):
                    veiculos = data.get('veiculos', [])
                    pessoas = data.get('pessoas', [])
                    if not isinstance(veiculos, list):
                        veiculos = []
                    if not isinstance(pessoas, list):
                        pessoas = []
                elif isinstance(data, list):
                    veiculos = data
            except Exception:
                veiculos = []
                pessoas = []
        genero = primeiro.genero
        first_name, last_name = separar_nome(primeiro.nome)
        documento, estado_documento = separar_documento(primeiro.documento)
        rua, apt, cidade, zipcode = separar_endereco(primeiro.endereco)
        tempo_de_seguro = primeiro.tempo_de_seguro
        data_nascimento = formatar_data(primeiro.data_nascimento)
        tempo_no_endereco = primeiro.tempo_no_endereco
        email = self.gerar_email(primeiro.nome)
        return {
            "genero": genero,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "estado_documento": estado_documento,
            "rua": rua,
            "apt": apt,
            "cidade": cidade,
            "zipcode": zipcode,
            "tempo_de_seguro": tempo_de_seguro,
            "data_nascimento": data_nascimento,
            "tempo_no_endereco": tempo_no_endereco,
            "estado_civil": getattr(primeiro, 'estado_civil', None),
            "nome_conjuge": getattr(primeiro, 'nome_conjuge', None),
            "data_nascimento_conjuge": getattr(primeiro, 'data_nascimento_conjuge', None),
            "documento_conjuge": getattr(primeiro, 'documento_conjuge', None),
            "veiculos": veiculos
        }

    def processar_preco_quitado(self, preco_form, taxa=None):
        taxa = float(taxa) if taxa is not None else self.TAXA
        entrada_basico = float(preco_form.entrada_basico.data.replace(",", "")) + taxa
        mensal_basico = preco_form.mensal_basico.data
        valor_total_basico = float(preco_form.valor_total_basico.data.replace(",", "")) + taxa
        entrada_completo = float(preco_form.entrada_completo.data.replace(",", "")) + taxa
        mensal_completo = preco_form.mensal_completo.data
        valor_total_completo = float(preco_form.valor_total_completo.data.replace(",", "")) + taxa
        nome = preco_form.nome.data

        return {
            "entrada_basico": formatar_com_virgula(entrada_basico),
            "mensal_basico": mensal_basico,
            "valor_total_basico": formatar_com_virgula(valor_total_basico),
            "entrada_completo": formatar_com_virgula(entrada_completo),
            "mensal_completo": mensal_completo,
            "valor_total_completo": formatar_com_virgula(valor_total_completo),
            "nome": nome
        }

    def processar_preco_financiado(self, preco_form, taxa=None):
        taxa = float(taxa) if taxa is not None else self.TAXA
        entrada_completo = float(preco_form.entrada_completo.data.replace(",", "")) + taxa
        mensal_completo = preco_form.mensal_completo.data
        valor_total_completo = float(preco_form.valor_total_completo.data.replace(",", "")) + taxa
        nome = preco_form.nome.data
        return {
            "entrada_completo": formatar_com_virgula(entrada_completo),
            "mensal_completo": mensal_completo,
            "valor_total_completo": formatar_com_virgula(valor_total_completo),
            "nome": nome
        }
    def duplicar_cotacao(self, cotacao):
        nova_cotacao = Cotacao(
            genero=cotacao.genero,
            nome=cotacao.nome,
            documento=cotacao.documento,
            endereco=cotacao.endereco,
            tempo_de_seguro=cotacao.tempo_de_seguro,
            data_nascimento=cotacao.data_nascimento,
            tempo_no_endereco=cotacao.tempo_no_endereco,
            estado_civil=cotacao.estado_civil,
            nome_conjuge=cotacao.nome_conjuge,
            data_nascimento_conjuge=cotacao.data_nascimento_conjuge,
            documento_conjuge=cotacao.documento_conjuge,
            vehicles_json=cotacao.vehicles_json,
            pessoas_json=cotacao.pessoas_json,
            trello_card_id=None
        )
        return nova_cotacao