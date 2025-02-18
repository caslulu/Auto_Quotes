import requests
import os
from dotenv import load_dotenv

from Data.data_funcoes import *
load_dotenv()


#EXCEL API INFOS
header = {os.getenv("HEADER_KEY"): os.getenv("HEADER_VALUE")}
URL_EXCEL = os.getenv("URL_EXCEL")


class DataManager:
    # def __init__(self) -> None:
    #     try:
    #         self.response = requests.get(url=f"{URL_EXCEL}", headers=header)
    #         self.response = self.response.json()["formResponses1"]
    #         print(self.response)
    #     except Exception as e:
    #         raise IndexError(f"Nao possui nenhuma cotacao para ser feita no excel: {e}")
            

    def informacoes_para_cotacao(self):

        self.genero = input("Qual o Genero? ")
        self.nome = input("Qual o Nome? ")
        self.documento, self.estado_documento = separar_documento(input("Qual a Driver License? "))
        self.rua, self.apt, self.cidade, self.zipcode = separar_endereco(input("Qual o endereco? "))
        self.financiado = input("financiado ou quitado? ")
        self.tempo_de_seguro = input("Quanto tempo de seguro? ")
        self.first_name, self.last_name = separar_nome(self.nome)
        self.vin = input("Qual o vin?")
        self.veiculos, self.lista_vin= decodificar_vin(vin=self.vin)
        self.nascimento = formatar_data(input("Qual a data de nascimento? "))
        self.endereco = f"{self.rua}, {self.apt}, {self.cidade}, {self.zipcode}"
        self.tempo_com_veiculo = input("Quanto tempo com o veiculo? ")
        self.tempo_no_endereco = input("Quanto tempo no endereco? ")
        self.email = os.getenv("EMAIL")

    

    def delete_excel(self):
        requests.delete(url=f"{URL_EXCEL}/2", headers=header)
