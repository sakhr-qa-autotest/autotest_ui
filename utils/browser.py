from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from utils.settings import Settings


class Browser:
    browser: WebDriver = None
    defaultUrl: str = None
    windowSize: str = "default"
    windowSizes: {} = {
        "default": [1980, 1080]
    }

    def __init__(self, settings: Settings):
        if settings.remote() == True:
            options = Options()
            selenoid_capabilities = {
                "browserName": "chrome",
                "browserVersion": "100.0",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True
                }
            }

            options.capabilities.update(selenoid_capabilities)
            Browser.browser = webdriver.Remote(
                command_executor=f"https://{settings.selenoidLogin()}:{settings.selenoidPass()}@{settings.selenoidHub()}",
                options=options
            )
        else:
            if settings.browser() == "Chrome":
                options = webdriver.ChromeOptions()

                if settings.headless() == False:
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
