from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(255), index=True)
    price = Column(Float, index=True,nullable=False, default=0.0)
    tax = Column(Float, index=True, nullable=False, default=0.0)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), index=True)
    email = Column(String(100), index=True)
    full_name = Column(String(100), index=True)
    hashed_password = Column(String(255), index=True)
    disabled = Column(Boolean, index=True, default=1)

