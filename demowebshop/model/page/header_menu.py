from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement


class HeaderMenu():
    def __init__(self, browser: WebDriver):
        self.__browser = browser

    def topcartlink(self) -> WebElement:
        return self.__browser.find_element(By.ID, 'topcartlink')

    def searchInput(self):
        return self.__browser.find_element(By.CSS_SELECTOR, 'div.search-box > form > input[type="text"]')

    def searchButton(self):
        return self.__browser.find_element(By.CSS_SELECTOR, 'div.search-box > form > input[type="submit"]')
