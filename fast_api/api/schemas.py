from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    
class ItemCreate(ItemBase):
    pass   
class ItemUpdate(ItemBase):
    id: int

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
    expire_time: int

class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str
