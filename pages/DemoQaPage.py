from BasePage import BasePage

# Se define la clase de la pagina que vamos a modelar. Esta siempre hereda de BasePage

class DemoQaPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Defino selectores especificos de la pagina
        self.fullname_input = "//input[@id='userName']"
        self.email_input = "//input[@id='userEmail']"
        self.address_text = "//textarea[@id='currentAddress']"
        self.submit_button = "//button[@id='submit']"
        self.name_p = "//p[@id='name']"
        self.email_p = "//p[@id='email']"
        self.address_p = "//p[@id='currentAddress']"

    def complete_form(self, name, email, address):
        self.fill(self.fullname_input, name)
        self.fill(self.email_input, email)
        self.fill(self.address_text, address)

    def click_submit(self):
        self.click(self.submit_button)

    def get_sent_data(self):
        sent_name = self.page.query_selector(self.name_p)
        sent_email = self.page.query_selector(self.email_p)
        sent_address = self.page.query_selector(self.address_p)
        data = []
        sent_name = sent_name.inner_text()
        data.append(sent_name)
        sent_email = sent_email.inner_text()
        data.append(sent_email)
        sent_address = sent_address.inner_text()
        data.append(sent_address)
        data = "/n".join(data)
        return data