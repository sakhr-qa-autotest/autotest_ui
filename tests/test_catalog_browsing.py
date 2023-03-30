import allure
from selenium.webdriver.support.ui import Select

from demowebshop.model.page.catalog.browsing import Browsing


@allure.title("Проверка наличия обязательных полей")
def test_elements(window):
    window.get("/apparel-shoes")
    browsing = Browsing(window.driver())

    for product in browsing.products():
        with allure.step('Заголовок'):
            title = browsing.productTitle(product)
            assert len(title.text) >= 1
        with allure.step('Цена'):
            price = browsing.productPrice(product)
            assert len(price.text) >= 1
        with allure.step('Картинка'):
            image = browsing.productImage(product)
            assert len(image.get_attribute('src')) >= 1


@allure.title("Проверка фильтра количества объектов на экране")
def test_filter_of_quantity(window):
    window.get("/apparel-shoes")
    browsing = Browsing(window.driver())

    with allure.step('Фильтр на отображение 4 элементов'):
        pagesize = browsing.productsPagesize()
        select = Select(pagesize)
        select.select_by_visible_text("4")
        assert len(browsing.products()) == 4

    with allure.step('Фильтр на отображение 8 элементов'):
        pagesize = browsing.productsPagesize()
        select = Select(pagesize)
        select.select_by_visible_text("8")
        assert len(browsing.products()) == 8
