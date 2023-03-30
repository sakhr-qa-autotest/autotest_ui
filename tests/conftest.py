from distutils.util import strtobool

import pytest

from demowebshop.utils.allure_attach import AllureAttach
from demowebshop.utils.authorization import Authorization
from demowebshop.utils.browser import Browser
from demowebshop.utils.settings import Settings


def pytest_addoption(parser):
    parser.addoption("--env", default="test")
    parser.addoption("--attachments", default=True)
    parser.addoption("--driver", default="local")  # selenoid #browserstack #local
    parser.addoption("--browser", default="Chrome")
    parser.addoption("--browserVersion", default="103.0")
    parser.addoption("--os", default="Windows")
    parser.addoption("--osVersion", default="11")
    parser.addoption("--headless", default=False)


@pytest.fixture(scope='session')
def settings(request) -> Settings:
    setting = Settings(request.config.getoption("--env"))
    setting.setBrowser(request.config.getoption("--browser"))
    setting.setBrowserVersion(request.config.getoption("--browserVersion"))
    setting.setOs(request.config.getoption("--os"))
    setting.setOsVersion(request.config.getoption("--osVersion"))
    setting.setDriver(request.config.getoption("--driver"))

    if type(request.config.getoption("--headless")) != type(True):
        setting.setHeadless(bool(strtobool(request.config.getoption("--headless"))))
    else:
        setting.setHeadless(request.config.getoption("--headless"))

    if type(request.config.getoption("--attachments")) != type(True):
        setting.setAttachments(bool(strtobool(request.config.getoption("--attachments"))))
    else:
        setting.setAttachments(request.config.getoption("--attachments"))

    return setting


@pytest.fixture(scope='session')
def cookie(webshop, settings: Settings):
    result = webshop.login(settings.login(), settings.pwd())
    webshop.authorization_cookie(result)
    return webshop.authorizationCookie


@pytest.fixture(scope='function')
def window(webshop, cookie, settings, request):
    if hasattr(request, 'param'):
        if type(request.param) == type({}):
            if 'browser' in request.param:
                settings.setBrowser(request.param['browser'])

    browser = Browser(settings)
    browser.setDefaultUrl(webshop.webshop.url)
    browser.get(webshop.webshop.url)
    browser.add_cookie(cookie)
    yield browser
    allureAttach = AllureAttach(settings)
    allureAttach.add(browser.driver())
    browser.quit()


@pytest.fixture(scope='session')
def webshop(settings):
    return Authorization(settings)
