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
    parser.addoption("--customDriver", default=False)


@pytest.fixture(scope='session')
def settings(request) -> Settings:
    setting = Settings(request.config.getoption("--env"))
    setting.set_browser(request.config.getoption("--browser"))
    setting.set_browser_version(request.config.getoption("--browserVersion"))
    setting.set_os(request.config.getoption("--os"))
    setting.set_os_version(request.config.getoption("--osVersion"))
    setting.set_driver(request.config.getoption("--driver"))

    if type(request.config.getoption("--headless")) != type(True):
        setting.set_headless(bool(strtobool(request.config.getoption("--headless"))))
    else:
        setting.set_headless(request.config.getoption("--headless"))

    if type(request.config.getoption("--attachments")) != type(True):
        setting.set_attachments(bool(strtobool(request.config.getoption("--attachments"))))
    else:
        setting.set_attachments(request.config.getoption("--attachments"))

    if type(request.config.getoption("--customDriver")) != type(True):
        setting.set_custom_driver(bool(strtobool(request.config.getoption("--customDriver"))))
    else:
        setting.set_custom_driver(request.config.getoption("--customDriver"))

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
                settings.set_browser(request.param['browser'])

    browser = Browser(settings)
    browser.set_default_url(webshop.webshop.url)
    browser.get(webshop.webshop.url)
    browser.add_cookie(cookie)
    yield browser
    allureAttach = AllureAttach(settings)
    allureAttach.add(browser.driver())
    browser.quit()


@pytest.fixture(scope='session')
def webshop(settings):
    return Authorization(settings)
