from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Kran(Base):
    __tablename__ = "kran"

    id = Column(Integer, primary_key=True, index=True)

    name_uz = Column(String(80))
    name_ru = Column(String(80))

    maxliftingcap = Column(String(80))
    maxradius = Column(String(80))
    liftingcap = Column(String(80))
    hooklifting = Column(String(80))

    description_uz = Column(String(800))
    description_ru = Column(String(800))

    images = relationship("KranImg", back_populates="kran", cascade="all, delete")


class KranImg(Base):
    __tablename__ = "kranimg"

    id = Column(Integer, primary_key=True, index=True)
    kran_id = Column(Integer, ForeignKey("kran.id", ondelete="CASCADE"))
    image_url = Column(Text)

    kran = relationship("Kran", back_populates="images")


class Lift(Base):
    __tablename__ = "lift"

    id = Column(Integer, primary_key=True, index=True)

    name_uz = Column(String(80))
    name_ru = Column(String(80))

    description_uz = Column(String(400))
    description_ru = Column(String(400))

    images = relationship("LiftImg", back_populates="lift", cascade="all, delete")


class LiftImg(Base):
    __tablename__ = "liftimg"

    id = Column(Integer, primary_key=True, index=True)
    lift_id = Column(Integer, ForeignKey("lift.id", ondelete="CASCADE"))
    image_url = Column(Text)

    lift = relationship("Lift", back_populates="images")
