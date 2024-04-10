from fastapi import HTTPException, status

from OtpValidation.utils.get_user import get_user


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