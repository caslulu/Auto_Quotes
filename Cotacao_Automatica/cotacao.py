import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


class Cotacao():
    def automatico(self, playwright, zipcode, first_name, last_name, date_birth, address, vin, email, financiado, opcao, quantidade_veiculos, genero, estado, seguro):
        ## Fazer cotacao na geico
        if opcao == "geico":
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            #1, zipcode
            page.goto("https://www.geico.com/auto-insurance/")
            page.get_by_label("Enter your ZIP code").click()
            page.get_by_label("Enter your ZIP code").fill(zipcode)
            page.get_by_role("button", name="Review Your Quote").click()
            #2 pagina, data de nascimento
            page.wait_for_load_state("networkidle")
            page.get_by_placeholder("MM/DD/YYYY").fill(date_birth)
            page.get_by_role("button", name="Next").click()
            #3 pagina, Nome
            page.wait_for_load_state("networkidle")
            page.get_by_label("First Name").fill(first_name)
            page.get_by_label("First Name").press("Tab")
            page.get_by_label("Last Name").fill(last_name)
            page.get_by_role("button", name="Next").click()
            #4 pagina, endereco
            page.wait_for_load_state("networkidle")
            page.goto("https://sales.geico.com/quote")
            page.get_by_placeholder("Enter a location").fill(address)
            page.get_by_role("button", name="Next").click()

            #####checar o que faz essa parte########
            page.wait_for_load_state("networkidle")
            try:
                page.locator("#labelForYes").click()
                page.get_by_role("button", name="Next").click()
                page.wait_for_load_state("networkidle")
                page.locator("#labelForYes").click()
                page.get_by_role("button", name="Next").click()
                page.wait_for_load_state("networkidle")
                page.get_by_placeholder("-----------------").fill(vin)
                page.get_by_role("button", name="Next").click()
            except:
                pass
            #page.get_by_role("button", name="Next").click()
            # page.locator("#labelForYes").click()
            # page.get_by_role("button", name="Next").click()
            # page.get_by_role("button", name="Next").click()
            # page.locator("#labelForF").click()
            time.sleep(350)
            #------------#
            context.close()
            browser.close()


            
        ## Fazer cotacao na progressive.
        elif opcao == "progressive":
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            #pagina inicial, coloca o zipcode.
            page.goto("https://www.progressive.com/")
            page.get_by_role("link", name="Or, see all 30+ products").click()
            page.get_by_role("option", name="Auto", exact=True).click()
            page.get_by_role("textbox", name="Enter ZIP Code").fill(zipcode)
            page.get_by_role("button", name="Get a quote").click()

            try:
                page.wait_for_load_state("networkidle")
            except:
                pass

            #Informacoes Basicas.
            page.goto("https://autoinsurance1.progressivedirect.com/0/UQA/Quote") 
            page.goto("https://autoinsurance1.progressivedirect.com/0/UQA/Quote/NameEdit")
            page.get_by_label("First Name").click()
            page.get_by_label("First Name").fill(first_name)
            page.get_by_label("Last Name").click()
            page.get_by_label("Last Name").fill(last_name)
            page.get_by_label("Primary email address").click()
            page.get_by_label("Primary email address").fill(email)
            page.get_by_label("Date of birth*").click()
            page.get_by_label("Date of birth*").fill(date_birth)
            page.get_by_role("button", name="Continue").click()

            #Informacoes do Endereco.
            page.wait_for_load_state("load")
            page.get_by_label("Street number and name").click()
            page.get_by_label("Street number and name").fill(address)
            time.sleep(10)
            page.get_by_role("button", name="Ok, start my quote").click()

            #Informacoes do Veiculo.
            for veiculo in quantidade_veiculos:
                i = 1
                page.get_by_role("link", name="Enter by VIN").click()
                page.get_by_label("Vehicle Identification Number").fill(veiculo)
                page.get_by_label("Learn more aboutVehicle Use*").select_option("1")
                time.sleep(0.5)
                if financiado == "Financiado":
                    page.get_by_label("Own or lease?").select_option("2")
                else:
                    page.get_by_label("Own or lease?").select_option("3")
                    time.sleep(0.5)
                try:
                    page.get_by_label("How long have you had this").select_option("D")
                    time.sleep(0.5)
                    page.get_by_label("Learn more aboutAnnual").select_option(index=1)
                    time.sleep(5)
                except:
                    print("Nao foi possivel encotrar alguns botoes.")
                    time.sleep(7)
                    continue
                if len(quantidade_veiculos) >= 2:
                    if i < len(quantidade_veiculos):
                        page.get_by_role("button", name="+Add another vehicle?").click()
                        i += 1

            page.get_by_role("button", name="Continue").click()

            #Informacoes Pessoais 
            try:
                if genero == "Masculino":
                    page.get_by_label("Male", exact=True).check()
                else:
                    page.get_by_label("Female").check()
                page.get_by_label("Marital Status*").select_option("S")
                try:
                    page.get_by_label("Primary Residence Insurance*").select_option("T")
                except:
                    pass
                if estado != "IT":
                    page.get_by_label("Has your license been valid").get_by_label("Yes").check()
                else:
                    page.get_by_label("U.S. License Type*").select_option("F")
                time.sleep(5)
            except:
                pass
            page.get_by_role("button", name="Continue").click()


            #Seguro Anterior
            try:
                if seguro == "Nunca Teve":
                    page.get_by_label("Do you have auto insurance").get_by_label("No").check()
                    page.get_by_label("Have you had auto insurance in the last 31 days?*").get_by_label("No").check()

                elif seguro == "Menos De 1 Ano":
                    page.get_by_label("Do you have auto insurance").get_by_label("Yes").check()
                    page.get_by_label("How long have you been with").select_option("A")
                    page.get_by_label("Have you been insured for the").get_by_label("Yes").check()
                elif seguro == "1-3 Anos":
                    page.get_by_label("Do you have auto insurance").get_by_label("Yes").check()
                    page.get_by_label("How long have you been with").select_option("B")
                else:
                    page.get_by_label("Do you have auto insurance").get_by_label("Yes").check()
                    page.get_by_label("How long have you been with").select_option("C")

                page.get_by_label("Do you have non-auto policies").get_by_label("No").check()
                page.get_by_label("Have you had auto insurance").get_by_label("No").check()
                time.sleep(7)
                page.get_by_role("button", name="Continue").click()
                page.get_by_label("Mobile app", exact=True).check()
                page.get_by_role("button", name="Continue").click()
                page.get_by_role("button", name="No thanks, just auto").click()
            except:
                print("Nao foi possivel encontrar alguns botoes")
                pass


            time.sleep(250)
            #---------------------#
            context.close()
            browser.close()