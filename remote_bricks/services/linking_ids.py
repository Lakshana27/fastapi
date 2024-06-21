from fastapi import HTTPException

# Function to link an ID to a user
def linking_ids(request, users_collection, linking_ids_collection):
    user = users_collection.find_one({"_id": request.user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    linking_ids_collection.insert_one({"user_id": user["_id"], "linked_id": request.linked_id})
    
    return {"message": f"Linked ID '{request.linked_id}' linked successfully with user ID '{user['_id']}'"}
