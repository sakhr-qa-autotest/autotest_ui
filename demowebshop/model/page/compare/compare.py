from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Compare():
    def __init__(self, browser: WebDriver):
        self.__browser = browser

    def price(self):
        return self.__browser.find_elements(By.CSS_SELECTOR, 'tr[class=product-price] > td')

    def name(self):
        return self.__browser.find_elements(By.CSS_SELECTOR, 'tr[class=product-name]  > td')

    def clear(self):
        return self.__browser.find_element(By.CSS_SELECTOR, 'a[class=clear-list]')

    def pageBody(self):
        return self.__browser.find_element(By.CSS_SELECTOR, 'div[class=page-body]')

    def products(self):
        return self.__browser.find_elements(By.CSS_SELECTOR, 'tr[class=overview] > td[class=a-center]')

    def productRemoveBuutton(self, element: WebElement):
        return element.find_element(By.CSS_SELECTOR, 'input[class="button-2 remove-button"]')
