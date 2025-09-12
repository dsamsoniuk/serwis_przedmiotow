from sqlalchemy.orm import Session
import api.models as models, api.schemas as schemas
from passlib.context import CryptContext

# Item
def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name, description=item.description, price=item.price, tax=item.tax)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item: schemas.ItemUpdate):
    db.query(models.Item).filter(models.Item.id == item.id).update({
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "tax": item.tax,
    })
    db.commit()
    return item


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User
def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, item: schemas.UserInDB):
    db_item = models.User(username=item.username,hashed_password= pwd_context.hash(item.password), email=item.email)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


