import time
from Data.data import DataManager
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
data = DataManager()
data.pegar_excel()

class Progressive():
    def cotacao(self, playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        self.page = context.new_page()
        
        self.pagina_inicial(zipcode=data.zipcode)

        try:
            self.page.wait_for_load_state("networkidle")
        except:
            pass

        self.informacoes_basicas(first_name=data.first_name, last_name=data.last_name, email=EMAIL, date_birth=data.nascimento)
        
        self.informacoes_endereco(address=data.endereco)

        self.informacoes_veiculos(quantidade_veiculos=data.lista_vin, financiado=data.financiado)

        self.informacoes_pessoais(genero=data.genero, estado=data.estado_documento)
        
        self.informacoes_seguro_anterior(seguro=data.tempo_de_seguro)
        
        time.sleep(250)
        context.close()
        browser.close()

    #Informacoes Zipcode
    def pagina_inicial(self, zipcode):
        self.page.goto("https://www.progressive.com/")
        self.page.get_by_role("link", name="Or, see all 30+ products").click()
        self.page.get_by_role("option", name="Auto", exact=True).click()
        self.page.get_by_role("textbox", name="Enter ZIP Code").fill(zipcode)
        self.page.get_by_role("button", name="Get a quote").click()

    #Informacoes Basicas
    def informacoes_basicas(self, first_name, last_name, email, date_birth):
        self.page.goto("https://autoinsurance1.progressivedirect.com/0/UQA/Quote") 
        self.page.goto("https://autoinsurance1.progressivedirect.com/0/UQA/Quote/NameEdit")
        self.page.get_by_label("First Name").click()
        self.page.get_by_label("First Name").fill(first_name)
        self.page.get_by_label("Last Name").click()
        self.page.get_by_label("Last Name").fill(last_name)
        self.page.get_by_label("Primary email address").click()
        self.page.get_by_label("Primary email address").fill(email)
        self.page.get_by_label("Date of birth*").click()
        self.page.get_by_label("Date of birth*").fill(date_birth)
        self.page.get_by_role("button", name="Continue").click()

    #Informacoes do Endereco.
    def informacoes_endereco(self, address):
        self.page.wait_for_load_state("load")
        self.page.get_by_label("Street number and name").click()
        self.page.get_by_label("Street number and name").fill(address)
        time.sleep(10)
        self.page.get_by_role("button", name="Ok, start my quote").click()

    #Informacoes do Veiculo.   
    def informacoes_veiculos(self, quantidade_veiculos, financiado):
        i = 1    
        for veiculo in quantidade_veiculos: 
            self.page.get_by_role("link", name="Enter by VIN").click()
            self.page.get_by_label("Vehicle Identification Number").fill(veiculo)
            self.page.get_by_label("Learn more aboutVehicle Use*").select_option("1")
            time.sleep(0.5)
            if financiado == "Financiado":
                self.page.get_by_label("Own or lease?").select_option("2")
            else:
                self.page.get_by_label("Own or lease?").select_option("3")
                time.sleep(0.5)
            try:
                self.page.get_by_label("How long have you had this").select_option("D")
                time.sleep(0.5)
                self.page.get_by_label("Learn more aboutAnnual").select_option(index=1)
                time.sleep(5)
            except:
                print("Nao foi possivel encotrar alguns botoes.")
                time.sleep(7)
                continue
            if len(quantidade_veiculos) >= 2:
                if i < len(quantidade_veiculos):
                    self.page.get_by_role("button", name="+Add another vehicle?").click()
                    i += 1
        self.page.get_by_role("button", name="Continue").click()

    #Informacoes Pessoais 
    def informacoes_pessoais(self, genero, estado):
        try:
            if genero == "Masculino":
                self.page.get_by_label("Male", exact=True).check()
            else:
                self.page.get_by_label("Female").check()
            self.page.get_by_label("Marital Status*").select_option("S")
            self.page.get_by_label("Primary Residence Insurance*").select_option("T")
            if estado != "IT":
                self.page.get_by_label("Has your license been valid").get_by_label("Yes").check()
            else:
                self.page.get_by_label("U.S. License Type*").select_option("F")


        except:
            if genero == "Masculino":
                self.page.get_by_label("Male", exact=True).check()
            else:
                self.page.get_by_label("Female").check()
            self.page.get_by_label("Marital Status*").select_option("S")
            self.page.get_by_label("Highest Level of Education*").select_option("2")
            self.page.get_by_label("Employment Status*").select_option("EM")
            self.page.get_by_label("Occupation view entire list").click()
            if genero == "Masculino":
                self.page.get_by_label("Occupation view entire list").fill("builder")
                self.page.get_by_role("option", name="Builder: Construction").click()
            else:
                self.page.get_by_label("Occupation view entire list").fill("cleaner")
                self.page.get_by_text("Cleaner").click()

            self.page.get_by_label("Primary Residence*").select_option("T")

            # if estado != "IT":
            #         self.page.get_by_label("Has your license been valid").get_by_label("Yes").check()
            # else:
            #     self.page.get_by_label("U.S. License Type*").select_option("F")
        else:
            time.sleep(10)
            pass
        finally:
            time.sleep(10)

        self.page.get_by_role("button", name="Continue").click()
        self.page.wait_for_load_state("networkidle")
        self.page.get_by_role("button", name="Continue").click()

    #Seguro Anterior
    def informacoes_seguro_anterior(self, seguro):
        try:
            if seguro == "Nunca Teve":
                self.page.get_by_label("Do you have auto insurance").get_by_label("No").check()
                self.page.get_by_label("Have you had auto insurance in the last 31 days?*").get_by_label("No").check()
            elif seguro == "Menos De 1 Ano":
                self.page.get_by_label("Do you have auto insurance").get_by_label("Yes").check()
                self.page.get_by_label("How long have you been with").select_option("A")
                self.page.get_by_label("Have you been insured for the").get_by_label("Yes").check()
            elif seguro == "1-3 Anos":
                self.page.get_by_label("Do you have auto insurance").get_by_label("Yes").check()
                self.page.get_by_label("How long have you been with").select_option("B")
            else:
                self.page.get_by_label("Do you have auto insurance").get_by_label("Yes").check()
                self.page.get_by_label("How long have you been with").select_option("C")
            self.page.get_by_label("Do you have non-auto policies").get_by_label("No").check()
            self.page.get_by_label("Have you had auto insurance").get_by_label("No").check()
            time.sleep(7)
            self.page.get_by_role("button", name="Continue").click()
            self.page.get_by_label("Mobile app", exact=True).check()
            self.page.get_by_role("button", name="Continue").click()
            self.page.get_by_role("button", name="No thanks, just auto").click()
        except:
            print("Nao foi possivel encontrar alguns botoes")
            pass