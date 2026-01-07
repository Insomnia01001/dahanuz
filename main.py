from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from db import engine, get_db
from models import Base
import crud
import schemas


app = FastAPI()

# 🔹 Jadvallarni yaratish
Base.metadata.create_all(bind=engine)

# 🔹 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================== KRAN ==================

@app.get("/krans/")
def get_krans(db: Session = Depends(get_db)):
    return crud.get_krans(db)


@app.get("/krans/{kran_id}")
def get_kran_by_id(kran_id: int, db: Session = Depends(get_db)):
    return crud.get_kran_with_img_by_id(db, kran_id)


@app.post("/krans/add/")
def add_kran(kran: schemas.KranCreate, db: Session = Depends(get_db)):
    return crud.add_kran(db, kran)


@app.post("/krans/img/add/")
def add_kran_img(kran: schemas.KranImgCreate, db: Session = Depends(get_db)):
    return crud.add_kran_img(db, kran)


@app.put("/krans/update/{kran_id}")
def update_kran(
    kran_id: int,
    kran: schemas.KranCreate,
    db: Session = Depends(get_db)
):
    return crud.update_kran(db, kran_id, kran)


@app.delete("/krans/delete/{kran_id}")
def delete_kran(kran_id: int, db: Session = Depends(get_db)):
    return crud.delete_kran(db, kran_id)


# ================== LIFT ==================

@app.get("/lifts/")
def get_lifts(db: Session = Depends(get_db)):
    return crud.get_lifts(db)


@app.get("/lifts/{lift_id}")
def get_lift_by_id(lift_id: int, db: Session = Depends(get_db)):
    return crud.get_lift_by_id(db, lift_id)


@app.post("/lifts/add/")
def add_lift(lift: schemas.LiftCreate, db: Session = Depends(get_db)):
    return crud.add_lift(db, lift)


@app.post("/lifts/img/add/")
def add_lift_img(lift: schemas.LiftImgCreate, db: Session = Depends(get_db)):
    return crud.add_lift_img(db, lift)


@app.put("/lifts/update/{lift_id}")
def update_lift(
    lift_id: int,
    lift: schemas.LiftCreate,
    db: Session = Depends(get_db)
):
    return crud.update_lift(db, lift_id, lift)


@app.delete("/lifts/delete/{lift_id}")
def delete_lift(lift_id: int, db: Session = Depends(get_db)):
    return crud.delete_lift(db, lift_id)
