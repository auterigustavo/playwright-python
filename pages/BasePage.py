from playwright.sync_api import expect
from datetime import datetime

class BasePage:
    def __init__(self, context):
        self.context = context
        self.searchField = "//input[starts-with(@id, 'downshift-') and contains(@id, '-input')]"
        self.cookiesButton = "//button[@id='onetrust-accept-btn-handler']"
        self.productItem = "//span[contains(text(),'$')]"
        self.priceItem = "//span[@class='valtech-carrefourar-product-price-0-x-currencyFraction']/.."
        self.productDescription = "//div/h1/span/../../../../.."

    def acceptCookies(self):
        self.context.page.click(self.cookiesButton)

    def clickSearchField(self):
        self.context.page.click(self.searchField)

    def searchProduct(self, text):
        self.context.page.fill(self.searchField,text)
        self.context.page.keyboard.press('Enter')

    def closePopUp(self):
        self.context.page.evaluate("document.elementFromPoint(150, 30).click()")

    def selectFirstProduct(self):
        self.context.page.click(self.productItem)

    def getProductDescription(self):
        product_description = self.context.page.query_selector(self.productDescription)
        description = product_description.inner_text()
        return description

    def getProductPrice(self):
        price_element = self.context.page.query_selector(self.priceItem)
        price = price_element.inner_text()
        return price
    
    def createReport(self, l1, l2):
        extention = ".txt"
        date = datetime.now()
        date = str(date).replace(":", "")
        date = str(date).replace(".", "")
        date = str(date).replace(" ", "")
        archive_name = str(date)+extention
        report = open('reports/'+archive_name, 'x')
        for prod,pre in zip(l1,l2):
            report.write(prod + ": " + pre + '\n')