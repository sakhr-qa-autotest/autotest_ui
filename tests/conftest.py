import pytest

from utils.authorization import Authorization
from utils.browser import Browser


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="prod")


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def cookie(webshop):
    result = webshop.login('testuser123@mail.com', 'testuser123')
    webshop.authorization_cookie(result)
    return webshop.authorizationCookie


@pytest.fixture(scope='function')
def window(webshop, cookie):
    browser = Browser()
    browser.setDefaultUrl(webshop.webshop.url)
    browser.get(webshop.webshop.url)
    browser.add_cookie(cookie)
    yield browser
    browser.close()


@pytest.fixture(scope='session')
def webshop(env):
    return Authorization()
