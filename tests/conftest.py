from distutils.util import strtobool

import pytest

from utils.allure_attach import AllureAttach
from utils.authorization import Authorization
from utils.browser import Browser
from utils.settings import Settings


def pytest_addoption(parser):
    parser.addoption("--env", default="test")
    parser.addoption("--attachments", default=True)
    parser.addoption("--browser", default="Chrome")
    parser.addoption("--headless", default=True)


@pytest.fixture(scope='session')
def settings(request) -> Settings:
    setting = Settings(request.config.getoption("--env"))
    setting.setAttachments(bool(strtobool(request.config.getoption("--attachments"))))
    setting.setBrowser(request.config.getoption("--browser"))
    setting.setHeadless(bool(strtobool(request.config.getoption("--headless"))))
    return setting


@pytest.fixture(scope='session')
def cookie(webshop, settings: Settings):
    result = webshop.login(settings.login(), settings.pwd())
    webshop.authorization_cookie(result)
    return webshop.authorizationCookie


@pytest.fixture(scope='function')
def window(webshop, cookie, settings):
    browser = Browser(settings)
    browser.setDefaultUrl(webshop.webshop.url)
    browser.get(webshop.webshop.url)
    browser.add_cookie(cookie)
    yield browser
    allureAttach = AllureAttach(settings)
    allureAttach.image(browser.driver())
    browser.close()


@pytest.fixture(scope='session')
def webshop(settings):
    return Authorization(settings)
