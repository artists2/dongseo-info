from pydantic import BaseModel
from abc import *


class BaseInformation(BaseModel):
    id: int
    date: str
    title: str


class NoticeInformation(BaseInformation):
    link: str

    class Config:
        orm_mode = True  # Python Class -> SQL (ORM)


class AcademicInformation(BaseInformation):
    link: str

    class Config:
        orm_mode = True


class RecruitInformation(BaseInformation):
    link: str

    class Config:
        orm_mode = True


class EventInformation(BaseInformation):
    link: str

    class Config:
        orm_mode = True


class ScholarInformation(BaseInformation):
    link: str

    class Config:
        orm_mode = True


class ScheduleInformation(BaseInformation):
    class Config:
        orm_mode = True
