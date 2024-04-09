from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from OtpValidation.Schemas.user_schemas import CreateUserData, NewPasswordRequest,OTP_Validation
from OtpValidation.Schemas.oauth_schemas import TokenData
from OtpValidation.database import Base, engine, get_db
from OtpValidation.Services.user_service import create_new_user, generate_user_otp, change_user_password
from OtpValidation.Services.oauth_service import generate_token, get_current_user


route = APIRouter()

Base.metadata.create_all(bind=engine)

@route.post("/AccessToken", tags=["Access Token"])
async def get_token(user_otp: OTP_Validation, db: Session = Depends(get_db)):
    return generate_token(user_otp,db)

@route.post("/User/CreateUser", tags=["Create User"])
async def create_user(user: CreateUserData, db: Session = Depends(get_db)):
    return create_new_user(user, db)

@route.post("/User/OtpGenerate", tags=["OTP Generation"])
async def generate_otp(user_credential: CreateUserData , db: Session = Depends(get_db)):
    return generate_user_otp(user_credential, db)

@route.put("/User/Update_User", tags=["Authentication"])
async def update_user(user_credential: NewPasswordRequest, current_user: TokenData = Depends(get_current_user), db: Session = Depends(get_db)):
    return change_user_password(user_credential, current_user, db)


