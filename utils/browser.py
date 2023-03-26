from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    browser: WebDriver = None
    defaultUrl: str = None
    windowSize: str = "default"
    windowSizes: {} = {
        "default": [1980, 1080]
    }

    def __init__(self, browser: str = "Chrome"):
        if browser == "Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument("--no-sandbox")
            Browser.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        else:
            Browser.browser = webdriver.Chrome(ChromeDriverManager().install())

    def get(self, url: str = None):
        if url is None:
            self.browser.get(self.defaultUrl)
        elif url.find('http') >= 0 and url.find('https') >= 0:
            self.browser.get(url)
        else:
            self.browser.get(self.defaultUrl + url)

    def driver(self) -> WebDriver:
        return self.browser

    def selectWindowSize(self, size: str):
        if size not in self.windowSize:
            raise Exception("Unknown window size")
        else:
            self.windowSize = size

        self.__setWindowSize()

    def setDefaultUrl(self, defaultUrl: str):
        self.defaultUrl = defaultUrl

    def __setWindowSize(self):
        if self.windowSize in self.windowSizes:
            size = self.windowSizes[self.windowSize]
            Browser.browser.set_window_size(size[0], size[1])

    def add_cookie(self, cookie):
        self.browser.add_cookie(cookie)

    def close(self):
        self.browser.close()
