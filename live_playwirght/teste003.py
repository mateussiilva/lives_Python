from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()  
    
    page.goto("https://web.whatsapp.com/")
    sleep(3)
    page.goto("https://google.com.br")
    sleep(3)
    page.go_back()
    print(page.title())
    sleep(3)
    browser.close()