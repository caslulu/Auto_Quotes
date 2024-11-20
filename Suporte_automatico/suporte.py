import time


from playwright.sync_api import Playwright, sync_playwright, expect



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
        time.sleep(600)

        # ---------------------
        context.close()
        browser.close()