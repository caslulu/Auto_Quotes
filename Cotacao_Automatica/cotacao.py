from Cotacao_automatica.Sites.progressive import Progressive


progressive = Progressive()



class Cotacao():
    def automatico(self, opcao, playwright):
        ## Fazer cotacao na geico
        if opcao == "geico":
            pass

        ## Fazer cotacao na progressive.
        elif opcao == "progressive":
            progressive.cotacao(playwright=playwright)
