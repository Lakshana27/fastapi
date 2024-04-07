from datetime import datetime,timedelta,timezone
from fastapi import HTTPException, status, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from jwt_security.Schemas.oauth_schemas import Token, TokenData
from jwt_security.utils import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from jwt_security.utils import bearer_scheme, verify_password
from jwt_security.database import get_db
from jwt_security.Services.user_services import get_user


def get_user_token(username, password, db):
    user = user_authentication(username, password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"user_id": user.user_id, "username": user.username, "role": user.role}, expires_delta=token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

def user_authentication(username, password, db):
    user = get_user(username, db)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: HTTPAuthorizationCredentials = Security(bearer_scheme),db : Session = Depends(get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate credentials",
                                         headers={"WWW-Authenticate": "Bearer"})
    
    token_data = verify_token(token.credentials, credential_exception)
    user =  get_user(token_data.username, db)
    if user is None:
        raise credential_exception
    return token_data
    
def verify_token(token: str, credential_exception: HTTPException):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if not user_id:
            raise credential_exception
        token_data = TokenData(user_id=user_id, username=payload.get("username"), role=payload.get("role"))
    except JWTError:
        raise credential_exception
    return token_data
    
