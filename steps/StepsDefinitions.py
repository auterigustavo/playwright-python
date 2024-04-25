from playwright.sync_api import sync_playwright, expect
from behave import Given, When, Then, Step
from pages.BasePage import BasePage
import time

website = None
listaProductos = []
listaPrecios = []

@Given("Ingreso a la pagina {url}")
def run(context, url):
    # Inicia Playwright y guarda los objetos relevantes en el contexto para su uso posterior
    playwright = sync_playwright().start()
    context.browser = playwright.chromium.launch(headless=False)
    
    # Crea un contexto de navegador y comienza el trazado
    context.browser_context = context.browser.new_context()
    context.browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    # Crea una nueva página en este contexto
    context.page = context.browser_context.new_page()
    context.page.goto(url)
    global website
    website = BasePage(context)
    website.acceptCookies()

@When("Busco el producto {producto} y obtengo el precio")
def searchItem(context, producto):
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
def generateReport(context):
    website.createReport(listaProductos, listaPrecios)

@Then("Guardo el trace en la carpeta logs")
def save_trace(context):
    context.browser_context.tracing.stop(path='logs/trace.zip')

