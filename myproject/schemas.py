from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class ManufactorBase(BaseModel):
    name: str

    class Config:
        orm_mode = True