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
    def criar_carta(self, **kwargs):

        descricao_carta = (
            f"doc: {kwargs['documento']}\n"
            f"{kwargs['endereco']} \n vin: {kwargs['vin']} \n"
            f"{kwargs['financiado']} \n {kwargs['data_nascimento']} \n"
            f"tempo de seguro: {kwargs['tempo_de_seguro']} \n veiculo: {kwargs['veiculos']} \n"
            f"tempo no endereco: {kwargs['tempo_no_endereco']} \n"
            f"tempo com o veiculo: {kwargs['tempo_com_veiculo']} \n"
            f"email: {kwargs['email']} \n"
        )

        params_create = {"key": yourKey,
        "token": yourToken,
        "idList": "662d7f3ed2bd7931022f2ed6",
        "name": kwargs['nome'],
        "desc": descricao_carta}
        response = requests.post(f"{URL_TRELLO}", params=params_create)
        if response.ok:
            return response.json().get("id")
        return None
    
    def anexar_imagem_trello(self, card_id, image_path):
        print("Tentando anexar imagem:", image_path)
        print("Card ID:", card_id)
        print("Arquivo existe?", os.path.exists(image_path))
        url = f"https://api.trello.com/1/cards/{card_id}/attachments"
        query = {
            'key': yourKey,
            'token': yourToken
        }
        with open(image_path, 'rb') as image_file:
            files = {
                'file': image_file
            }
            response = requests.post(url, params=query, files=files)
        print("Resposta Trello:", response.status_code, response.text)
        return response.json()
