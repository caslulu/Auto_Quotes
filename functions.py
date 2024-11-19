from playwright.sync_api import Playwright, sync_playwright, expect
from data import DataManager
from cotacao import Cotacao
EMAIL = "novembro2024ins@outlook.com"
data = DataManager()
cotacao = Cotacao()
metodos_cotacao = {
    "geico": cotacao.geico,
    "progressive": cotacao.progressive,
    }

def card_only():
    data.pegar_excel()
    data.criar_card_trello(data.nome, data.documento, data.endereco,
                       data.vin, data.financiado, data.nascimento, data.tempo_de_seguro, data.veiculos)
    

def fazer_cotacao_only(opcao):
    data.pegar_excel()
    zipcode = data.endereco.split(" ")
    zipcode = zipcode[-1]
    with sync_playwright() as playwright:
        if opcao in metodos_cotacao:
            metodos_cotacao[opcao]( playwright,  zipcode=zipcode, first_name=data.first_name, 
            last_name=data.last_name,  date_birth=data.nascimento,  address=data.endereco, 
            vin=data.vin[0],  email=EMAIL,  financiado=data.financiado )
            

def card_and_cotacao(opcao):
    card_only()
    fazer_cotacao_only(opcao=opcao)


def support_progressive(user, password, mensagem):
    with sync_playwright() as playwright:
            cotacao.progressive_support(playwright, user=user, password=password, mensagem=mensagem)
