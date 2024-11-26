import requests
from datetime import datetime

def decodificar_vin(vin):

    """pegar o(s) vins e escrever o nome do veiculo"""

    veiculos = ""
    lista_vin = vin.split(" / ")
    for veiculo in lista_vin:
        get_info = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{veiculo}?format=json').json()['Results']
        carro=f"{get_info[7]["Value"]}, {get_info[9]["Value"]}, {get_info[10]["Value"]} / "
        veiculos = carro + veiculos
    return (veiculos, lista_vin)


def formatar_data(data):
    """formatar a data no formato (mm/dd/yyyy)"""
    nascimento = datetime.strptime(data, "%m/%d/%Y").strftime("%m/%d/%Y")
    return nascimento

def separar_nome(nome):
    """separar o nome em first e last name"""

    parts = nome.split(" ")
    first_name = parts[0]
    last_name = parts[-1]
    return (first_name, last_name)

def separar_documento(documento_completo):
    """separar documento em numero do documento e estado do documento"""
    documento, estado = documento_completo.split(" - ")
    return(documento, estado)

