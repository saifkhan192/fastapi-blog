from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import models
from app.schema import schemas
from app.schema.hash import Hash


def create(request: schemas.User, db: Session):
    hashedPassword = Hash.bcrypt(request.password)
    user = models.User(name=request.name, email=request.email, password=hashedPassword)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    return user


def get_by_email(email: str, db: Session):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"User with email {email} not found"
        )
    return user


def get_all(db: Session):
    return db.query(models.User).all()
