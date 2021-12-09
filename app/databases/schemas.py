from pydantic import BaseModel
from enum import Enum


class NoticesInformation(BaseModel):
    id: int
    date: str
    title: str
    link: str

    class Config:
        orm_mode = True  # ?
