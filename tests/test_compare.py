import allure
import pytest

from demowebshop.model.page.compare.compare import Compare


@allure.title("Таблица сравнений товаров")
def test_comparison_table(window, webshop):
    window.get("/compareproducts/add/31")
    window.get("/compareproducts/add/16")

    compare = Compare(window.driver())
    with allure.step('Цена'):
        prices = compare.price()
        assert len(prices) >= 3

    with allure.step('Название'):
        names = compare.name()
        assert len(names) >= 3


@allure.title("Проверка кнопки очистить таблицу сравнений")
@pytest.mark.skip(reason="Пропускаем, фича на доработки")
def test_clear(window, webshop):
    window.get("/compareproducts/add/31")
    window.get("/compareproducts/add/16")

    with allure.step('Нажимаем на кнопку'):
        compare = Compare(window.driver())
        compare.clear().click()
        assert compare.page_body().text == 'You have no items to compare.'


@allure.title("Удааление по отдельности каждый элемент в корзине")
def test_deleting_elements(window, webshop):
    window.get("/compareproducts/add/31")
    window.get("/compareproducts/add/16")

    compare = Compare(window.driver())

    while True:
        products = compare.products()
        if len(products) == 0:
            break
        with allure.step('Удаление одного из элементов'):
            compare.product_remove_buutton(products[0]).click()

    assert compare.page_body().text == 'You have no items to compare.'
