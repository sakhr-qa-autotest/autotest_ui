import json

from demowebshop.utils.const import SELENOID, BROWSERSTACK, LOCAL
from demowebshop.utils.file import abs_path_from_project


class Settings:
    __url: str
    __attachments: bool
    __browser: str
    __browser_version: str
    __login: str
    __pwd: str
    __headless: bool = False
    __selenoid: bool = False
    __browserstack: bool = False
    __local: bool = False

    __custom_driver: bool = False

    __os: str
    __osVersion: str

    __selenoid_hub: str
    __selenoid_video_hub: str
    __selenoid_login: str
    __selenoid_pass: str

    __browserstack_hub: str
    __browserstack_video_hub: str
    __browserstack_user_name: str
    __browserstack_access_key: str

    __driver: str

    def __init__(self, env: str):
        try:
            fp = open(abs_path_from_project(f'../config.{env}.json'))
            config = json.loads(fp.read())

            if 'url' in config:
                self.__url = config['url']
            if 'login' in config:
                self.__login = config['login']
            if 'pwd' in config:
                self.__pwd = config['pwd']

            if 'selenoid_hub' in config:
                self.__selenoid_hub = config['selenoid_hub']
            if 'selenoid_video_hub' in config:
                self.__selenoid_video_hub = config['selenoid_video_hub']
            if 'selenoid_login' in config:
                self.__selenoid_login = config['selenoid_login']
            if 'selenoid_pass' in config:
                self.__selenoid_pass = config['selenoid_pass']

            if 'browserstack_hub' in config:
                self.__browserstack_hub = config['browserstack_hub']
            if 'browserstack_video_hub' in config:
                self.__browserstack_video_hub = config['browserstack_video_hub']
            if 'browserstack_user_name' in config:
                self.__browserstack_user_name = config['browserstack_user_name']
            if 'browserstack_access_key' in config:
                self.__browserstack_access_key = config['browserstack_access_key']
        except:
            raise Exception("Environment file not found")

    def set_custom_driver(self, value=False):
        self.__custom_driver = value

    def custom_driver(self) -> bool:
        return self.__custom_driver

    def set_driver(self, driver: str):
        if BROWSERSTACK.lower() == driver.lower():
            self.__browserstack = True
        elif SELENOID.lower() == driver.lower():
            self.__selenoid = True
        elif LOCAL.lower() == driver.lower():
            self.__local = True

        self.__driver = driver

    def driver(self) -> str:
        return self.__driver

    def local(self) -> bool:
        return self.__local

    def url(self) -> str:
        return self.__url

    def headless(self) -> bool:
        return self.__headless

    def set_headless(self, value: bool):
        self.__headless = value

    def browserstack(self) -> bool:
        return self.__browserstack

    def set_browserstack(self, value: bool):
        self.__browserstack = value

    def selenoid(self) -> bool:
        return self.__selenoid

    def set_selenoid(self, value: bool):
        self.__selenoid = value

    def attachments(self) -> bool:
        return self.__attachments

    def set_attachments(self, value: bool):
        self.__attachments = value

    def browser(self) -> str:
        return self.__browser

    def browser_version(self) -> str:
        return self.__browser_version

    def set_os_version(self, value: str):
        self.__osVersion = value

    def os_version(self) -> str:
        return self.__osVersion

    def set_os(self, value: str):
        self.__os = value

    def os(self) -> str:
        return self.__os

    def set_browser(self, value: str):
        self.__browser = value

    def set_browser_version(self, value: str):
        self.__browser_version = value

    def login(self) -> str:
        return self.__login

    def pwd(self) -> str:
        return self.__pwd

    def selenoid_hub(self) -> str:
        return self.__selenoid_hub

    def selenoid_video_hub(self) -> str:
        return self.__selenoid_video_hub

    def selenoid_login(self) -> str:
        return self.__selenoid_login

    def selenoid_pass(self) -> str:
        return self.__selenoid_pass

    def browserstack_hub(self) -> str:
        return self.__browserstack_hub

    def browserstack_video_hub(self) -> str:
        return self.__browserstack_video_hub

    def browserstack_username(self) -> str:
        return self.__browserstack_user_name

    def browserstack_access_key(self) -> str:
        return self.__browserstack_access_key
