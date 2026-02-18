from playwright.sync_api import sync_playwright, expect
from behave import Given, When, Then, Step
from pages.DemoQaPage import DemoQaPage

website = None

@Given("Ingreso a la pagina {url}")
def run(context, url):
    context.page = context.browser_context.new_page()
    context.page.goto(url)
    context.website = DemoQaPage(context.page)


@When("Lleno los campos presentados")
def fill_text_forms(context):
    name = "Gustavo Auteri"
    email = "gauteri@mail.com"
    address = "Hola Mundo"
    context.website.complete_form(name, email, address)
    

@Step("Hago click en submit")
def send_form(context):
    context.website.click_submit()

@Then("Verifico que el mail {email} coincida")
def verify_sent_data(context, email):
    context.website.validate_sent_data(email)