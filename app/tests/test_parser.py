import requests
from pydantic import BaseModel
from bs4 import BeautifulSoup as bs
import re


class Parsing:
    day: int  # 공지날짜
    text: str
    link: str  # 공지 이동 링크
    picture: bin  # 바이너리 저장

    def __init__(self, _page: str):
        self.page = requests.get(_page)  # page응답 안할시 구현해야함
        self.soup = bs(self.page.text, "html.parser")

    def schedule_parser(self) -> None:  # 매달 1일 parsing
        # https://www.dongseo.ac.kr/kr/index.php?pCode=dscalendar
        elements_day = self.soup.findAll("div", {"class": "date-core"})  # day
        elements_schedule = self.soup.findAll("div", {"class": "body-core"})  # schedule

        _day = [''.join(e.text.split()) for e in elements_day]
        _schedule = [''.join(s.text.split()) for s in elements_schedule]

        for i in range(0, len(_day)):  # test code
            print(_day[i], _schedule[i])

    def academic(self):  # 학사
        self.day = 0
        self.text = ''
        # elements_
        pass

    def important_academic(self):  # 중요 학사 공지 (중요 공지는 있는가 없는가 체크해야함)
        if not self.is_important():
            print("주요 공지가 없습니다.")
        _elements = self.soup.findAll("tr", {"class": "isnotice"})
        element = []
        for i in range(0, len(_elements)):
            e = list()
            e.append(_elements[i].find("span").text)
            e.append(_elements[i].find("td", {"class": "f-date date"}).text)
            e.append('https://www.dongseo.ac.kr' + _elements[i].find("a")["href"])
            # element.append(e)
            print(e)
        print(element)  # complete


    def recruit(self):  # 모집
        pass

    def important_recruit(self):  # 중요 모집 공지
        pass

    def notices(self):  # 공지
        pass

    def important_notices(self):  # 중요 공지
        pass

    def event(self):  # 행사
        pass

    def important_event(self):  # 중요 행사 공지
        pass

    def scholarship(self):  # 장학
        pass

    def important_scholarship(self):  # 중요 장학 공지
        pass

    def is_important(self) -> bool:  # 중요 공지가 있는지 없는지 반환
        if self.soup.findAll("tr", {"class": "isnotice"}):
            return True
        else:
            return False
