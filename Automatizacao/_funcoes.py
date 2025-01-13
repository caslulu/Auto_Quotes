from playwright.sync_api import sync_playwright

from Data.data import DataManager
from Automatizacao.progressive import Progressive
from Automatizacao.geico import Geico
from Interface.preco import Preco


data = DataManager()

# vai apenas criar o card no trello
def card_only():
    data.pegar_excel()
    data.criar_card_trello()
    
# vai apenas fazer a cotacao
def fazer_cotacao_only(opcao):
    data.pegar_excel()
    with sync_playwright() as playwright:

        if opcao == "progressive":
            progressive = Progressive()
            preco = Preco()
            progressive.cotacao(playwright=playwright, data_dict=data.dict, f1=preco.financiado, f2=preco.quitado)

        elif opcao == "geico":
            preco = Preco()
            geico = Geico()
            geico.cotacao(playwright=playwright, data_dict=data.dict, f1=preco.financiado, f2=preco.quitado)
            

            
# vai fazer a cotacao e criar o card no trello
def card_and_cotacao(opcao):
    card_only()
    fazer_cotacao_only(opcao=opcao)

# Vai chamar o suporte no site da Progressive
def suporte_progressive(user, password, mensagem):
    progressive = Progressive()
    with sync_playwright() as playwright:
            progressive.suporte(playwright, user=user, password=password, mensagem=mensagem)

# Vai chamar o suporte no site da Geico
def suporte_geico(usuario, senha, mensagem, nome):
    geico = Geico()
    with sync_playwright() as playwright:
            geico.suporte(playwright, usuario=usuario, senha=senha, mensagem=mensagem, nome=nome)


