import requests
import os
from dotenv import load_dotenv

from Data.data import *

#TRELLO API INFOS
URL_TRELLO = os.getenv("URL_TRELLO")
yourKey = os.getenv("TRELLO_KEY")
yourToken = os.getenv("TRELLO_TOKEN")
idList = os.getenv("TRELLO_ID_LIST")

load_dotenv()


class Trello(DataManager):
    def __init__(self):
        super().__init__()
        self.informacoes_para_cotacao()

    def criar_descricao(self):
        return (f'doc: {self.documento} - {self.estado_documento} \n {self.endereco} \n vin: {self.vin} \n\
           {self.financiado} \n {self.nascimento} \n tempo de seguro: {self.tempo_de_seguro} \n veiculo: {self.veiculos} \n tempo no endereco: {self.tempo_no_endereco} \n\
            tempo com o veiculo: {self.tempo_com_veiculo}')
    
    def criar_carta(self):   

        descricao_carta = self.criar_descricao()

        params_create = {"key": yourKey,
        "token": yourToken,
        "idList": "662d7f3ed2bd7931022f2ed6",
        "name": self.nome,
        "desc": descricao_carta}
        requests.post(f"{URL_TRELLO}", params=params_create)
