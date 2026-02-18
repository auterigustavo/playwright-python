from playwright.sync_api import expect

# Modelado basico para utilizar en todas las paginas. Define metodos generales para trabajar en cualquier web

class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, selector):
        self.page.locator(selector).click()

    def fill(self, selector, text):
        self.page.locator(selector).fill(text)
    
    def wait_for_element(self, selector):
        self.page.locator(selector).wait_for(state="visible")