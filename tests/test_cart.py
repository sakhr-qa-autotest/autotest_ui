import allure

from model.page.cart.cart import Cart
from model.page.cart.product import Product
from model.page.header_menu import HeaderMenu


def test_adding_to_cart(window, webshop):
    webshop.webshop.post('/addproducttocart/catalog/31/1/1')
    window.get("")
    headerMenu = HeaderMenu(window.driver())

    with allure.step('Добавление товара в корзину'):
        cart = headerMenu.topcartlink()
        assert cart.text.strip('\n') != 'Shopping cart(0)'


def test_checking_cart_details(window, webshop):
    webshop.webshop.post('/addproducttocart/catalog/31/1/1')
    window.get("/cart")
    cart = Cart(window.driver())
    products = cart.productTable()

    assert len(products) >= 1

    for element in products:
        product = Product(element)
        name = product.name()
        price = product.price()
        remove = product.remove()

        assert len(name.text) >= 1
        assert len(price.text) >= 1
        assert remove.get_attribute('name') == "removefromcart"


def test_removing_item_from_the_cart(window, webshop):
    webshop.webshop.post('/addproducttocart/catalog/31/1/1')
    window.get("/cart")
    cart = Cart(window.driver())
    products = cart.productTable()

    assert len(products) >= 1
    for element in products:
        product = Product(element)
        product.remove().click()

    cart.updatecart().click()
    orderSummaryContent = cart.orderSummaryContent()

    assert orderSummaryContent.text == "Your Shopping Cart is empty!"
