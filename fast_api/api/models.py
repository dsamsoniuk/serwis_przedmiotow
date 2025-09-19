from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Table
from api.database import Base
from sqlalchemy.orm import relationship

# tabela asocjacyjna
user_item = Table(
    "user_item",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("item_id", Integer, ForeignKey("items.id"), primary_key=True)
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), index=True)
    email = Column(String(100), index=True)
    full_name = Column(String(100), index=True)
    hashed_password = Column(String(255), index=True)
    disabled = Column(Boolean, index=True, default=1)

    # relacja many-to-many
    items = relationship(
        "Item",
        secondary=user_item,
        back_populates="users"
    )

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(255), index=True)
    price = Column(Float, index=True,nullable=False, default=0.0)
    tax = Column(Float, index=True, nullable=False, default=0.0)

    # relacja odwrotna
    users = relationship(
        "User",
        secondary=user_item,
        back_populates="items"
    )