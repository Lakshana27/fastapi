from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from OtpValidation.Schemas.user_schemas import CreateUserData, NewPasswordRequest
from OtpValidation.Schemas.oauth_schemas import TokenData
from OtpValidation.utils.get_db import get_db
from OtpValidation.Services.create_new_user import create_new_user 
from OtpValidation.Services.generate_user_otp import generate_user_otp
from OtpValidation.Services.change_user_password import change_user_password
from OtpValidation.utils.get_current_user import  get_current_user

route = APIRouter(prefix="/User")


@route.post("/CreateUser", tags=["Create User"])
async def create_user(user: CreateUserData, db: Session = Depends(get_db)):
    return create_new_user(user, db)

@route.post("/OtpGenerate", tags=["OTP Generation"])
async def generate_otp(user_credential: CreateUserData , db: Session = Depends(get_db)):
    return generate_user_otp(user_credential, db)

@route.put("/Update_User", tags=["Authentication"])
async def update_user(user_credential: NewPasswordRequest, current_user: TokenData = Depends(get_current_user), db: Session = Depends(get_db)):
    return change_user_password(user_credential, current_user, db)
