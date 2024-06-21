from fastapi import HTTPException
from utils.password_security import password_hasing

# Function to register a new user
def register_users(request, users_collection):
    user = users_collection.find_one({"email": request.email})
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    request.password = password_hasing(request.password)
    user_data = request.__dict__
    user_data.update({"_id": str(users_collection.count_documents({}) + 1)})
    result = users_collection.insert_one(user_data)
    
    return {"message": "User registered successfully", "id": str(result.inserted_id)}
