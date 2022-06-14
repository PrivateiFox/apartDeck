from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return RedirectResponse(url='/apartments/')


@app.post("/apartments/create", response_model=schemas.Apartment)
def create_apartment(apartment: schemas.ApartmentCreate, db: Session = Depends(get_db)):
    db_apartment = crud.get_apartment_by_link(db, link=apartment.link)
    if db_apartment:
        if not db_apartment.is_valid:
            raise HTTPException(status_code=400, detail="Apartment was marked as invalid")
        raise HTTPException(status_code=400, detail="Link already registered")
    return crud.create_apartment(db=db, apartment=apartment)


@app.get("/apartments/invalidate")
def invalidate_apartment(link: str, db: Session = Depends(get_db)):
    db_apartment = crud.get_apartment_by_link(db, link=link)
    if not db_apartment:
        raise HTTPException(status_code=400, detail="No matching apartment found")
    return crud.invalidate_apartment(db=db, apartment=db_apartment)


@app.get("/apartments/", response_model=list[schemas.ApartmentBase])
def read_apartments(limit: int = 100, db: Session = Depends(get_db)):
    apartments = crud.get_apartments(db, limit=limit)
    return apartments
