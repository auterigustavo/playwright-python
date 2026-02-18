from pages.BasePage import BasePage
from playwright.sync_api import expect

# Se define la clase de la pagina que vamos a modelar. Esta siempre hereda de BasePage

class DemoQaPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Defino selectores especificos de la pagina
        self.fullname_input = "//input[@id='userName']"
        self.email_input = "//input[@id='userEmail']"
        self.address_text = "//textarea[@id='currentAddress']"
        self.submit_button = "//button[@id='submit']"
        self.email_p = "//p[@id='email']"
        self.elements_a = "//a[@href='/elements']"
        self.text_box_a = "//*[contains(text(), 'Text Box')]"

    def complete_form(self, name, email, address):
        self.click(self.elements_a)
        self.click(self.text_box_a)
        self.fill(self.fullname_input, name)
        self.fill(self.email_input, email)
        self.fill(self.address_text, address)

    def click_submit(self):
        self.click(self.submit_button)

    def validate_sent_data(self, email):
        locator = self.page.locator(self.email_p)
        expect(locator).to_contain_text(email)