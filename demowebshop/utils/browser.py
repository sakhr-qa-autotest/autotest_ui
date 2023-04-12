import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.chrome.webdriver import WebDriver as CWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from demowebshop.utils.const import CHROME, FIREFOX
from demowebshop.utils.file import abs_path_from_project
from demowebshop.utils.settings import Settings


class Browser:
    browser: CWebDriver or FWebDriver = None
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
                self.browser = self.__chrome(settings)
            elif settings.browser().lower() == FIREFOX.lower():
                self.browser = self.__firefox(settings)
            else:
                self.browser = self.__chrome(settings)

    def get(self, url: str = None):
        if url is None:
            self.browser.get(self.defaultUrl)
        elif url.find('http') >= 0 and url.find('https') >= 0:
            self.browser.get(url)
        else:
            self.browser.get(self.defaultUrl + url)

    def driver(self) -> CWebDriver or FWebDriver:
        return self.browser

    def select_window_size(self, size: str):
        if size not in self.windowSize:
            raise Exception("Unknown window size")
        else:
            self.windowSize = size

        self.__set_window_size()

    def set_default_url(self, defaultUrl: str):
        self.defaultUrl = defaultUrl

    def __set_window_size(self):
        if self.windowSize in self.windowSizes:
            size = self.windowSizes[self.windowSize]
            Browser.browser.set_window_size(size[0], size[1])

    def add_cookie(self, cookie):
        self.browser.add_cookie(cookie)

    def close(self):
        self.browser.close()

    def quit(self):
        return self.browser.quit()

    def __selenoid(self, settings: Settings) -> CWebDriver:
        default = {
            CHROME.lower(): {
                "version": "100"
            },
            FIREFOX.lower(): {
                "version": "97.0"
            }
        }
        options = COptions()
        selenoid_capabilities = {
            "browserName": settings.browser().lower(),
            "browserVersion": default[settings.browser().lower()]['version'],
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        options.capabilities.update(selenoid_capabilities)
        self.browser = webdriver.Remote(
            command_executor=f"https://{settings.selenoid_login()}:{settings.selenoid_pass()}@{settings.selenoid_hub()}/wd/hub",
            options=options
        )
        return self.browser

    def __browserstack(self, settings: Settings) -> CWebDriver:
        options = COptions()
        bstack_options = {
            "browserName": settings.browser(),
            "browserVersion": settings.browser_version(),
            "os": settings.os(),
            "osVersion": settings.os_version(),
            "buildName": "browserstack-build-1",
            "sessionName":
                datetime.datetime.now().strftime(
                    '%d-%m-%y|%H:%M:%S'
                ).__str__() + " " + settings.browser() + "_" + settings.browser_version() + "_" + settings.os() + "_" + settings.os_version(),
            "userName": settings.browserstack_username(),
            "accessKey": settings.browserstack_access_key(),
        }

        options.set_capability('bstack:options', bstack_options)
        self.browser = webdriver.Remote(
            command_executor=settings.browserstack_hub(),
            options=options
        )
        return self.browser

    def __chrome(self, settings: Settings) -> webdriver:
        options = webdriver.ChromeOptions()

        if settings.headless() == True:
            options.add_argument('headless')
            options.add_argument("--no-sandbox")

        if settings.custom_driver() == True:
            return webdriver.Chrome(
                abs_path_from_project('../drivers/chromedriver_111_0_5563_19'),
                options=options
            )

        return webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def __firefox(self, settings: Settings) -> webdriver:
        options = webdriver.FirefoxOptions()

        if settings.headless() == True:
            options.add_argument('headless')
            options.add_argument("--no-sandbox")

        return webdriver.Firefox(
            executable_path=GeckoDriverManager().install(),
            options=options,
        )
