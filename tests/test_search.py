import allure

from demowebshop.model.page.header_menu import HeaderMenu
from demowebshop.model.page.search.search import Search


@allure.title("Успешный поиск")
def test_successful_search(window):
    window.get("")
    headerMenu = HeaderMenu(window.driver())

    with allure.step('Поиск по фразе build'):
        headerMenu.search_input().send_keys("build")
        headerMenu.search_button().click()
        search = Search(window.driver())
        products = search.products()

        assert len(products) >= 1


@allure.title("Неудачный поиск")
def test_unsuccessful_search(window):
    window.get("")
    headerMenu = HeaderMenu(window.driver())

    with allure.step('Поиск по фразе testestest'):
        headerMenu.search_input().send_keys("testestest")
        headerMenu.search_button().click()
        search = Search(window.driver())
        products = search.products()

        assert len(products) == 0
        result = search.result()
        assert result.text == 'No products were found that matched your criteria.'


@allure.title("Минимальная длина строки поиска")
def test_minimum_input_length(window):
    window.get("")
    headerMenu = HeaderMenu(window.driver())
    with allure.step('Вводим 2 текстовых символа'):
        headerMenu.search_input().send_keys("it")
        headerMenu.search_button().click()
        search = Search(window.driver())
        warning = search.warning()
        assert warning.text == "Search term minimum length is 3 characters"
