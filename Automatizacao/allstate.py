from playwright.sync_api import sync_playwright
import time

def run(playwright, apt):
    browser = playwright.chromium.launch(
        headless=False,
        args=[
            "--disable-web-security",
            "--disable-blink-features=AutomationControlled",])
    
    context = browser.new_context()
    page = context.new_page()

    ## primeira pagina
    page.goto("https://www.allstate.com/")
    page.get_by_role("textbox", name="Enter ZIP", exact=True).fill("90802")
    page.locator("#heroBundleGetQuote").click()
    page.get_by_role("button", name="start my quote").click()
    page.get_by_label("First name").click()
    page.get_by_label("First name").fill("first")
    page.get_by_label("Last name").click()
    page.get_by_label("Last name").fill("nAME")
    page.get_by_label("Date of birth").click()
    page.get_by_label("Date of birth").fill("01/12/1990")
    page.get_by_label("Street address").click()
    page.get_by_label("Street address").fill("31 teste st")
    if apt != None:
        page.get_by_label("Apt/unit").click()
        page.get_by_label("Apt/unit").fill("teste")
    page.get_by_role("button", name="next").click()

    ## segunda pagina
    page.get_by_role("span", name="VIN").click()




    time.sleep(3000)
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright, apt=None)