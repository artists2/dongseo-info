import requests
from pydantic import BaseModel
import re
from bs4 import BeautifulSoup as bs
from abc import *
# from databases.crud import create_notices
from typing import List, Dict


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
    def is_important(page: str) -> bool:
        soup = bs(page, "html.parser")
        if soup.findAll("tr", {"class": "isnotice"}):
            return True
        else:
            return False


def parse(page: str) -> List[Dict]:
    soup = bs(page, "html.parser")
    if not ImportantNoticesParser.is_important(page):
        print("주요 공지가 없습니다.")  # print 말고 다른거로 수정해야함
        return {}
    elements = soup.findAll("tr", {"class": "isnotice"})
    element: List[Dict] = list()
    for i in range(0, len(elements)):
        e = dict()
        e["title"] = elements[i].find("a").find("span").text
        e["date"] = elements[i].find("td", {"class": "f-date date"}).text
        e["link"] = 'https://www.dongseo.ac.kr' + elements[i].find("a")["href"]
        element.append(e)
    return element


class NoticesParser(BaseParser):  #
    @staticmethod
    def parse(page: str) -> List[dict]:
        soup = bs(page, "html.parser")
        elements = soup.findAll("tr", {"class": re.compile('child_1|child_2')})
        element: List[Dict] = list()
        for i in range(0, len(elements)):
            e = dict()
            e["title"] = elements[i].find("a").find("span").text
            e["date"] = elements[i].find("td", {"class": "f-date date"}).text
            e["link"] = 'https://www.dongseo.ac.kr' + elements[i].find("a")["href"]
            element.append(e)

        return element


class ScheduleParser(BaseParser):  # ScheduleParser.parse(page)
    @staticmethod
    def parse(page: str) -> List[dict]:
        soup = bs(page, "html.parser")
        elements_day = soup.findAll("div", {"class": "date-core"})  # day
        elements_schedule = soup.findAll("div", {"class": "body-core"})  # schedule

        day = [''.join(e.text.split()) for e in elements_day]
        schedule = [''.join(s.text.split()) for s in elements_schedule]
        element: List[dict] = list()
        for i in range(0, len(day)):  # test code
            e = dict()
            e["date"] = day[i]
            e["title"] = schedule[i]
            element.append(e)
        print(element)
        return element
