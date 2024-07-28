from fastapi import HTTPException
from utils.password_security import password_verification

# Function to log in a user
def login_user(request, users_collection):
    user = users_collection.find_one({"email": request.email})
    if not user or not password_verification(request.password, user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect Email or Password")
    
    return {"message": f"'{user['username']}' LoggedIn successfully"}
