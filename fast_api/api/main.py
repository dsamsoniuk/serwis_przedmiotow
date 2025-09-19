from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from  api.crud import ItemCrud, UserCrud
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
import os
import time

from  api.routes import router, router_auth, router_user, router_item

load_dotenv()

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(router)
app.include_router(router_auth)
app.include_router(router_user)
app.include_router(router_item)

app.mount("/static", StaticFiles(directory="static"), name="static")

