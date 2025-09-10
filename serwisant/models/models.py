from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import  Column, Integer, String, DateTime, Float, Text, func

Base = declarative_base()

# class User(Base):
#     __tablename__ = "user"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     age = Column(Integer)

#     def __repr__(self):
#         return f"<User(name='{self.name}', age={self.age})>"

# class Token(Base):
#     __tablename__ = "token"
#     id = Column(Integer, primary_key=True)
#     token = Column(String)
#     expire_time = Column(Integer)

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(255), index=True)
    price = Column(Float, index=True,nullable=False, default=0.0)
    tax = Column(Float, index=True, nullable=False, default=0.0)


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True)
    created_at = Column(
            DateTime, 
            nullable=True,              
            server_default=func.now()  
        )