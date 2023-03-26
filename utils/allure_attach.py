import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver

from utils.settings import Settings


class AllureAttach:
    __setting: Settings

    def __init__(self, setting: Settings):
        self.__setting = setting

    def add(self, driver: WebDriver):
        self.__image(driver)
        self.__selenoidVideo(driver)

    def __image(self, driver: WebDriver):
        if self.__setting.attachments():
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def __selenoidVideo(self, driver: WebDriver):
        if self.__setting.attachments() and self.__setting.remote():
            video_url = self.__setting.selenoidVideoHub() + driver.session_id + ".mp4"
            html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
                   + video_url \
                   + "' type='video/mp4'></video></body></html>"
            allure.attach(html, 'video_' + driver.session_id, AttachmentType.HTML, '.html')
