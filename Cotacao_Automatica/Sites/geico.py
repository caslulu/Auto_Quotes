import time

class Geico:
    def cotacao(self, playwright, data_dict):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        self.page = context.new_page()
        self.pagina_inicial(zipcode=data_dict["zipcode"])
        self.pagina_nascimento(date_birth=data_dict["date_birth"])
        self.pagina_nome(first_name=data_dict["first_name"], last_name=data_dict["last_name"])
        self.pagina_endereco(rua=data_dict["rua"],  cidade=data_dict["cidade"],apt=data_dict["apt"])
        #self.pagina_veiculo(veiculo = data_dict["veiculo"])

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
    
    def pagina_veiculo (self, vin):
        pass