import time

class Progressive():
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
    def cotacao(self, playwright, data_dict, modelo, delete):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        self.page = context.new_page()
        
        self.pagina_inicial(zipcode=data_dict["zipcode"])

        try:
            self.page.wait_for_load_state("networkidle")
        except:
            pass

        self.preencher_informacoes_basicas(first_name=data_dict["first_name"], last_name=data_dict["last_name"], email=data_dict["email"], date_birth=data_dict["date_birth"])
        
        self.preencher_informacoes_endereco(street=data_dict["rua"], city=data_dict["cidade"], apt=data_dict["apt"])

        self.preencher_informacoes_veiculos(quantidade_veiculos=data_dict["lista_vin"], financiado=data_dict["financiado"], tempo_com_veiculo=data_dict["tempo_com_veiculo"])

        self.preencher_informacoes_pessoais(genero=data_dict["genero"], estado=data_dict["estado"])
        
        self.preencher_informacoes_seguro_anterior(seguro=data_dict["tempo_seguro"], tempo_endereco=data_dict["tempo_no_endereco"])

        self.preencher_pergunta_snapshot():

        time.sleep(30)

        modelo(data_dict["financiado"], opcao="progressive", delete=delete)

        context.close()
        browser.close()

    #Informacoes Zipcode
    def preencher_pagina_inicial(self, zipcode):
            self.page.goto("https://www.progressive.com/")
            self.page.get_by_role("link", name="Or, see all 30+ products").click()
            self.page.get_by_role("option", name="Auto", exact=True).click()
            self.page.get_by_role("textbox", name="Enter ZIP Code").fill(zipcode)
            self.page.get_by_role("button", name="Get a quote").click()

    #Informacoes Basicas
    def preencher_informacoes_basicas(self, first_name, last_name, email, date_birth):
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
    def preencher_informacoes_endereco(self,street, city, apt=None):
        self.page.wait_for_load_state("load")
        self.page.get_by_label("Street number and name").click()
        self.page.get_by_label("Street number and name").fill(street)
        self.page.get_by_label("Apt./Unit #").click()
        if apt != None:
            self.page.get_by_label("Apt./Unit #").fill(apt)
            self.page.get_by_label("City").click()
        self.page.get_by_label("City").fill(city)
        self.page.get_by_role("button", name="Ok, start my quote").click()






    #Informacoes do Veiculo.   
    def preencher_informacoes_veiculos(self, quantidade_veiculos, financiado, tempo_com_veiculo):
        try:
            self.page.set_default_timeout(7000)
            self.page.get_by_role("button", name="No, I'll add my own").click()
        except:
                self.page.set_default_timeout(30000)
        i = 1    
        for veiculo in quantidade_veiculos: 
            self.page.get_by_role("link", name="Enter by VIN").click()
            self.page.get_by_label("Vehicle Identification Number").fill(veiculo)
            self.page.get_by_label("Learn more aboutVehicle Use*").select_option("1")
            time.sleep(1)
            self.estado_pagamento_veiculo(financiado)
            time.sleep(1)
            self.tempo_com_veiculo_opcao(tempo_com_veiculo)
            time.sleep(1)
            self.page.get_by_label("Learn more aboutAnnual").select_option(index=1)
            time.sleep(5)
            if len(quantidade_veiculos) >= 2 and i < len(quantidade_veiculos):
                self.page.get_by_role("button", name="+Add another vehicle?").click()
                i += 1
        self.page.get_by_role("button", name="Continue").click()

    def estado_pagamento_veiculo(self,financiado_ou_quitado):
            if financiado_ou_quitado == "Financiado":
                self.page.get_by_label("Own or lease?").select_option("2")
            else:
                self.page.get_by_label("Own or lease?").select_option("3")       

    def tempo_com_veiculo_opcao(self, tempo_com_veiculo):
        if tempo_com_veiculo == "5 anos+":
                self.page.get_by_label("How long have you had this").select_option("D")
                time.sleep(1)
        elif tempo_com_veiculo == "1-3 Anos": 
                self.page.get_by_label("How long have you had this").select_option("B")
                time.sleep(1)
        else:
                self.page.get_by_label("How long have you had this").select_option("E")

    #Informacoes Pessoais 
    def preencher_informacoes_pessoais(self, genero, estado):
        if genero == "Masculino":
            self.page.get_by_label("Male", exact=True).check()
        else:
            self.page.get_by_label("Female").check()
        self.page.get_by_label("Marital Status*").select_option("S")

        try:
            self.page.locator("label:has-text('Primary Residence Insurance*')").wait_for(timeout=7000)
            self.page.get_by_label("Primary Residence Insurance*").select_option("T")
            if estado != "IT":
                self.page.get_by_label("Has your license been valid").get_by_label("Yes").check()
            else:
                self.page.get_by_label("U.S. License Type*").select_option("F")

        except:
            self.page.get_by_label("Highest Level of Education*").select_option("2")
            self.page.get_by_label("Employment Status*").select_option("EM")
            self.page.get_by_label("Occupation view entire list").click()
            if genero == "Masculino":
                self.page.get_by_label("Occupation view entire list").fill("builder")
                self.page.get_by_role("option", name="Builder: Construction").click()
            else:
                self.page.get_by_label("Occupation view entire list").fill("cleaner")
                self.page.get_by_role("option", name="Cleaner").click()

            self.page.get_by_label("Primary Residence*").select_option("R")
            if estado =="IT":
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
    def preencher_informacoes_seguro_anterior(self, seguro, tempo_endereco):
        try:
            self.seguro_anterior(seguro)
            self.tempo_morando_no_endereco(tempo_endereco)
            time.sleep(4)

            self.page.get_by_role("button", name="Continue").click()
        except:
            print("Nao foi possivel encontrar alguns botoes")
            pass
   
    def seguro_anterior(self, seguro): 

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

    def tempo_morando_no_endereco(self, tempo_endereco):
        try:
            if tempo_endereco == "Mais de 1 Ano":
                self.page.get_by_label("How long have you lived at").select_option("C")
            else:
                self.page.get_by_label("How long have you lived at").select_option("B")
        except:
            pass

        
    #Pergunta Snapshot
    def preencher_pergunta_snapshot(self):
        try:
            try:
                self.page.get_by_label("Mobile app", exact=True).check()
            except:
                self.page.get_by_label("Yes, please").check()
            self.page.get_by_role("button", name="Continue").click()
            self.page.get_by_role("button", name="No thanks, just auto").click()
        except:
            pass