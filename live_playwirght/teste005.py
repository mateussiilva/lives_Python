
from playwright.sync_api import sync_playwright
from time import sleep

def event_handler(request_event):
    response = request_event.response()
    print(f"{request_event.url} - {response.status}")
    
def print_console_message(request_event):
    print(request_event)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={"width":400,"height":500}
    )
    page = context.new_page()
    
    #       "EVENTO",  CALLBACK   
    page.on("request",event_handler)
    page.on("console",print_console_message)
    page.goto("https://ddg.gg")
    sleep(30)
    browser.close()
