from playwright.sync_api import sync_playwright

from Automatizacao.progressive import *
from Automatizacao.geico import *
from Automatizacao.trello import *
from Interface.preco import *

trello = Trello()

def card_only():
    trello.criar_carta()
    
def fazer_cotacao_only(opcao):
    
    trello.informacoes_para_cotacao()
    with sync_playwright() as playwright:

        if opcao == "progressive":
            progressive = Progressive()
            preco = Preco()
            progressive.cotacao(playwright=playwright, data_dict=trello.informacoes, modelo=preco.tela)
        elif opcao == "geico":
            preco = Preco()
            geico = Geico()
            geico.cotacao(playwright=playwright, data_dict=trello.informacoes, modelo=preco.tela)
            

def card_and_cotacao(opcao):
    card_only()
    fazer_cotacao_only(opcao)

def chamar_suporte(opcao, usuario, senha, mensagem, nome = None):
    with sync_playwright() as playwright:
        if opcao == "Progressive":
            progressive = Progressive()
            progressive.suporte(playwright, usuario=usuario, senha=senha, mensagem=mensagem)
        elif opcao == "Geico":
            geico = Geico()
            geico.suporte(playwright, usuario=usuario, senha=senha, mensagem=mensagem, nome=nome)


