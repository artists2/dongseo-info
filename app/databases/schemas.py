from pydantic import BaseModel
from abc import *


class BaseInformation(metaclass=ABCMeta):
    id: int
    date: str
    title: str


class NoticesInformation(BaseModel, BaseInformation):
    # id: int
    # date: str
    # title: str
    link: str

    class Config:
        orm_mode = True  # Python Class -> SQL (ORM)


class ScheduleInformation(BaseModel, BaseInformation):
    # id: int
    # date: str
    # title: str

    class Config:
        orm_mode = True
