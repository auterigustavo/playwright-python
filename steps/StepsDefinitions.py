from playwright.sync_api import sync_playwright, expect
from behave import Given, When, Then, Step
from pages.BasePage import BasePage
from mailing.smtp_service import send_mail_to_address
import time

website = None
listaProductos = []
listaPrecios = []

@Given("Ingreso a la pagina {url}")
def run(context, url):
    context.page = context.browser_context.new_page()
    context.page.goto(url)
    global website
    website = BasePage(context)
    website.acceptCookies()


@When("Busco los siguientes productos y obtengo los precios")
def searchProducts(context):
    #Recorro la lista de productos detallada en el feature file
    for row in context.table:
        producto = row["Producto"]
        website.clickSearchField()
        website.searchProduct(producto)
        time.sleep(3)
        website.closePopUp()
        time.sleep(2)
        website.selectFirstProduct()
        listaProductos.append(producto)
        precio = website.getProductPrice()
        listaPrecios.append(str(precio))
        time.sleep(1)

@Step("Genero un reporte con los datos")
def genero_un_reporte_con_los_datos(context):
    website.createReport(listaProductos, listaPrecios)

@Then("Envio un reporte por mail")
def envio_un_reporte_al_mail(context):
    send_mail_to_address("auterigustavo@gmail.com")