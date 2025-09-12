from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import api.crud
from api.database import get_db
from api.authentications import authenticate_user, create_access_token, get_current_active_user
from fastapi import Depends, FastAPI, HTTPException, status
from api.models import  User
from api.schemas import  Token, User, UserInDB, Item, ItemCreate, ItemUpdate

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os, time
import time

# os.environ["TZ"] = "Poland/Warsaw"
# time.tzset()

load_dotenv()


app = FastAPI()


ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer", expire_time=int(datetime.now().timestamp()))


@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]


#---------------------------------------------

@app.post("/users/", response_model=UserInDB)
def create_user(item: UserInDB, db: Session = Depends(get_db)):
    return api.crud.create_user(db=db, item=item)


@app.get("/")
async def root():
    a = {"aaa": 34}
    return {"message": "Hello World 272"}


@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return api.crud.create_item(db=db, item=item)

@app.patch("/items/", response_model=Item)
def update_item(item: ItemUpdate, db: Session = Depends(get_db)):
    return api.crud.update_item(db=db, item=item)

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = api.crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = api.crud.get_items(db, skip=skip, limit=limit)
    return items