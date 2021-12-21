from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Notices(Base):
    __tablename__ = "notice_info"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)  # unique 설정 => id
    date = Column(String(30))
    title = Column(String(100))
    link = Column(String(110))


class Schedules(Base):
    __tablename__ = "schedule_info"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)  # unique 설정 => id
    date = Column(String(30))
    title = Column(String(100))
