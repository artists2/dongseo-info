import requests
from pydantic import BaseModel
from bs4 import BeautifulSoup as bs
from abc import *

# self.page = page
# self.soup = bs(self.page.text, 'html.parser')


class BaseParser(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def parse(page):
        pass


class ScheduleParser(BaseParser):  # ScheduleParser.parse(page)
    @staticmethod
    def parse(page: str):
        soup = bs(page, "html.parser")
        return


class AcademicParser(BaseParser):
    def parse(self):
        return


class RecruitParser(BaseParser):
    def parse(self):
        pass


class NoticeParser(BaseParser):
    def parse(self):
        pass


class EventParser(BaseParser):
    def parse(self):
        pass


class ScholarParser(BaseParser):
    def parse(self):
        pass
