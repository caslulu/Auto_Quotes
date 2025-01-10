import time

class Suporte:
    def progressive(self, playwright, mensagem, user, password):
        
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://account.apps.progressive.com/access/login?cntgrp=A&fd=accountHome")
        page.get_by_placeholder("User ID").fill(user)
        page.get_by_placeholder("Password").click()
        page.get_by_placeholder("Password").fill(password)
        page.get_by_role("button", name="Log In").click()
        page.wait_for_load_state("networkidle")
        page.goto("https://policyservicing.apps.progressive.com/app/account-home?brand=Progressive")
        page.get_by_role("link", name="Contact Us").click()
        page.get_by_role("link", name="Start chat").click()
        page.get_by_placeholder("Enter a message...").fill("live agent")
        page.get_by_role("button", name="Send").click()
        page.get_by_label("Start Live Chat").click()
        time.sleep(30)
        page.get_by_placeholder("Enter a message...").fill(mensagem)
        page.get_by_role("button", name="Send").click()
        time.sleep(4000)


    def geico(self, playwright, mensagem, user, password, nome):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://ecams.geico.com/login")
        page.get_by_label("User ID / Email / Policy").click()
        page.get_by_label("User ID / Email / Policy").fill(user)
        page.get_by_label("Password").click()
        page.get_by_label("Password").fill(password)
        page.get_by_role("button", name="Login").click()
        try:
            self.page.wait_for_load_state("networkidle")
        except:
            pass
        page.get_by_label("Bring up More Info Menu.").click()
        page.get_by_role("link", name="Start New Quote").click()
        time.sleep(4)
        page.locator(".gabby-g").click()
        time.sleep(5)
        page.get_by_placeholder("Type your message...").fill("live agent")
        page.keyboard.press("Enter")
        time.sleep(5)
        page.get_by_role("button", name="Policy Details or Updates").click()
        page.get_by_role("button", name="Auto").click()
        time.sleep(50)
        page.get_by_placeholder("Type your message...").fill(f"{nome}")
        page.keyboard.press("Enter")
        time.sleep(5)
        page.get_by_placeholder("Type your message...").click()
        page.get_by_placeholder("Type your message...").fill(mensagem)
        page.keyboard.press("Enter")
        time.sleep(4000)

