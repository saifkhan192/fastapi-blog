from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.api.user import get_by_email
from app.schema.token import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")
from sqlalchemy.orm import Session

from app.database import configuration

get_db = configuration.get_db


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    token_data = verify_token(token)
    print("token_data", token_data)
    user = get_by_email(str(token_data.username), db)
    print("user", user)
    return user
