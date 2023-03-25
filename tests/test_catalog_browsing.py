import allure
from selenium.webdriver.support.ui import Select

from model.page.catalog.browsing import Browsing


def test_elements(window):
    window.get("/apparel-shoes")
    browsing = Browsing(window.driver())

    with allure.step('Проверка наличия обязательных полей'):
        for product in browsing.products():
            title = browsing.productTitle(product)
            assert len(title.text) >= 1
            price = browsing.productPrice(product)
            assert len(price.text) >= 1
            image = browsing.productImage(product)
            assert len(image.get_attribute('src')) >= 1


def test_filter_of_quantity(window):
    window.get("/apparel-shoes")
    browsing = Browsing(window.driver())

    with allure.step('Проверка фильтра количества объектов на экране'):
        pagesize = browsing.productsPagesize()
        select = Select(pagesize)
        select.select_by_visible_text("4")
        assert len(browsing.products()) == 4

        pagesize = browsing.productsPagesize()
        select = Select(pagesize)
        select.select_by_visible_text("8")
        assert len(browsing.products()) == 8
