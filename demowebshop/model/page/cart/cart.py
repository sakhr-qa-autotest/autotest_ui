from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from demowebshop.model.page.wait import Wait


class Cart():
    def __init__(self, browser: WebDriver):
        self.__browser = browser

    def product_table(self):
        return self.__browser.find_elements(By.CSS_SELECTOR, 'tr.cart-item-row')

    def update_cart(self):
        return self.__browser.find_element(By.CSS_SELECTOR, 'div.common-buttons > input')

    def order_summary_content(self):
        Wait.wait(self.__browser, By.CSS_SELECTOR, 'div.order-summary-content')
        return self.__browser.find_element(By.CSS_SELECTOR, 'div.order-summary-content')
