from sqlalchemy.orm import Session

from . import models, schemas


def get_link(db: Session, short_url: str):
    return db.query(models.Link).filter(models.Link.short_url == short_url).first()


def create_link(db: Session, link: schemas.LinkCreate):
    print(link)
    db_link = models.Link(**link)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link
