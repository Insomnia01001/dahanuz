from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Kran, KranImg, Lift, LiftImg

def get_krans(db: Session):
    krans = db.query(Kran).all()
    if not krans:
        raise HTTPException(status_code=404, detail="Kranlar topilmadi")
    return krans


def get_kran_with_img_by_id(db: Session, kran_id: int):
    kran = db.query(Kran).filter(Kran.id == kran_id).first()
    if not kran:
        raise HTTPException(status_code=404, detail="Kran topilmadi")

    return {
        "id": kran.id,
        "name_uz": kran.name_uz,
        "name_ru": kran.name_ru,
        "maxliftingcap": kran.maxliftingcap,
        "maxradius": kran.maxradius,
        "liftingcap": kran.liftingcap,
        "hooklifting": kran.hooklifting,
        "description_uz": kran.description_uz,
        "description_ru": kran.description_ru,
        "images": [
            {
                "id": img.id,
                "image_url": img.image_url
            }
            for img in kran.images
        ]
    }


def add_kran(db: Session, kran):
    new_kran = Kran(
        name_uz=kran.name_uz,
        name_ru=kran.name_ru,
        maxliftingcap=kran.maxliftingcap,
        maxradius=kran.maxradius,
        liftingcap=kran.liftingcap,
        hooklifting=kran.hooklifting,
        description_uz=kran.description_uz,
        description_ru=kran.description_ru
    )
    db.add(new_kran)
    db.commit()
    db.refresh(new_kran)
    return {"message": "Kran qo‘shildi", "id": new_kran.id}

def add_kran_img(db: Session, kran_img):
    kran = db.query(Kran).filter(Kran.id == kran_img.kran_id).first()
    if not kran:
        raise HTTPException(status_code=404, detail="Kran topilmadi")

    img = KranImg(
        kran_id=kran_img.kran_id,
        image_url=kran_img.image_url
    )
    db.add(img)
    db.commit()
    return {"message": "Kran img qo‘shildi"}

def update_kran(db: Session, kran_id: int, kran):
    kran_db = db.query(Kran).filter(Kran.id == kran_id).first()
    if not kran_db:
        raise HTTPException(status_code=404, detail="Kran topilmadi")

    kran_db.name_uz = kran.name_uz
    kran_db.name_ru = kran.name_ru
    kran_db.maxliftingcap = kran.maxliftingcap
    kran_db.maxradius = kran.maxradius
    kran_db.liftingcap = kran.liftingcap
    kran_db.hooklifting = kran.hooklifting
    kran_db.description_uz = kran.description_uz
    kran_db.description_ru = kran.description_ru

    db.commit()
    return {"message": "Kran yangilandi"}


def delete_kran(db: Session, kran_id: int):
    kran = db.query(Kran).filter(Kran.id == kran_id).first()
    if not kran:
        raise HTTPException(status_code=404, detail="Kran topilmadi")

    db.delete(kran)
    db.commit()
    return {"message": "Kran o‘chirildi"}









# lift section


def get_lifts(db: Session):
    lifts = db.query(Lift).all()
    if not lifts:
        raise HTTPException(status_code=404, detail="Liftlar topilmadi")
    return lifts

def get_lift_by_id(db: Session, lift_id: int):
    lift = db.query(Lift).filter(Lift.id == lift_id).first()
    if not lift:
        raise HTTPException(status_code=404, detail="Lift topilmadi")
    return lift

def add_lift(db: Session, lift):
    new_lift = Lift(
        name_uz=lift.name_uz,
        name_ru=lift.name_ru,
        description_uz=lift.description_uz,
        description_ru=lift.description_ru
    )
    db.add(new_lift)
    db.commit()
    db.refresh(new_lift)
    return {"message": "Lift qo‘shildi", "id": new_lift.id}

def add_lift_img(db: Session, lift_img):
    lift = db.query(Lift).filter(Lift.id == lift_img.lift_id).first()
    if not lift:
        raise HTTPException(status_code=404, detail="Lift topilmadi")

    img = LiftImg(
        lift_id=lift_img.lift_id,
        image_url=lift_img.image_url
    )
    db.add(img)
    db.commit()
    return {"message": "Lift img qo‘shildi"}

def update_lift(db: Session, lift_id: int, lift):
    lift_db = db.query(Lift).filter(Lift.id == lift_id).first()
    if not lift_db:
        raise HTTPException(status_code=404, detail="Lift topilmadi")

    lift_db.name_uz = lift.name_uz
    lift_db.name_ru = lift.name_ru
    lift_db.description_uz = lift.description_uz
    lift_db.description_ru = lift.description_ru

    db.commit()
    return {"message": "Lift yangilandi"}

def delete_lift(db: Session, lift_id: int):
    lift = db.query(Lift).filter(Lift.id == lift_id).first()
    if not lift:
        raise HTTPException(status_code=404, detail="Lift topilmadi")

    db.delete(lift)
    db.commit()
    return {"message": "Lift o‘chirildi"}
