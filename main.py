from data import DataManager
from playwright.sync_api import Playwright, sync_playwright, expect
from cotacao import Cotacao
EMAIL = "novembro2024ins@outlook.com"




data = DataManager()
cotacao = Cotacao()



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
        
        # opcao 2 = cotacao na progressive + card no trello
        # opcao 1 = cotacao na geico + card no trello
        # opcao 4 = cotacao apenas na geico
        #opcao 5 = cotacao apenas na progressive


        if opcao == 1:
            card_only()
        elif opcao == 2 or opcao == 3:
            card_and_cotacao(opcao)
        elif opcao == 4 or opcao == 5:
            fazer_cotacao_only(opcao)
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
    

def fazer_cotacao_only(opcao):
    data.pegar_excel()
    zipcode = data.endereco.split(" ")
    zipcode = zipcode[-1]
    with sync_playwright() as playwright:
        ## opcao 2/5 = cotacao na progressive
        ## opcao 3/4 = cotacao na geico
        if opcao == 3 or opcao == 4:
            cotacao.geico(playwright, zipcode=zipcode, first_name=data.first_name, 
                    last_name=data.last_name, date_birth=data.nascimento, 
                    address=data.endereco, vin=data.vin, email=EMAIL, financiado=data.financiado)
        elif opcao == 2 or opcao == 5:
            cotacao.progressive(playwright, zipcode=zipcode, first_name=data.first_name, 
                last_name=data.last_name, date_birth=data.nascimento, 
                address=data.endereco, vin=data.vin, email=EMAIL, financiado=data.financiado)
            

def card_and_cotacao(opcao):
    card_only()
    fazer_cotacao_only(opcao=opcao)


if __name__ == "__main__":
    main()