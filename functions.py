from playwright.sync_api import Playwright, sync_playwright, expect
from data import DataManager
from cotacao import Cotacao
EMAIL = "novembro2024ins@outlook.com"
data = DataManager()
cotacao = Cotacao()

def card_only():
    data.pegar_excel()
    data.criar_card_trello(data.nome, data.documento, data.endereco,
                       data.vin, data.financiado, data.nascimento, data.tempo_de_seguro, data.veiculo)
    

def fazer_cotacao_only(opcao):
    data.pegar_excel()
    zipcode = data.endereco.split(" ")
    zipcode = zipcode[-1]
    with sync_playwright() as playwright:
        if opcao == "geico":
            cotacao.geico(playwright, zipcode=zipcode, first_name=data.first_name, 
                    last_name=data.last_name, date_birth=data.nascimento, 
                    address=data.endereco, vin=data.vin, email=EMAIL, financiado=data.financiado)
        elif opcao == "progressive":
            cotacao.progressive(playwright, zipcode=zipcode, first_name=data.first_name, 
                last_name=data.last_name, date_birth=data.nascimento, 
                address=data.endereco, vin=data.vin, email=EMAIL, financiado=data.financiado)
            

def card_and_cotacao(opcao):
    card_only()
    fazer_cotacao_only(opcao=opcao)
