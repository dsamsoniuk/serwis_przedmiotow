

from sqlalchemy.orm import Session
from database import get_db
from models import User, Item
from authentications import get_password_hash

def seedUsers(db):
    users = [
        User(username="jacek", email="jacek@example.com", hashed_password=get_password_hash("jacek"), full_name="jacek exam", disabled=False),
        User(username="ala", email="ala@example.com", hashed_password=get_password_hash("ala"), full_name="ala exam"),
    ]
    print(users)
    db.add_all(users)
    db.commit()
    db.close()

def seedItems(db):
    users = [
        Item(name="Gazeta", description="Pomorska", price=14.3, tax=23),
        Item(name="Czasopismo", description="Uśmiech", price=4.3, tax=23),
    ]
    print(users)
    db.add_all(users)
    db.commit()
    db.close()

if __name__ == "__main__":

    # db: Session = Depends(get_db)
    db: Session = next(get_db())  
    seedUsers(db)
    seedItems(db)