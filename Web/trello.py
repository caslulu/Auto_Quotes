import requests
import os
from dotenv import load_dotenv


#TRELLO API INFOS
URL_TRELLO = os.getenv("URL_TRELLO")
yourKey = os.getenv("TRELLO_KEY")
yourToken = os.getenv("TRELLO_TOKEN")
idList = os.getenv("TRELLO_ID_LIST")

load_dotenv()


class Trello():
    def criar_carta(self, nome, estado_documento, veiculos, documento, endereco, vin, financiado, tempo_de_seguro, nascimento, tempo_no_endereco, tempo_com_veiculo):   

        descricao_carta = (f'doc: {documento} - {estado_documento} \n {endereco} \n vin: {vin} \n\
           {financiado} \n {nascimento} \n tempo de seguro: {tempo_de_seguro} \n veiculo: {veiculos} \n tempo no endereco: {tempo_no_endereco} \n\
            tempo com o veiculo: {tempo_com_veiculo}')

        params_create = {"key": yourKey,
        "token": yourToken,
        "idList": "662d7f3ed2bd7931022f2ed6",
        "name": nome,
        "desc": descricao_carta}
        requests.post(f"{URL_TRELLO}", params=params_create)
