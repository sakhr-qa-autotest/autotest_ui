from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Compare():
    def __init__(self, browser: WebDriver):
        self.__browser = browser

    def price(self):
        return self.__browser.find_elements(By.CSS_SELECTOR, 'tr[class=product-price] > td')

    def name(self):
        return self.__browser.find_elements(By.CSS_SELECTOR, 'tr[class=product-name]  > td')
