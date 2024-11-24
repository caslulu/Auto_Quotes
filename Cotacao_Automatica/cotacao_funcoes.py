import os

from playwright.sync_api import Playwright, sync_playwright, expect


from Cotacao_automatica.data import DataManager
from Cotacao_automatica.cotacao import Cotacao


EMAIL = os.getenv("EMAIL")
data = DataManager()
cotacao = Cotacao()

def card_only():
    data.pegar_excel()
    data.criar_card_trello()
    

def fazer_cotacao_only(opcao):
    data.pegar_excel()
    with sync_playwright() as playwright:
        cotacao.automatico( playwright,  zipcode=data.zipcode, first_name=data.first_name, 
            last_name=data.last_name,  date_birth=data.nascimento,  address=data.endereco, 
            vin=data.lista_vin[0],  email=EMAIL,  financiado=data.financiado, opcao=opcao, quantidade_veiculos=data.lista_vin )
            

def card_and_cotacao(opcao):
    card_only()
    fazer_cotacao_only(opcao=opcao)


