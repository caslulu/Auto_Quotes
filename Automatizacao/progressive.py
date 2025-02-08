import time
from Data.data import *

class Progressive(DataManager):
    def __init__(self) -> None:
        super().__init__()
        self.informacoes_para_cotacao()
    #Suporte
    def suporte(self, playwright, mensagem, usuario, senha):

        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        self.page = context.new_page()
        self.page.goto("https://account.apps.progressive.com/access/login?cntgrp=A&fd=accountHome")
        self.page.get_by_placeholder("User ID").fill(usuario)
        self.page.get_by_placeholder("Password").click()
        self.page.get_by_placeholder("Password").fill(senha)
        self.page.get_by_role("button", name="Log In").click()
        self.page.wait_for_load_state("networkidle")
        self.page.goto("https://policyservicing.apps.progressive.com/app/account-home?brand=Progressive")
        self.page.get_by_role("link", name="Contact Us").click()
        self.page.get_by_role("link", name="Start chat").click()
        self.page.get_by_placeholder("Enter a message...").fill("live agent")
        self.page.get_by_role("button", name="Send").click()
        self.page.get_by_label("Start Live Chat").click()
        time.sleep(30)
        self.page.get_by_placeholder("Enter a message...").fill(mensagem)
        self.page.get_by_role("button", name="Send").click()
        time.sleep(4000)

    #Cotacao // Junta todas as funcoes abaixo para fazer a cotacao.
    def cotacao(self, playwright,modelo, delete):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        self.page = context.new_page()
        time.sleep(500000)
        
        self.pagina_inicial()

        try:
            self.page.wait_for_load_state("networkidle")
        except:
            pass

        self.informacoes_basicas()
        
        self.informacoes_endereco()
        try:
            self.informacoes_veiculos1()
            self.informacoes_pessoais1()
            self.informacoes_seguro_anterior()
        except:
            self.informacoes_veiculo2()
            self.informacoes_pessoais2()
            self.informacoes_seguro_anterior()



        time.sleep(30)

        modelo(self.financiado, opcao="progressive", delete=delete)

        context.close()
        browser.close()

    #Informacoes Zipcode
    def pagina_inicial(self):
            self.page.goto("https://www.progressive.com/")
            self.page.get_by_role("link", name="Or, see all 30+ products").click()
            self.page.get_by_role("option", name="Auto", exact=True).click()
            self.page.get_by_role("textbox", name="Enter ZIP Code").fill(self.zipcode)
            self.page.get_by_role("button", name="Get a quote").click()

    #Informacoes Basicas
    def informacoes_basicas(self):
        self.page.goto("https://autoinsurance1.progressivedirect.com/0/UQA/Quote") 
        self.page.goto("https://autoinsurance1.progressivedirect.com/0/UQA/Quote/NameEdit")
        self.page.get_by_label("First Name").click()
        self.page.get_by_label("First Name").fill(self.first_name)
        self.page.get_by_label("Last Name").click()
        self.page.get_by_label("Last Name").fill(self.last_name)
        self.page.get_by_label("Primary email address").click()
        self.page.get_by_label("Primary email address").fill(self.email)
        self.page.get_by_label("Date of birth*").click()
        self.page.get_by_label("Date of birth*").fill(self.nascimento)
        self.page.get_by_role("button", name="Continue").click()

    #Informacoes do Endereco.
    def informacoes_endereco(self):
        self.page.wait_for_load_state("load")
        self.page.get_by_label("Street number and name").click()
        self.page.get_by_label("Street number and name").fill(self.rua)
        self.page.get_by_label("Apt./Unit #").click()
        if self.apt != None:
            self.page.get_by_label("Apt./Unit #").fill(self.apt)
            self.page.get_by_label("City").click()
        self.page.get_by_label("City").fill(self.cidade)
        self.page.get_by_role("button", name="Ok, start my quote").click()

    #Informacoes do Veiculo.   
    def informacoes_veiculos1(self):
        try:
            self.page.set_default_timeout(7000)
            self.page.get_by_role("button", name="No, I'll add my own").click()
        except:
            pass
        self.page.set_default_timeout(30000)
        i = 1    
        for veiculo in self.lista_vin:
            self.page.get_by_role("link", name="Enter by VIN").click()
            self.page.get_by_label("Vehicle Identification Number").fill(veiculo)
            self.page.get_by_label("Learn more aboutVehicle Use*").select_option("1")
            time.sleep(1)
            if self.financiado == "Financiado":
                self.page.get_by_label("Own or lease?").select_option("2") 
            else:
                self.page.get_by_label("Own or lease?").select_option("3")
            time.sleep(1)

            if self.tempo_com_veiculo == "5 anos+":
                self.page.get_by_label("How long have you had this").select_option("D")

            elif self.tempo_com_veiculo == "1-3 Anos": 
                self.page.get_by_label("How long have you had this").select_option("B")

            else:
                self.page.get_by_label("How long have you had this").select_option("E")

            time.sleep(1)
            self.page.get_by_label("Learn more aboutAnnual").select_option(index=1)

            time.sleep(5)


            if len(self.lista_vin) >= 2 and i < len(self.lista_vin):
                self.page.get_by_role("button", name="+Add another vehicle?").click()
                i += 1
        self.page.get_by_role("button", name="Continue").click()
    
    #Informacoes Pessoais 
    def informacoes_pessoais1(self):
        if self.genero == "Masculino":
            self.page.get_by_label("Male", exact=True).check()
        else:
            self.page.get_by_label("Female").check()
        self.page.get_by_label("Marital Status*").select_option("S")

        try:
            self.page.locator("label:has-text('Primary Residence Insurance*')").wait_for(timeout=7000)
            self.page.get_by_label("Primary Residence Insurance*").select_option("T")
            if self.estado_documento != "IT":
                self.page.get_by_label("Has your license been valid").get_by_label("Yes").check()
            else:
                self.page.get_by_label("U.S. License Type*").select_option("F")

        except:
            self.page.get_by_label("Highest Level of Education*").select_option("2")
            self.page.get_by_label("Employment Status*").select_option("EM")
            self.page.get_by_label("Occupation view entire list").click()
            if self.genero == "Masculino":
                self.page.get_by_label("Occupation view entire list").fill("builder")
                self.page.get_by_role("option", name="Builder: Construction").click()
            else:
                self.page.get_by_label("Occupation view entire list").fill("cleaner")
                self.page.get_by_role("option", name="Cleaner").click()

            self.page.get_by_label("Primary Residence*").select_option("R")
            if self.estado_documento =="IT":
                self.page.get_by_label("U.S. License Type*").select_option("F")
        try:
            self.page.get_by_label("Accidents, claims, or other damages you had to a vehicle?*e.g.: hitting a car/").get_by_label("No").check()
            time.sleep(1)     
            self.page.get_by_label("Tickets or Violations?*").get_by_label("No").check()
        except:
            pass
        time.sleep(2)
        self.page.get_by_role("button", name="Continue").click()
        self.page.get_by_role("button", name="Continue").click()

    #Seguro Anterior
    def informacoes_seguro_anterior(self):
        try:
            if self.tempo_de_seguro == "Nunca Teve":
                self.page.get_by_label("Do you have auto insurance").get_by_label("No").check()
                self.page.get_by_label("Have you had auto insurance in the last 31 days?*").get_by_label("No").check()
            elif self.tempo_de_seguro == "Menos De 1 Ano":
                self.page.get_by_label("Do you have auto insurance").get_by_label("Yes").check()
                self.page.get_by_label("How long have you been with").select_option("A")
                self.page.get_by_label("Have you been insured for the").get_by_label("Yes").check()
            elif self.tempo_de_seguro == "1-3 Anos":
                self.page.get_by_label("Do you have auto insurance").get_by_label("Yes").check()
                self.page.get_by_label("How long have you been with").select_option("B")
            else:
                self.page.get_by_label("Do you have auto insurance").get_by_label("Yes").check()
                self.page.get_by_label("How long have you been with").select_option("C")
            self.page.get_by_label("Do you have non-auto policies").get_by_label("No").check()
            self.page.get_by_label("Have you had auto insurance").get_by_label("No").check()
            try:
                self.page.set_default_timeout(7000)
                if self.tempo_no_endereco == "Mais de 1 Ano":
                    self.page.get_by_label("How long have you lived at").select_option("C")
                else:
                    self.page.get_by_label("How long have you lived at").select_option("B")
            except:
                pass
            self.page.set_default_timeout(30000)
            self.page.get_by_role("button", name="Continue").click()
        except:
            print("Nao foi possivel encontrar alguns botoes")
            pass



