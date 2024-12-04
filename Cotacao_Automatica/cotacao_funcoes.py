from playwright.sync_api import sync_playwright

from Data.data import DataManager
from Cotacao_automatica.cotacao import Cotacao


data = DataManager()
cotacao = Cotacao()


# vai apenas criar o card no trello
def card_only():
    data.pegar_excel()
    data.criar_card_trello()
    
# vai apenas fazer a cotacao
def fazer_cotacao_only(opcao):
    with sync_playwright() as playwright:
        cotacao.automatico(playwright=playwright, opcao=opcao)
            
# vai fazer a cotacao e criar o card no trello
def card_and_cotacao(opcao):
    card_only()
    fazer_cotacao_only(opcao=opcao)


