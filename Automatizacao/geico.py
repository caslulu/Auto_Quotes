import time
from Data.data import DataManager

class Geico(DataManager):
    def __init__(self):
        super().__init__()
        self.informacoes_para_cotacao()

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
    def cotacao(self, playwright, modelo, delete):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        self.page = context.new_page()
        self.pagina_inicial()
        self.pagina_nascimento()
        self.pagina_nome()
        self.pagina_endereco()
        self.pagina_veiculo()
        time.sleep(30)
        modelo(data_dict["financiado"], opcao="geico", delete=delete)
        
        context.close()
        browser.close()

    # pagina do zipcode
    def pagina_inicial(self):
        self.page.goto("https://www.geico.com/auto-insurance/")
        self.page.get_by_label("Enter your ZIP code").click()
        self.page.get_by_label("Enter your ZIP code").fill(self.zipcode)
        self.page.get_by_role("button", name="Review Your Quote").click()

    #pagina nascimento
    def pagina_nascimento(self):
        self.page.get_by_placeholder("MM/DD/YYYY").fill(self.nascimento)
        time.sleep(2)
        self.page.get_by_role("button", name="Next").click()

    #pagina nome    
    def pagina_nome(self):
        
        self.page.get_by_label("First Name").fill(self.first_name)
        self.page.get_by_label("Last Name").click()
        self.page.get_by_label("Last Name").fill(self.last_name)
        time.sleep(2)
        self.page.get_by_role("button", name="Next").click()

    #pagina endereco
    def pagina_endereco(self):   
        self.page.get_by_placeholder("Enter a location").fill(f"{self.rua}, {self.cidade}")
        if self.apt != None:
            self.page.get_by_label("Apt #").click()
            self.page.get_by_label("Apt #").fill(self.apt)
            time.sleep(2)
        self.page.get_by_role("button", name="Next").click()
    
    #pagina veiculo
    def pagina_veiculo (self):
        try:
            ## pergunta do drive easy
            self.page.locator("#labelForYes").click()
            self.page.get_by_role("button", name="Next").click()
            ## pergunta se tem vin
            self.page.locator("#labelForYes").click()
            self.page.get_by_role("button", name="Next").click()
            # insere o vin
            self.page.get_by_placeholder("-----------------").fill(self.vin[0])
            self.page.get_by_role("button", name="Next").click()
        except:
            pass