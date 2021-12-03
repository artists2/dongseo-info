import requests
from pydantic import BaseModel
from bs4 import BeautifulSoup as bs


class Parsing:
    page: str

    def __init__(self, _page):
        page: str = _page


class Schedule(Parsing):
    # page: str

    def schedule_parser(self):
        return self.page


class Notice(Parsing):
    def academic(self):  # 학사
        pass

    def recruit(self):  # 모집
        pass

    def notices(self):  # 공지
        pass

    def event(self):  # 행사
        pass

    def scholarship(self):  # 장학
        pass






