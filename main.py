from data import DataManager
from progressive import get_quote
from playwright.sync_api import Playwright, sync_playwright, expect
data = DataManager()
def main():
    try:
        opcao = int(input("\
 1) Apenas criar card Trello \n \
2) Criar card trello e fazer cotacao na progressive \n \
3) Apenas cotacoa na progressive \n \
4) Deletar ultima linha excel \n \
5) Sair \n" ))
        if opcao == 1:
            card_only()
        elif opcao == 2:
            card_and_progressive()
        elif opcao == 3:
            progressive_only()
        elif opcao == 4:
            data.delete_excel()
        elif opcao == 5:
            print("Encerrado")
        else:
            raise ValueError
    except ValueError:
        main()














def card_only():
    data.pegar_excel()
    data.criar_card_trello(data.nome, data.documento, data.endereco,
                       data.vin, data.financiado, data.nascimento, data.tempo_de_seguro)
    

def card_and_progressive():
    card_only()
    zipcode = data.endereco.split(" ")
    zipcode = zipcode[-1]

    with sync_playwright() as playwright:
        get_quote(playwright, zipcode=zipcode, first_name=data.first_name, 
                last_name=data.last_name, date_birth=data.nascimento, 
                address=data.endereco, vin=data.vin, email="novembro2024ins@outlook.com")
        
def progressive_only():
    data.pegar_excel()
    zipcode = data.endereco.split(" ")
    zipcode = zipcode[-1]
    with sync_playwright() as playwright:
        get_quote(playwright, zipcode=zipcode, first_name=data.first_name, 
                last_name=data.last_name, date_birth=data.nascimento, 
                address=data.endereco, vin=data.vin, email="novembro2024ins@outlook.com")



if __name__ == "__main__":
    main()