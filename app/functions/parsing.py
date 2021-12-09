import requests
from pydantic import BaseModel
import re
from bs4 import BeautifulSoup as bs
from abc import *
# self.page = page
# self.soup = bs(self.page.text, 'html.parser')


class BaseParser(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def parse(page: str):
        pass


class BaseImportantNoticesParser(BaseParser, metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def parse(page: str) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def is_important(page: str) -> bool:
        pass


class ImportantNoticesParser(BaseImportantNoticesParser):
    @staticmethod
    def parse(page: str) -> dict:
        soup = bs(page, "html.parser")
        if not ImportantNoticesParser.is_important(page):
            print("주요 공지가 없습니다.")  # print 말고 다른거로 수정해야함
            return {}
        elements = soup.findAll("tr", {"class": "isnotice"})
        element = []
        for i in range(0, len(elements)):
            e = list()
            e.append(elements[i].find("a").find("span").text)
            e.append(elements[i].find("td", {"class": "f-date date"}).text)
            e.append('https://www.dongseo.ac.kr' + elements[i].find("a")["href"])
            element.append(e)
            print(e)
        print(element[0])
        return {
            "title": "",
            "date": "",
            "url": ""
        }

    @staticmethod
    def is_important(page: str) -> bool:
        soup = bs(page, "html.parser")
        if soup.findAll("tr", {"class": "isnotice"}):
            return True
        else:
            return False


class NoticesParser(BaseParser):  #
    @staticmethod
    def parse(page: str):
        soup = bs(page, "html.parser")
        elements = soup.findAll("tr", {"class": re.compile('child_1|child_2')})
        element = []
        for i in range(0, len(elements)):
            e = list()
            e.append(elements[i].find("a").find("span").text)
            e.append(elements[i].find("td", {"class": "f-date date"}).text)
            e.append('https://www.dongseo.ac.kr' + elements[i].find("a")["href"])
            element.append(e)
            print(e)
        print(element[0])

        return {}


class ScheduleParser(BaseParser):  # ScheduleParser.parse(page)
    @staticmethod
    def parse(page: str) -> dict:
        soup = bs(page, "html.parser")
        elements_day = soup.findAll("div", {"class": "date-core"})  # day
        elements_schedule = soup.findAll("div", {"class": "body-core"})  # schedule

        _day = [''.join(e.text.split()) for e in elements_day]
        _schedule = [''.join(s.text.split()) for s in elements_schedule]

        for i in range(0, len(_day)):  # test code
            print(_day[i], _schedule[i])
        return {
            "date": "",
            "schedule": ""
        }