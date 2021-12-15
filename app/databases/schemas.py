from pydantic import BaseModel
from enum import Enum


class NoticesInformation(BaseModel):
    id: int
    date: str
    title: str
    link: str

    class Config:
        orm_mode = True  # Python Class -> SQL (ORM)


class ScheduleInformation(BaseModel):
    id: int
    date: str
    title: str

    class Config:
        orm_mode = True
