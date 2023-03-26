import json

import utils.file


class Settings:
    __url: str
    __attachments: bool
    __browser: str
    __login: str
    __pwd: str
    __headless: bool
    __remote: bool

    __selenoid_hub: str
    __selenoid_video_hub: str
    __selenoid_login: str
    __selenoid_pass: str

    def __init__(self, env: str):
        try:
            fp = open(utils.file.abs_path_from_project(f'config.{env}.json'))
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
        except:
            raise Exception("Environment file not found")

    def url(self) -> str:
        return self.__url

    def headless(self) -> bool:
        return self.__headless

    def setHeadless(self, value: bool):
        self.__headless = value

    def remote(self) -> bool:
        return self.__remote

    def setRemote(self, value: bool):
        self.__remote = value

    def attachments(self) -> bool:
        return self.__attachments

    def setAttachments(self, value: bool):
        self.__attachments = value

    def browser(self) -> str:
        return self.__browser

    def setBrowser(self, value: str):
        self.__browser = value

    def login(self) -> str:
        return self.__login

    def pwd(self) -> str:
        return self.__pwd

    def selenoidHub(self) -> str:
        return self.__selenoid_hub

    def selenoidVideoHub(self) -> str:
        return self.__selenoid_video_hub

    def selenoidLogin(self) -> str:
        return self.__selenoid_login

    def selenoidPass(self) -> str:
        return self.__selenoid_pass
