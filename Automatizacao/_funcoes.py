from playwright.sync_api import sync_playwright

from Automatizacao.progressive import *
from Automatizacao.geico import *
from Automatizacao.trello import *
from Interface.preco import *

def card_only():
    trello = Trello()
    trello.criar_carta()
    
def fazer_cotacao_only(opcao):
    with sync_playwright() as playwright:
        preco = Preco()
        if opcao == "progressive":
            progressive = Progressive()
            progressive.cotacao(playwright=playwright, modelo=preco.tela, delete=progressive.delete_excel)

        elif opcao == "geico":
            geico = Geico()
            geico.cotacao(playwright=playwright, modelo=preco.tela, delete=geico.delete_excel)
            

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


