from fastapi import HTTPException, status

from OtpValidation.models.UserData import UserData
from OtpValidation.utils.password_security import  password_hasing

def create_new_user(user, db):
    hash_password = password_hasing(user.password)
    to_create_user = UserData(email = user.email,
                              password = hash_password)
    try:
        db.add(to_create_user)
        db.commit() 
        return{"message": f"Successfully created user id- {to_create_user.user_id}"}
    
    except:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,
                            detail=f"Given email '{to_create_user.email}' already exist")