import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def get_quote(playwright: Playwright, zipcode, first_name, last_name, date_birth, address, vin, email):
    """"Utilizei playwright para fazer o codigo
    nao tenho ideia de como funcione, mas esta funcionando."""
    # tentar mudar para selenium.


    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.progressive.com/")
    page.get_by_role("link", name="Popular Auto Average savings").click()
    page.get_by_role("textbox", name="Enter ZIP Code").fill(zipcode)
    page.get_by_role("button", name="Get a quote").click()
    page.wait_for_load_state("networkidle")

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
    time.sleep(15)

    page.get_by_role("button", name="Ok, start my quote").click()
    page.get_by_role("link", name="Enter by VIN").click()
    page.get_by_label("Vehicle Identification Number").fill(vin)
    page.get_by_label("Learn more aboutVehicle Use*").select_option("1")