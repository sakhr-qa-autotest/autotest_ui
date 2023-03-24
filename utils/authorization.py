from utils.base_session import BaseSession


class Authorization:
    authorizationCookie = None

    def __init__(self):
        self.webshop = BaseSession(url="https://demowebshop.tricentis.com")
        self.authorizationCookie = None

    def login(self, email, password):
        return self.webshop.post(
            url="/login",
            params={'Email': email, 'Password': password},
            headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
            allow_redirects=False
        )

    def authorization_cookie(self, response):
        self.authorizationCookie = {"name": "NOPCOMMERCE.AUTH", "value": response.cookies.get("NOPCOMMERCE.AUTH")}
