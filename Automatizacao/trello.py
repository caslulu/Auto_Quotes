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

    def criar_card(self):   
        descricao_carta = f'doc: {self.documento} - {self.estado_documento} \n {self.endereco} \n vin: {self.vin} \n\
           {self.financiado} \n {self.nascimento} \n tempo de seguro: {self.tempo_de_seguro} \n\
            veiculo: {self.veiculos}'


        params_create = {"key": yourKey,
        "token": yourToken,
        "idList": idList,
        "name": self.nome,
        "desc": descricao_carta}
        requests.post(f"{URL_TRELLO}cards", params=params_create)
