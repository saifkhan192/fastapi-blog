from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import configuration
from app.models import models
from app.schema import schemas
from app.schema.hash import Hash
from app.schema.token import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(configuration.get_db),
):
    print("request", request.__dict__)
    user: schemas.User = (
        db.query(models.User).filter(models.User.email == request.username).first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password"
        )
    access_token = create_access_token(data={"sub": user.email})
    # generate JWT token and return
    return {"access_token": access_token, "token_type": "bearer"}
