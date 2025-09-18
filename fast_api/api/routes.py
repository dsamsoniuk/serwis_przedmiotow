from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from api.crud import ItemCrud, UserCrud
from api.database import get_db
from api.authentications import authenticate_user, create_access_token, get_current_active_user
from api.models import  User
from api.schemas import  Token, User, UserInDB, Item, ItemCreate, ItemUpdate
from typing import Annotated
from datetime import datetime, timedelta
import os

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


'''Main'''
router = APIRouter(tags=["Main"])

@router.get("/", 
            summary="Ogolne endpoint-y", 
            description="""
            Tutaj jest zwykly opis ![Logo](/static/logo-teal.png)
            """
)
async def root():
    return {"message": "Hello World !!!"}


'''Authorization'''
router_auth = APIRouter(tags=["authorization"])

@router_auth.post("/token")
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


'''User'''
router_user = APIRouter(tags=["user"])

@router_user.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@router_user.post("/users/", response_model=UserInDB)
def create_user(item: UserInDB, db: Session = Depends(get_db)):
    return UserCrud.create_user(db=db, item=item)


'''Item'''
router_item = APIRouter(tags=["item"])

@router_item.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return ItemCrud.create_item(db=db, item=item)

@router_item.patch("/items/", response_model=Item)
def update_item(item: ItemUpdate, db: Session = Depends(get_db)):
    return ItemCrud.update_item(db=db, item=item)

@router_item.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int = 1, db: Session = Depends(get_db)):
    db_item = ItemCrud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router_item.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = ItemCrud.get_items(db, skip=skip, limit=limit)
    return items