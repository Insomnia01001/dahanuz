from pydantic import BaseModel

class KranBase(BaseModel):
    name_uz: str
    name_ru: str
    maxliftingcap: str
    maxradius: str
    liftingcap: str
    hooklifting: str
    description_uz: str
    description_ru: str

class KranCreate(KranBase):
    pass

class KranImgCreate(BaseModel):
    kran_id: int
    image_url: str


class LiftBase(BaseModel):
    name_uz: str
    name_ru: str
    description_uz: str
    description_ru: str

class LiftCreate(LiftBase):
    pass

class LiftImgCreate(BaseModel):
    lift_id: int
    image_url: str
