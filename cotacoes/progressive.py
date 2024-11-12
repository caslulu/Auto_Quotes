import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def get_quote_progressive(playwright: Playwright, zipcode, first_name, last_name, date_birth, address, vin, email, financiado):
    """"Utilizei playwright para fazer o codigo
    nao tenho ideia de como funcione, mas esta funcionando."""
    # tentar mudar para selenium.


    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.progressive.com/")
    page.get_by_role("link", name="Or, see all 30+ products").click()
    page.get_by_role("option", name="Auto", exact=True).click()
    page.get_by_role("textbox", name="Enter ZIP Code").fill(zipcode)
    page.get_by_role("button", name="Get a quote").click()
    try:
        page.wait_for_load_state("networkidle")
    except:
        pass
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

    page.wait_for_load_state("load")
    page.get_by_label("Street number and name").click()
    page.get_by_label("Street number and name").fill(address)
    time.sleep(10)

    page.get_by_role("button", name="Ok, start my quote").click()
    page.get_by_role("link", name="Enter by VIN").click()
    page.get_by_label("Vehicle Identification Number").fill(vin)
    page.get_by_label("Learn more aboutVehicle Use*").select_option("1")
    if financiado == "Financiado":
        page.get_by_label("Own or lease?").select_option("2")
    else:
        page.get_by_label("Own or lease?").select_option("3")
    time.sleep(270)
    # ---------------------
    context.close()
    browser.close()