## Nova Interface
    def informacoes_veiculo2(self):
        i = 1
        for veiculo in self.lista_vin:
            self.page.get_by_role("link", name="Enter vehicle by VIN").click()
            self.page.get_by_label("Vehicle Identification Number").fill(veiculo)
            self.page.get_by_label("Vehicle use", exact=True).select_option("1")
            if self.financiado == "Financiado":
                self.page.get_by_label("Own or lease?").select_option("2")
            else:
                self.page.get_by_label("Own or lease?").select_option("3")
            if self.tempo_com_veiculo == "Menos de 1 ano":
                self.page.get_by_label("How long have you had this").select_option("E")
            elif self.tempo_com_veiculo == "1-3 anos":
                self.page.get_by_label("How long have you had this").select_option("B")
            else:
                self.page.get_by_label("How long have you had this").select_option("D")
            time.sleep(1)
            self.page.get_by_label("Learn more aboutAnnual").select_option("0 - 3,999")
            if len(self.lista_vin) >= 2 and i < len(self.lista_vin):
                self.page.get_by_role("button", name="+Add another vehicle?").click()
                i += 1
        self.page.get_by_role("button", name="Continue").click()



    def informacoes_pessoais2(self):
        if self.genero == "Masculino":
            self.page.get_by_label("Male", exact=True).check()
        else:
            self.page.get_by_label("Female").check()
        self.page.get_by_label("Marital status").select_option("S")
        self.page.get_by_label("Primary residence insurance", exact=True).select_option("T")
        if self.estado_documento != "IT":
            self.page.get_by_label("U.S. License type").select_option("O")
            self.page.get_by_label("U.S. License status").select_option("V")
            self.page.get_by_label("Has your license been valid").get_by_label("Yes").check()
        else:
            self.page.get_by_label("U.S. License type").select_option("F")
        self.page.get_by_label("Accidents, claims, or other damages you had to a vehicle?*e.g.: hitting a car/").get_by_label("No").check()
        self.page.get_by_label("Tickets or violations?*").get_by_label("No").check()
        self.page.get_by_role("button", name="Continue").click()
        self.page.get_by_role("button", name="Continue").click()

        if self.tempo_de_seguro == "Nunca Teve":
            self.page.get_by_label("Do you have auto insurance").get_by_label("No").check()
            self.page.get_by_label("Have you had auto insurance in the last 31 days?*").get_by_label("No").check()
        elif self.tempo_de_seguro == "Menos De 1 Ano":
            self.page.get_by_label("Do you have auto insurance").get_by_label("Yes").check()
            self.page.get_by_label("How long have you been with").select_option("A")
            self.page.get_by_label("Have you been insured for the").get_by_label("Yes").check()
        elif self.tempo_de_seguro == "1-3 Anos":
            self.page.get_by_label("Do you have auto insurance").get_by_label("Yes").check()
            self.page.get_by_label("How long have you been with").select_option("B")
        else:
            self.page.get_by_label("Do you have auto insurance").get_by_label("Yes").check()
            self.page.get_by_label("How long have you been with").select_option("C")
        self.page.get_by_label("Do you have non-auto policies").get_by_label("No").check()
        self.page.get_by_label("Have you had auto insurance").get_by_label("No").check()
        try:
            self.page.set_default_timeout(7000)
            if self.tempo_no_endereco == "Mais de 1 Ano":
                self.page.get_by_label("How long have you lived at").select_option("C")
            else:
                self.page.get_by_label("How long have you lived at").select_option("B")
        except:
            pass
        self.page.set_default_timeout(30000)
        self.page.get_by_role("button", name="Continue").click()
        self.page.get_by_role("button", name="Continue").click()