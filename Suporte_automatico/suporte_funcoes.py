from playwright.sync_api import Playwright, sync_playwright, expect
from suporte import Suporte

suporte = Suporte()

def support_progressive(user, password, mensagem):
    with sync_playwright() as playwright:
            suporte.progressive(playwright, user=user, password=password, mensagem=mensagem)
