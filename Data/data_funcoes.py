import requests
from datetime import datetime

def decodificar_vin(vin):

    """pegar o(s) vins e escrever o nome do veiculo
        return Marca, Modelo, Ano / ..."""
    try:
        veiculos = ""
        lista_vin = vin.split(" / ")
        for veiculo in lista_vin:
            get_info = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{veiculo}?format=json').json()['Results']
            marca = get_info[7]["Value"]
            modelo = get_info[9]["Value"]
            ano = get_info[10]["Value"]

            if not marca or not modelo or not ano:
                raise ValueError
            
            else:
                carro=f"{marca}, {modelo}, {ano} / "
                veiculos = carro + veiculos
        return (veiculos.rstrip(" / "), lista_vin)
    except Exception as e:
        raise ValueError(f"Verifique se o vin number esta correto: {e}")

def formatar_data(data):

    nascimento = datetime.strptime(data, "%m/%d/%Y").strftime("%m/%d/%Y")
    return nascimento

def separar_nome(nome):
    try:
        partes = nome.split(" ")
        if len(partes) < 2:
            raise ValueError
        first_name = partes[0]
        last_name = partes[-1]
        return (first_name, last_name)
    
    except Exception as e:
        raise ValueError(f"Voce deve colocar o primeiro e o ultimo nome: {e}")

def separar_documento(documento_completo):

    try:
        documento, estado = documento_completo.split(" - ")
        return(documento, estado)
    except Exception as e:
        raise Exception(f"Verifique se o input esta na formatacao 'documento - estado': {e}")

def separar_endereco(endereco_completo):

    try:
        if len(endereco_completo.split(", ")) == 3:
            rua, cidade, zipcode = endereco_completo.split(", ")
            return (rua, None, cidade, zipcode)
        else:
            rua, apt, cidade, zipcode = endereco_completo.split(", ")
            return (rua, apt, cidade, zipcode)
    except Exception as e:
        raise ValueError(f"Verifique se o input esta na formatacao 'Rua, apt, cidade, zipcode': {e}") ## apt = argumento opcional

