from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement


class Product():
    __element: WebElement

    def __init__(self, element: WebElement):
        self.__element = element

    def name(self):
        return self.__element.find_element(By.CSS_SELECTOR, 'a.product-name')

    def price(self):
        return self.__element.find_element(By.CSS_SELECTOR, 'span.product-unit-price')

    def remove(self):
        return self.__element.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
