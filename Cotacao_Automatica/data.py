import requests
import os
from dotenv import load_dotenv, dotenv_values 
from datetime import datetime
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
        self.zipcode = self.endereco.split(" ")[-1]
        self.financiado = response["oVeículo éQuitadoOuFinanciado?"]
        self.tempo_de_seguro = response["tempoDeSeguro"]
        self.first_name, self.last_name = self.nome.split(" ")
        self.vin = response["vinDoVeículo"]
        self.veiculos = ""
        self.decodificar_vin()
        data_nascimento = response["dataDeNascimento"]
        data_formatada = datetime.strptime(data_nascimento, "%m/%d/%Y")
        self.nascimento = data_formatada.strftime("%m/%d/%Y")


        
    def decodificar_vin(self):

        """essa funcao vai pegar o(s) vins e escrever o nome do veiculo, caso seja necessario utilizar"""
        self.lista_vin = self.vin.split(" / ")
        for veiculo in self.lista_vin:
            get_info = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{veiculo}?format=json').json()['Results']
            carros=f"{get_info[7]["Value"]}, {get_info[9]["Value"]}, {get_info[10]["Value"]} / "
            self.veiculos = carros + self.veiculos


            
    def criar_card_trello(self):

        """
        a funcao 'criar_card_trello' ira criar o card
          no trello com as informacoes adquiridas no excel.

        Args:
        nome (str): Nome completo do cliente.
        documento (str): Documento do cliente (CNH, passaporte, etc.).
        endereco (str): Endereço completo do cliente.
        vin (str): Código VIN do veículo.
        financiado (str): Status de financiamento do veículo.
        nascimento (str): Data de nascimento do cliente.
        tempo_de_seguro (str): Tempo de seguro atual.
        veiculo (str): Informacoes do veiculo.
        """

        
        descricao_carta = f'doc: {self.documento} \n {self.endereco} \n vin: {self.vin} \n\
           {self.financiado} \n {self.nascimento} \n tempo de seguro: {self.tempo_de_seguro} \n\
            veiculo: {self.veiculos}'


        params_create = {"key": yourKey,
        "token": yourToken,
        "idList": idList,
        "name": self.nome,
        "desc": descricao_carta}
        requests.post(f"{URL_TRELLO}cards", params=params_create)




    def delete_excel(self):
        """Apenas deleta a primeira row do excel 
        (utilizar quando a cotacao ja tiver sido feita)"""

        requests.delete(url=f"{URL_EXCEL}/2", headers=header)




