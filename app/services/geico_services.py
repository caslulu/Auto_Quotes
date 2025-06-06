import time

class Geico():
    def cotacao(self, playwright, zipcode, first_name, last_name, email, data_nascimento, rua, cidade, apt=None, veiculos=None, genero=None, estado_documento=None, tempo_de_seguro=None, tempo_no_endereco=None, estado_civil=None, nome_conjuge=None, data_nascimento_conjuge=None, documento_conjuge=None):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        self.page = context.new_page()
        self.pagina_inicial(zipcode=zipcode)
        self.pagina_nascimento(data_nascimento=data_nascimento)
        self.pagina_nome(first_name=first_name, last_name=last_name)
        self.pagina_endereco(rua=rua, cidade=cidade, apt=apt)

        time.sleep(3000)
        
        context.close()
        browser.close()

    # pagina do zipcode
    def pagina_inicial(self, zipcode):
        self.page.goto("https://www.geico.com/auto-insurance/")
        self.page.get_by_label("Enter your ZIP code").click()
        self.page.get_by_label("Enter your ZIP code").fill(zipcode)
        self.page.get_by_role("button", name="Get Your Quote").click()

    #pagina nascimento
    def pagina_nascimento(self, data_nascimento):
        self.page.get_by_placeholder("MM/DD/YYYY").fill(data_nascimento)
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
    def pagina_endereco(self, rua, cidade, apt):   
        self.page.get_by_placeholder("Enter a location").fill(f"{rua}, {cidade}")
        if apt != None:
            self.page.get_by_label("Apt #").click()
            self.page.get_by_label("Apt #").fill(apt)
            time.sleep(2)
        self.page.get_by_role("button", name="Next").click()
