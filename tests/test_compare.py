import allure

from model.page.compare.compare import Compare


def test_comparison_table(window, webshop):
    window.get("/compareproducts/add/31")
    window.get("/compareproducts/add/16")

    with allure.step('Таблица сравнений'):
        compare = Compare(window.driver())
        prices = compare.price()
        names = compare.name()

        assert len(prices) >= 3
        assert len(names) >= 3


def test_clear(window, webshop):
    window.get("/compareproducts/add/31")
    window.get("/compareproducts/add/16")

    with allure.step('Проверка кнопки очистить таблицу сравнений'):
        compare = Compare(window.driver())
        compare.clear().click()
        assert compare.pageBody().text == 'You have no items to compare.'


def test_deleting_elements(window, webshop):
    window.get("/compareproducts/add/31")
    window.get("/compareproducts/add/16")

    with allure.step('Удааление по отдельности каждый элемент в корзине'):
        compare = Compare(window.driver())

        while True:
            products = compare.products()
            if len(products) == 0:
                break

            compare.productRemoveBuutton(products[0]).click()

        assert compare.pageBody().text == 'You have no items to compare.'
