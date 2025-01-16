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


class Trello():
    def __init__(self):
        self.data = DataManager()
        self.data.informacoes_para_cotacao()

    def criar_card(self):   
        
        descricao_carta = f'doc: {self.data.documento} - {self.data.estado_documento} \n {self.data.endereco} \n vin: {self.data.vin} \n\
           {self.data.financiado} \n {self.data.nascimento} \n tempo de seguro: {self.data.tempo_de_seguro} \n\
            veiculo: {self.data.veiculos}'


        params_create = {"key": yourKey,
        "token": yourToken,
        "idList": idList,
        "name": self.data.nome,
        "desc": descricao_carta}
        requests.post(f"{URL_TRELLO}cards", params=params_create)
