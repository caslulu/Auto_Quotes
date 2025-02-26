import requests
import os
from dotenv import load_dotenv

from Data.data_funcoes import *
load_dotenv()


#EXCEL API INFOS
header = {os.getenv("HEADER_KEY"): os.getenv("HEADER_VALUE")}
URL_EXCEL = os.getenv("URL_EXCEL")


class DataManager:
    def __init__(self) -> None:
        try:
            self.response = requests.get(url=f"{URL_EXCEL}", headers=header)
            self.response = self.response.json()["formResponses1"]
            print(self.response)
        except Exception as e:
            raise IndexError(f"Nao possui nenhuma cotacao para ser feita no excel: {e}")
            

    def informacoes_para_cotacao(self):

        
        self.genero = self.response["genero"] 
        self.nome = self.response["nomeCompleto"]
        self.documento, self.estado_documento = separar_documento(self.response["documentoDeHabilitação (cnhDoBrasil,DriverLicenseOuPassaporte)"])
        self.rua, self.apt, self.cidade, self.zipcode = separar_endereco(self.response["endereçoResidencialCompleto (comZipCode)"])
        self.financiado = self.response["oVeículo éQuitadoOuFinanciado?"]
        self.tempo_de_seguro = self.response["tempoDeSeguro"]
        self.first_name, self.last_name = separar_nome(self.nome)
        self.vin = self.response["vinDoVeículo"]
        self.veiculos, self.lista_vin= decodificar_vin(vin=self.vin)
        self.nascimento = formatar_data(data=self.response["dataDeNascimento"])
        self.endereco = f"{self.rua}, {self.apt}, {self.cidade}, {self.zipcode}"
        self.tempo_com_veiculo = self.response["tempoComOVeiculo"]
        self.tempo_no_endereco = self.response["tempoNoEndereco"]
        self.email = os.getenv("EMAIL")
    

    def delete_excel(self):
        requests.delete(url=f"{URL_EXCEL}/2", headers=header)
