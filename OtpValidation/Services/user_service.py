from time import time
from fastapi import HTTPException, status

from OtpValidation.models import UserData
from OtpValidation.utils import get_otp, password_hasing, password_verification, send_otp

def get_user(email, db):
    return db.query(UserData).filter(UserData.email == email).first()

def create_new_user(user, db):
    hash_password = password_hasing(user.password)
    to_create_user = UserData(email = user.email,
                              password = hash_password)
    db.add(to_create_user)
    db.commit() 
    return{"message": f"Successfully created user id- {to_create_user.user_id}"}
    
    # try:
    #     db.add(to_create_user)
    #     db.commit() 
    #     return{"message": f"Successfully created user id- {to_create_user.user_id}"}
    
    # except:
    #     raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,
    #                         detail=f"Given email '{to_create_user.email}' already exist")
    
def generate_user_otp(credentials, db):
    user_data = get_user(credentials.email, db)
    if not user_data or not password_verification(credentials.password, user_data.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User Not Found! Invalid Credentials")
    
    otp = get_otp()
    user_data.otp = otp
    user_data.otp_time = time()
    send_otp(user_data.email, otp)
    db.commit()
    return {"OTP": otp,
            "message": "Successfully OTP Generated"}

def change_user_password(credentials, current_user, db):
    if credentials.email != current_user.email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"Access denied": "You can only change your own password."}
        )
    user = get_user(credentials.email, db)
    user.password = credentials.newpassword
    db.commit()
    return {"message": "Password change successful. You can now log in with your new password."}