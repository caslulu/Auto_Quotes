from data import DataManager
from cotacoes.progressive import get_quote_progressive
from cotacoes.geico import get_quote_geico
from playwright.sync_api import Playwright, sync_playwright, expect
EMAIL = "novembro2024ins@outlook.com"




data = DataManager()



def main():
    try:
        opcao = int(input("\
                                1) Apenas criar card Trello \n \
                                2) Criar card trello e fazer cotacao na progressive \n \
                                3) Criar card trello e fazer cotacao na geico \n \
                                4) Apenas cotacao na geico \n \
                                5) Apenas cotacao na progressive \n \
                                6) Deletar ultima linha excel \n \
                                7) Sair \n" ))
        if opcao == 1:
            card_only()
        elif opcao == 2:
            card_and_progressive()
        elif opcao == 3:
            card_and_geico()
        elif opcao == 4:
            geico_only()
        elif opcao == 5:
            progressive_only()
        elif opcao == 6:
            data.delete_excel()
        elif opcao == 7:
            print("Encerrado")
        else:
            raise ValueError
    except ValueError:
        main()


def card_only():
    data.pegar_excel()
    data.criar_card_trello(data.nome, data.documento, data.endereco,
                       data.vin, data.financiado, data.nascimento, data.tempo_de_seguro, data.veiculo)
    

def progressive_only():
    data.pegar_excel()
    zipcode = data.endereco.split(" ")
    zipcode = zipcode[-1]
    with sync_playwright() as playwright:
        get_quote_progressive(playwright, zipcode=zipcode, first_name=data.first_name, 
                last_name=data.last_name, date_birth=data.nascimento, 
                address=data.endereco, vin=data.vin, email=EMAIL, financiado=data.financiado)
        
def geico_only():
    data.pegar_excel()
    zipcode = data.endereco.split(" ")
    zipcode = zipcode[-1]
    with sync_playwright() as playwright:
        get_quote_geico(playwright, zipcode=zipcode, first_name=data.first_name, 
                last_name=data.last_name, date_birth=data.nascimento, 
                address=data.endereco, vin=data.vin, email=EMAIL, financiado=data.financiado)



def card_and_progressive():
    card_only()
    progressive_only()

def card_and_geico():
    card_only()
    geico_only()


if __name__ == "__main__":
    main()