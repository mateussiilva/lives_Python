
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        color_scheme="dark",
        record_video_dir="."
    )
    page= context.new_page()  
    page.goto("https://web.whatsapp.com/")
    print(page.title())
    
    browser.close()