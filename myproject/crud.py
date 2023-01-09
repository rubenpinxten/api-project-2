from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import auth
import models
import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_prodyct(db: Session, prodcut: schemas.ProductCreate, user_id: int):
    db_product = models.Product(**prodcut.dict(), owner_id=user_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return 