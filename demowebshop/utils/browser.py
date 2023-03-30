import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from demowebshop.utils.const import CHROME
from demowebshop.utils.settings import Settings


class Browser:
    browser: WebDriver = None
    defaultUrl: str = None
    windowSize: str = "default"
    windowSizes: {} = {
        "default": [1980, 1080]
    }

    def __init__(self, settings: Settings):
        if settings.selenoid() == True:
            self.__selenoid(settings)
        elif settings.browserstack() == True:
            self.__browserstack(settings)
        else:
            if settings.browser().lower() == CHROME.lower():
                options = webdriver.ChromeOptions()

                if settings.headless() == True:
                    options.add_argument('headless')
                    options.add_argument("--no-sandbox")

                self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            else:
                options = webdriver.ChromeOptions()

                if settings.headless() == True:
                    options.add_argument('headless')
                    options.add_argument("--no-sandbox")

                self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

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

    def quit(self):
        return self.browser.quit()

    def __selenoid(self, settings: Settings) -> WebDriver:
        options = Options()
        selenoid_capabilities = {
            "browserName": settings.browser(),
            "browserVersion": settings.browserVersion(),
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        options.capabilities.update(selenoid_capabilities)
        self.browser = webdriver.Remote(
            command_executor=f"https://{settings.selenoidLogin()}:{settings.selenoidPass()}@{settings.selenoidHub()}",
            options=options
        )
        return self.browser

    def __browserstack(self, settings: Settings) -> WebDriver:
        options = Options()
        bstack_options = {
            "browserName": settings.browser(),
            "browserVersion": settings.browserVersion(),
            "os": settings.os(),
            "osVersion": settings.osVersion(),
            "buildName": "browserstack-build-1",
            "sessionName":
                datetime.datetime.now().strftime(
                    '%d-%m-%y|%H:%M:%S'
                ).__str__() + " " + settings.browser() + "_" + settings.browserVersion() + "_" + settings.os() + "_" + settings.osVersion(),
            "userName": settings.browserstackUserName(),
            "accessKey": settings.browserstackAccessKey(),
        }

        options.set_capability('bstack:options', bstack_options)
        self.browser = webdriver.Remote(
            command_executor=settings.browserstackHub(),
            options=options
        )
        return self.browser