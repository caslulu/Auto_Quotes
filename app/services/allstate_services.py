import time
class Allstate():
    
    def cotacao(self, playwright, zipcode, first_name, last_name, email, data_nascimento, rua, cidade, apt=None, veiculos=None, genero=None, estado_documento=None, tempo_de_seguro=None, tempo_no_endereco=None, estado_civil=None, nome_conjuge=None, data_nascimento_conjuge=None, documento_conjuge=None):
        self.browser = playwright.chromium.launch(
            headless=False,
            args=[
                "--disable-web-security",
                "--disable-blink-features=AutomationControlled",])
        
        context = self.browser.new_context()
        self.page = context.new_page()
        try:
            self.pagina_inicial(zipcode=zipcode, first_name=first_name,last_name=last_name, data_nascimento=data_nascimento, rua=rua, apt=apt)
        except:
            pass

        time.sleep(7000)
        context.close()
        self.browser.close()



        ## primeira pagina
    def pagina_inicial(self, zipcode, first_name, last_name, data_nascimento, rua, apt=None):
        self.page.goto("https://www.allstate.com/")
        self.page.get_by_role("textbox", name="Enter ZIP", exact=True).fill(zipcode)
        try:
            self.page.wait_for_load_state("networkidle")
        except:
            pass
        self.page.locator("#heroBundleGetQuote").click()
        self.page.get_by_role("button", name="start my quote").click()
        self.page.get_by_label("First name").click()
        self.page.get_by_label("First name").fill(first_name)
        self.page.get_by_label("Last name").click()
        self.page.get_by_label("Last name").fill(last_name)
        self.page.get_by_label("Date of birth").click()
        self.page.get_by_label("Date of birth").fill(data_nascimento)
        self.page.get_by_label("Street address").click()
        self.page.get_by_label("Street address").fill(rua)
        if apt != None:
            self.page.get_by_label("Apt/unit").click()
            self.page.get_by_label("Apt/unit").fill(apt)
        self.page.get_by_role("button", name="next").click()
        self.page.pause()
        
        
