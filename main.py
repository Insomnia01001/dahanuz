from fastapi import FastAPI, Depends,APIRouter,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, get_db
from models import Base,Kran,Lift
import crud
import schemas
from sqlalchemy.orm import joinedload


app = FastAPI()

# 🔹 Jadvallarni yaratish

# 🔹 CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://dahanuz-frontend.netlify.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================== KRAN ==================

@app.get("/krans/", response_model=list[schemas.KranOut])
def get_krans(db: Session = Depends(get_db)):
    krans = (
        db.query(Kran)
        .options(joinedload(Kran.images))
        .all()
    )
    return krans




@app.get("/krans/{kran_id}", response_model=schemas.KranDetailOut)
def get_kran_by_id(kran_id: int, db: Session = Depends(get_db)):
    kran = (
        db.query(Kran)
        .options(joinedload(Kran.images))
        .filter(Kran.id == kran_id)
        .first()
    )

    if not kran:
        raise HTTPException(status_code=404, detail="Kran not found")

    return kran


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

@app.get("/lifts/",response_model=list[schemas.LiftOut])
def get_lifts(db: Session = Depends(get_db)):
    lifts = (db.query(Lift).options(joinedload(Lift.images)).all())
    return lifts


@app.get("/lifts/{lift_id}", response_model=schemas.LiftOut)
def get_lift_by_id(lift_id: int, db: Session = Depends(get_db)):
    lift = (
        db.query(Lift)
        .options(joinedload(Lift.images))
        .filter(Lift.id == lift_id)
        .first()
    )

    if not lift:
        raise HTTPException(status_code=404, detail="Lift not found")

    return lift


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
