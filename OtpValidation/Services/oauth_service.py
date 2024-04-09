from time import time
from datetime import timedelta, datetime, timezone
from fastapi import HTTPException, status, Security, Depends
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from OtpValidation.database import get_db
from OtpValidation.Services.user_service import get_user
from OtpValidation.utils import OTP_TIME_LIMIT
from OtpValidation.utils import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from OtpValidation.Schemas.oauth_schemas import Token,TokenData
from OtpValidation.utils import bearer_scheme

def generate_token(user_otp,db):
    user = get_user(user_otp.email, db)
    time_since_otp_generation = time() - user.otp_time
    if time_since_otp_generation > OTP_TIME_LIMIT:
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT,
                            detail="The OTP validation has timed out. Please regenerate the OTP and try again")
    if not user or not user_otp.otp==user.otp:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect Email or OTP",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"user_id": user.user_id, "email": user.email})
    return Token(access_token=access_token, token_type="bearer")

def create_access_token(data: dict, expires_delta = int(ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
    return encode_jwt

def get_current_user(token: HTTPAuthorizationCredentials = Security(bearer_scheme),db : Session = Depends(get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate credentials",
                                         headers={"WWW-Authenticate": "Bearer"})
    
    token_data = verify_token(token.credentials, credential_exception)
    user =  get_user(token_data.email, db)
    if user is None:
        raise credential_exception
    return token_data

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

