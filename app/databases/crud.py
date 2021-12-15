from sqlalchemy.orm import Session

from . import models, schemas


def create_notices(db: Session, id: int, date: str, title: str, link: str) -> models.Notices:
    notice_info = models.Notices(id=id, date=date, title=title, link=link)
    db.add(notice_info)
    db.commit()
    db.refresh(notice_info)
    return notice_info


def get_notices(db: Session):
    pass


def update_notices(db: Session):
    pass


def delete_notices(db: Session):
    pass


def create_schedules(db: Session, id: int, date: str, title: str) -> models.Notices:
    schedule_info = models.Schedules(id=id, date=date, title=title)
    db.add(schedule_info)
    db.commit()
    db.refresh(schedule_info)
    return schedule_info


def get_schedule(db: Session):
    pass


def update_schedule(db: Session):
    pass


def delete_schedule(db: Session):
    pass


# https://fastapi.tiangolo.com/tutorial/sql-databases/
