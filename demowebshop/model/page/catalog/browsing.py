from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Browsing:
    def __init__(self, browser: WebDriver):
        self.__browser = browser

    def products(self):
        return self.__browser.find_elements(By.CSS_SELECTOR, 'div[class=item-box]')

    def productImage(self, element: WebElement):
        return element.find_element(By.CSS_SELECTOR, 'div[class=picture] > a > img')

    def productPrice(self, element: WebElement):
        return element.find_element(By.CSS_SELECTOR, 'div[class=prices] > span')

    def productTitle(self, element: WebElement):
        return element.find_element(By.CSS_SELECTOR, 'h2[class=product-title] > a')

    def productsPagesize(self):
        return self.__browser.find_element(By.ID, 'products-pagesize')
