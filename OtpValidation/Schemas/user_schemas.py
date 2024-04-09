from pydantic import BaseModel, EmailStr

class CreateUserData(BaseModel):
    email: EmailStr
    password: str

class NewPasswordRequest(BaseModel):
    email: EmailStr
    newpassword: str

class OTP_Validation(BaseModel):
    email: EmailStr
    otp: str
    
