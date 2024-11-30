import requests
import os
from dotenv import load_dotenv

from Data.data_funcoes import *
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
    def __init__(self) -> None:
        pass


    def pegar_excel(self):


        """a funcao pegar_excel, vai pegar a primeira row do excel e salvar nas variaveis abaixo!"""


        response = requests.get(url=f"{URL_EXCEL}", headers=header)
        print(response.status_code)
        response = response.json()["formResponses1"][0]


        self.genero = response["genero"]
        self.nome = response["nomeCompleto"]
        self.documento, self.estado_documento = separar_documento(response["documentoDeHabilitação (cnhDoBrasil,DriverLicenseOuPassaporte)"])
        self.endereco = response["endereçoResidencialCompleto (comZipCode)"]
        self.zipcode = self.endereco.split(" ")[-1]
        self.financiado = response["oVeículo éQuitadoOuFinanciado?"]
        self.tempo_de_seguro = response["tempoDeSeguro"]
        self.first_name, self.last_name = separar_nome(self.nome)
        self.vin = response["vinDoVeículo"]
        self.veiculos, self.lista_vin = decodificar_vin(vin=self.vin)
        self.nascimento = formatar_data(data=response["dataDeNascimento"])
            
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

        
        descricao_carta = f'doc: {self.documento} - {self.estado_documento} \n {self.endereco} \n vin: {self.vin} \n\
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
