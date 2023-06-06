
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chroumin.lauch()


    browser.close()
