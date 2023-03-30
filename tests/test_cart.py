import allure
import pytest

from demowebshop.model.page.cart.cart import Cart
from demowebshop.model.page.cart.product import Product
from demowebshop.model.page.header_menu import HeaderMenu
from demowebshop.utils.const import CHROME, FIREFOX


@allure.title("Состояние корзины в заголовке")
@pytest.mark.parametrize('window', [
    {
        'browser': CHROME
    },
    {
        'browser': FIREFOX
    }
], indirect=True)
def test_adding_to_cart(window, webshop):
    webshop.webshop.post('/addproducttocart/catalog/31/1/1')
    window.get("")
    headerMenu = HeaderMenu(window.driver())

    with allure.step('Состояние с не пустой корзиной'):
        cart = headerMenu.topcartlink()
        assert cart.text.strip('\n') != 'Shopping cart(0)'


@allure.title("Проверка обязательных полей в корзине")
@pytest.mark.parametrize('window', [
    {
        'browser': CHROME
    },
    {
        'browser': FIREFOX
    }
], indirect=True)
def test_checking_cart_details(window, webshop):
    webshop.webshop.post('/addproducttocart/catalog/31/1/1')
    window.get("/cart")
    cart = Cart(window.driver())
    products = cart.productTable()

    assert len(products) >= 1

    for element in products:
        product = Product(element)

        with allure.step('Название'):
            name = product.name()
            assert len(name.text) >= 1

        with allure.step('Цена'):
            price = product.price()
            assert len(price.text) >= 1

        with allure.step('Кнопка удалить из корзины'):
            remove = product.remove()
            assert remove.get_attribute('name') == "removefromcart"


@allure.title("Удаление элемента из корзины")
@pytest.mark.parametrize('window', [
    {
        'browser': CHROME
    },
    {
        'browser': FIREFOX
    }
], indirect=True)
def test_removing_item_from_the_cart(window, webshop):
    webshop.webshop.post('/addproducttocart/catalog/31/1/1')
    window.get("/cart")
    cart = Cart(window.driver())
    products = cart.productTable()

    assert len(products) >= 1
    for element in products:
        product = Product(element)
        with allure.step('Удаление ' + product.name().text):
            product.remove().click()

    cart.updatecart().click()
    orderSummaryContent = cart.orderSummaryContent()

    assert orderSummaryContent.text == "Your Shopping Cart is empty!"
