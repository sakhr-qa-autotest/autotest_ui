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
