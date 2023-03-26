import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver

from utils.settings import Settings


class AllureAttach:
    __useAttach: bool = True

    def __init__(self, setting: Settings):
        self.__useAttach = setting.attachments()

    def image(self, driver: WebDriver):
        if self.__useAttach:
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def video(driver: WebDriver):
        pass
