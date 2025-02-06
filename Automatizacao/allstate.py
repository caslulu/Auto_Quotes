from playwright.sync_api import sync_playwright
from Data.data import *
import time
class Allstate(DataManager):
    def __init__(self):
        super().__init__()
        self.informacoes_para_cotacao()
    def cotacao(self, playwright, modelo, delete):
        self.browser = playwright.chromium.launch(
            headless=False,
            args=[
                "--disable-web-security",
                "--disable-blink-features=AutomationControlled",])
        
        context = self.browser.new_context()
        self.page = context.new_page()
        self.pagina_inicial()

        time.sleep(70)
        modelo(self.financiado, opcao="progressive", delete=delete)
        context.close()
        self.browser.close()
        ## primeira pagina
    def pagina_inicial(self):
        self.page.goto("https://www.allstate.com/")
        self.page.get_by_role("textbox", name="Enter ZIP", exact=True).fill(self.zipcode)
        try:
            self.page.wait_for_load_state("networkidle")
        except:
            pass
        self.page.locator("#heroBundleGetQuote").click()
        self.page.get_by_role("button", name="start my quote").click()
        self.page.get_by_label("First name").click()
        self.page.get_by_label("First name").fill(self.first_name)
        self.page.get_by_label("Last name").click()
        self.page.get_by_label("Last name").fill(self.last_name)
        self.page.get_by_label("Date of birth").click()
        self.page.get_by_label("Date of birth").fill(self.nascimento)
        self.page.get_by_label("Street address").click()
        self.page.get_by_label("Street address").fill(self.rua)
        if self.apt != None:
            self.page.get_by_label("Apt/unit").click()
            self.page.get_by_label("Apt/unit").fill(self.apt)
        self.page.get_by_role("button", name="next").click()
        
        
