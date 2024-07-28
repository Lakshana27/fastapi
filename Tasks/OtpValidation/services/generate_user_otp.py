from time import time
from fastapi import HTTPException, status

from OtpValidation.utils.get_user import get_user
from OtpValidation.utils.password_security import password_verification
from OtpValidation.utils.get_otp import get_otp
from OtpValidation.utils.send_otp import send_otp



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
    return {"message": "Successfully OTP Generated",
            "Quick Reminder": "You Have 1 min to use your OTP for Verification",
            "OTP": otp}