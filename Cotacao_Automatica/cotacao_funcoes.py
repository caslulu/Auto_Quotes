from playwright.sync_api import sync_playwright

from Data.data import DataManager
from Cotacao_automatica.Sites.progressive import Progressive
from Cotacao_automatica.Sites.geico import Geico


data = DataManager()


data.pegar_excel()

# vai apenas criar o card no trello
def card_only():
    data.criar_card_trello()
    
# vai apenas fazer a cotacao
def fazer_cotacao_only(opcao):
    with sync_playwright() as playwright:

        if opcao == "progressive":
            progressive = Progressive()
            progressive.cotacao(playwright=playwright, data_dict=data.dict)

        elif opcao == "geico":
            geico = Geico()
            geico.cotacao(playwright=playwright, data_dict=data.dict)
            

            
# vai fazer a cotacao e criar o card no trello
def card_and_cotacao(opcao):
    card_only()
    fazer_cotacao_only(opcao=opcao)


