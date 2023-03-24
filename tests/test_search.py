import allure

from model.page.header_menu import HeaderMenu
from model.page.search.search import Search


def test_successful_search(window):
    window.get("")
    headerMenu = HeaderMenu(window.driver())

    with allure.step('Успешный поиск'):
        headerMenu.searchInput().send_keys("build")
        headerMenu.searchButton().click()
        search = Search(window.driver())
        products = search.products()

        assert len(products) >= 1


def test_unsuccessful_search(window):
    window.get("")
    headerMenu = HeaderMenu(window.driver())

    with allure.step('Неудачный поиск'):
        headerMenu.searchInput().send_keys("testestest")
        headerMenu.searchButton().click()
        search = Search(window.driver())
        products = search.products()

        assert len(products) == 0
        result = search.result()
        assert result.text == 'No products were found that matched your criteria.'


def test_minimum_input_length(window):
    window.get("")
    headerMenu = HeaderMenu(window.driver())
    with allure.step('Минимальная длина строки поиска'):
        headerMenu.searchInput().send_keys("it")
        headerMenu.searchButton().click()
        search = Search(window.driver())
        warning = search.warning()
        assert warning.text == "Search term minimum length is 3 characters"
