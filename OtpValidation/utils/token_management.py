import os
from dotenv import load_dotenv
from datetime import timedelta, datetime, timezone

from fastapi import HTTPException
from jose import JWTError, jwt

from OtpValidation.Schemas.oauth_schemas import TokenData


load_dotenv()

# Retrieving the SECRET_KEY, ALGORITH, ACCESS_TOKEN_EXPIRE_MINUTES environment variable and assigning it to the SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES variable
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM= os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES= os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

def create_access_token(data: dict, expires_delta = int(ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
    return encode_jwt

def verify_token(token: str, credential_exception: HTTPException):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms= [ALGORITHM])
        user_id = payload.get("user_id")
        if not user_id:
            raise credential_exception
        token_data = TokenData(user_id= user_id, email= payload.get("email"))
    except JWTError:
        raise credential_exception
    return token_data