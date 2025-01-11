import time

class Geico:
    # Suporte
    def suporte(self, playwright, mensagem, usuario, senha, nome):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        self.page = context.new_page()
        self.page.goto("https://ecams.geico.com/login")
        self.page.get_by_label("User ID / Email / Policy").click()
        self.page.get_by_label("User ID / Email / Policy").fill(usuario)
        self.page.get_by_label("Password").click()
        self.page.get_by_label("Password").fill(senha)
        self.page.get_by_role("button", name="Login").click()
        try:
            self.page.wait_for_load_state("networkidle")
        except:
            pass
        self.page.get_by_label("Bring up More Info Menu.").click()
        self.page.get_by_role("link", name="Start New Quote").click()
        time.sleep(4)
        self.page.locator(".gabby-g").click()
        time.sleep(5)
        self.page.get_by_placeholder("Type your message...").fill("live agent")
        self.page.keyboard.press("Enter")
        time.sleep(5)
        self.page.get_by_role("button", name="Policy Details or Updates").click()
        self.page.get_by_role("button", name="Auto").click()
        time.sleep(50)
        self.page.get_by_placeholder("Type your message...").fill(f"{nome}")
        self.page.keyboard.press("Enter")
        time.sleep(5)
        self.page.get_by_placeholder("Type your message...").click()
        self.page.get_by_placeholder("Type your message...").fill(mensagem)
        self.page.keyboard.press("Enter")
        time.sleep(4000)

    # Junta todas as funcoes abaixo e faz a cotacao.
    def cotacao(self, playwright, data_dict):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        self.page = context.new_page()
        self.pagina_inicial(zipcode=data_dict["zipcode"])
        self.pagina_nascimento(date_birth=data_dict["date_birth"])
        self.pagina_nome(first_name=data_dict["first_name"], last_name=data_dict["last_name"])
        self.pagina_endereco(rua=data_dict["rua"],  cidade=data_dict["cidade"],apt=data_dict["apt"])
        self.pagina_veiculo(vin = data_dict["lista_vin"], financiado = data_dict["financiado"])

        time.sleep(250)
        context.close()
        browser.close()

    # pagina do zipcode
    def pagina_inicial(self, zipcode):
        self.page.goto("https://www.geico.com/auto-insurance/")
        self.page.get_by_label("Enter your ZIP code").click()
        self.page.get_by_label("Enter your ZIP code").fill(zipcode)
        self.page.get_by_role("button", name="Review Your Quote").click()


    #pagina nascimento
    def pagina_nascimento(self, date_birth):
        self.page.get_by_placeholder("MM/DD/YYYY").fill(date_birth)
        time.sleep(2)
        self.page.get_by_role("button", name="Next").click()

    #pagina nome    
    def pagina_nome(self, first_name, last_name):
        
        self.page.get_by_label("First Name").fill(first_name)
        self.page.get_by_label("Last Name").click()
        self.page.get_by_label("Last Name").fill(last_name)
        time.sleep(2)
        self.page.get_by_role("button", name="Next").click()


    #pagina endereco
    def pagina_endereco(self, rua, cidade, apt=None):   
        self.page.get_by_placeholder("Enter a location").fill(f"{rua}, {cidade}")
        if apt != None:
            self.page.get_by_label("Apt #").click()
            self.page.get_by_label("Apt #").fill(apt)
            time.sleep(2)
        self.page.get_by_role("button", name="Next").click()
    
    def pagina_veiculo (self, vin, financiado):
            try:
                ## pergunta do drive easy
                self.page.locator("#labelForYes").click()
                self.page.get_by_role("button", name="Next").click()
                ## pergunta se tem vin
                self.page.locator("#labelForYes").click()
                self.page.get_by_role("button", name="Next").click()
                # insere o vin
                self.page.get_by_placeholder("-----------------").fill(vin[0])
                self.page.get_by_role("button", name="Next").click()
            except:
                time.sleep(5)
                pass
            self.page.locator("#labelForYes").click()
            self.page.get_by_role("button", name="Next").click()
            # se o veiculo é financiado ou quitado
            if  financiado == "Financiado":
                self.page.locator("#labelForF").click()
            else:
                self.page.locator("#labelForO").click()

            # coloca o veiculo para o tempo mais antigo de compra possivel
            i=5
            while i > 0:
                try:
                    self.page.locator(f"#labelFor{i}").click()
                    break
                except:
                    i -= 1
            self.page.get_by_role("button", name="Next").click()
