from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from OtpValidation.schemas.user_schemas import OTP_Validation
from OtpValidation.schemas.oauth_schemas import TokenData
from OtpValidation.utils.get_db import get_db
from OtpValidation.services.generate_token import generate_token

route = APIRouter()

@route.post("/AccessToken", tags=["Access Token"])
async def get_token(user_otp: OTP_Validation, db: Session = Depends(get_db)):
    return generate_token(user_otp,db)

