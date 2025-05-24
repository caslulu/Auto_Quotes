import requests
import os
from dotenv import load_dotenv


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
        email = kwargs.get('email', '')
        nome_conjuge = kwargs.get('nome_conjuge')
        data_nascimento_conjuge = kwargs.get('data_nascimento_conjuge')
        documento_conjuge = kwargs.get('documento_conjuge')
        descricao = (
            f"doc: {kwargs['documento']}\n"
            f"{kwargs['endereco']} \n vin: {kwargs['vin']} \n"
            f"{kwargs['financiado']} \n {kwargs['data_nascimento']} \n"
            f"tempo de seguro: {kwargs['tempo_de_seguro']} \n veiculo: {veiculos} \n"
            f"tempo no endereco: {kwargs['tempo_no_endereco']} \n"
            f"tempo com o veiculo: {kwargs['tempo_com_veiculo']} \n"
            f"email: {email} \n"
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
            "name": kwargs['nome'],
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
