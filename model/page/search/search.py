from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Search():
    def __init__(self, browser: WebDriver):
        self.__browser = browser

    def products(self):
        return self.__browser.find_elements(By.CLASS_NAME, 'item-box')

    def result(self):
        return self.__browser.find_element(By.CSS_SELECTOR, 'strong[class="result"]')
