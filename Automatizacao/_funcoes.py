from playwright.sync_api import sync_playwright

from Automatizacao.progressive import *
from Automatizacao.geico import *
from Automatizacao.trello import *
from Interface.preco import *



trello = Trello()

# vai apenas criar o card no trello
def card_only():
    trello.criar_card()
    
# vai apenas fazer a cotacao
def fazer_cotacao_only(opcao):
    
    trello.informacoes_para_cotacao()
    with sync_playwright() as playwright:

        if opcao == "progressive":
            progressive = Progressive()
            preco = Preco()
            progressive.cotacao(playwright=playwright, data_dict=trello.informacoes, f1=preco.financiado, f2=preco.quitado)

        elif opcao == "geico":
            preco = Preco()
            geico = Geico()
            geico.cotacao(playwright=playwright, data_dict=trello.informacoes, f1=preco.financiado, f2=preco.quitado)
            

            
# vai fazer a cotacao e criar o card no trello
def card_and_cotacao(opcao):
    card_only()
    fazer_cotacao_only(opcao=opcao)

# Vai chamar o suporte
def chamar_suporte(opcao, usuario, senha, mensagem, nome = None):
    with sync_playwright() as playwright:
        if opcao == "Progressive":
            progressive = Progressive()
            progressive.suporte(playwright, usuario=usuario, senha=senha, mensagem=mensagem)
        elif opcao == "Geico":
            geico = Geico()
            geico.suporte(playwright, usuario=usuario, senha=senha, mensagem=mensagem, nome=nome)


