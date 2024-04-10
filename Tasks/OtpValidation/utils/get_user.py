from OtpValidation.models.UserData import UserData

def get_user(email, db):
    return db.query(UserData).filter(UserData.email == email).first()