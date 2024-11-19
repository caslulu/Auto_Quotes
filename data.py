import requests
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv()
#EXCEL API INFOS
header = {os.getenv("HEADER_KEY"): os.getenv("HEADER_VALUE")}
URL_EXCEL = os.getenv("URL_EXCEL")


#TRELLO API INFOS
URL_TRELLO = os.getenv("URL_TRELLO")
yourKey = os.getenv("TRELLO_KEY")
yourToken = os.getenv("TRELLO_TOKEN")
idList = os.getenv("TRELLO_ID_LIST")




class DataManager:


    def pegar_excel(self):


        """a funcao pegar_excel, vai pegar a primeira row do excel e salvar nas variaveis abaixo!"""


        response = requests.get(url=f"{URL_EXCEL}", headers=header).json()["formResponses1"][0]
        
        

        self.nome = response["nomeCompleto"]
        self.documento = response["documentoDeHabilitação (cnhDoBrasil,DriverLicenseOuPassaporte)"]
        self.endereco = response["endereçoResidencialCompleto (comZipCode)"]
        self.financiado = response["oVeículo éQuitadoOuFinanciado?"]
        self.tempo_de_seguro = response["tempoDeSeguro"]
        self.first_name, self.last_name = self.nome.split(" ")


        mes,dia,ano = response["dataDeNascimento"].split("/")
        if len(mes) == 1:
            mes = f"0{mes}"
        if len(dia) == 1:
            dia = f"0{dia}"
        self.nascimento = f"{mes}/{dia}/{ano}"


        
        
        self.vin = response["vinDoVeículo"].split(" / ")
        self.veiculos = ""
        for veiculo in self.vin:
            get_info = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{veiculo}?format=json').json()['Results']
            carros=f"{get_info[7]["Value"]}, {get_info[9]["Value"]}, {get_info[10]["Value"]} / "
            self.veiculos = carros + self.veiculos



            
    def criar_card_trello(self, nome, documento, endereco, vin, financiado, nascimento, tempo_de_seguro, veiculo):
        

        """a funcao 'criar_card_trello' ira criar o card
          no trello com as informacoes adquiridas no excel."""

        
        descricao_carta = f'doc: {documento} \n {endereco} \n vin: {vin} \n {financiado} \n {nascimento} \n tempo de seguro: {tempo_de_seguro} \n veiculo: {veiculo}'


        params_create = {"key": yourKey,
        "token": yourToken,
        "idList": idList,
        "name": nome,
        "desc": descricao_carta}
        requests.post(f"{URL_TRELLO}cards", params=params_create)


    def delete_excel(self):
        """Apenas deleta a primeira row do excel 
        (utilizar quando a cotacao ja tiver sido feita)"""
        requests.delete(url=f"{URL_EXCEL}/2", headers=header)
