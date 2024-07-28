from time import time
import os
from dotenv import load_dotenv
from fastapi import HTTPException, status

from OtpValidation.utils.get_user import get_user
from OtpValidation.schemas.oauth_schemas import Token
from OtpValidation.utils.token_management import create_access_token

load_dotenv

OTP_TIME_LIMIT = os.getenv("OTP_TIME_LIMIT")

def generate_token(user_otp,db):
    credential_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect Email or OTP",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = get_user(user_otp.email, db)
    if not user:
        raise credential_exception
    time_since_otp_generation = time() - user.otp_time
    if time_since_otp_generation > int(OTP_TIME_LIMIT):
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT,
                            detail="The OTP validation has timed out. Please regenerate the OTP and try again")
    if not user_otp.otp==user.otp:
        raise credential_exception
    access_token = create_access_token(
        data={"user_id": user.user_id, "email": user.email})
    return Token(access_token=access_token, token_type="bearer")






