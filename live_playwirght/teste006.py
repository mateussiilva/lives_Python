
from playwright.sync_api import sync_playwright
from time import sleep


url = "https://selenium.dunossauro.live/aula_05_a.html"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    
    page = browser.new_page(
        base_url="https://selenium.dunossauro.live/"
    )
    
    page.goto("aula_05_a.html") # NAVEGA ATÉ A PAGINA
    locator_div = page.locator("div").nth(0)
    print(locator_div.text_content())
    browser.close()
