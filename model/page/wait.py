from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Wait():

    @staticmethod
    def wait(browser, by, selector, time=3):
        WebDriverWait(browser, time).until(
            EC.presence_of_element_located((by, selector))
        )
        WebDriverWait(browser, time).until(
            EC.visibility_of_element_located((by, selector))
        )
