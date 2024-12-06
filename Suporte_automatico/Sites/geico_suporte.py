import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ecams.geico.com/login")
    page.get_by_label("User ID / Email / Policy").click()
    page.get_by_label("User ID / Email / Policy").fill("BrenoSantos01")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Carteira123@")
    page.get_by_role("button", name="Login").click()
    page.goto("https://portfolio.geico.com/dashboard")
    page.get_by_role("link", name="Menu", exact=True).click()
    page.get_by_role("link", name="Contact Us").click()
    page.get_by_label("Please choose the policy that").select_option("6175850434")
    page.get_by_role("button", name="Go").click()
    page.get_by_placeholder("Type your message...").click()
    page.get_by_placeholder("Type your message...").fill("live agent")
    page.get_by_role("button", name="Policy Details or Updates").click()
    page.get_by_role("button", name="Auto").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
