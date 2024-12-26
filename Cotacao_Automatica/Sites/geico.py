import time

class Geico:
    def cotacao(self, playwright, data_dict):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        self.page = context.new_page()
        self.pagina_inicial(zipcode=data_dict["zipcode"])
        self.pagina_nascimento(date_birth=data_dict["date_birth"])
        self.pagina_nome(first_name=data_dict["first_name"], last_name=data_dict["last_name"])
        self.pagina_endereco(address=data_dict["endereco"])

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
        self.page.get_by_role("button", name="Next").click()

    #pagina nome    
    def pagina_nome(self, first_name, last_name):
        
        self.page.get_by_label("First Name").fill(first_name)
        self.page.get_by_label("Last Name").click()
        self.page.get_by_label("Last Name").fill(last_name)
        self.page.get_by_role("button", name="Next").click()


    #pagina endereco
    def pagina_endereco(self, address):
        self.page.get_by_placeholder("Enter a location").fill(address)
        self.page.get_by_role("button", name="Next").click()