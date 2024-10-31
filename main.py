from data import DataManager
from progressive import get_quote
from playwright.sync_api import Playwright, sync_playwright, expect

data = DataManager()

data.pegar_excel()
data.criar_card_trello(data.nome, data.documento, data.endereco,
                       data.vin, data.financiado, data.nascimento)
zipcode = data.endereco.split(" ")
zipcode = zipcode[-1]

with sync_playwright() as playwright:
    get_quote(playwright, zipcode=zipcode, first_name=data.first_name, 
              last_name=data.last_name, date_birth=data.nascimento, 
              address=data.endereco, vin=data.vin, email="outubro2024ins@outlook.com")

data.delete_excel()
