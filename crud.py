from sqlalchemy.orm import Session

import models
import schemas


def get_apartments(db: Session, limit: int) -> list[models.Apartment]:
    return db.query(models.Apartment).filter(models.Apartment.is_valid).limit(
        limit).all()


def get_apartment_by_link(db: Session, link: str) -> models.Apartment:
    return db.query(models.Apartment).filter(models.Apartment.link == link).first()


def create_apartment(db: Session, apartment: schemas.ApartmentCreate) -> models.Apartment:
    db_apartment = models.Apartment(**apartment.dict(), is_valid=True)
    db.add(db_apartment)
    db.commit()
    db.refresh(db_apartment)
    return db_apartment


def invalidate_apartment(db: Session, apartment: schemas.Apartment) -> models.Apartment:
    apartment.is_valid = False
    db.commit()
    db.refresh(apartment)
    return apartment
