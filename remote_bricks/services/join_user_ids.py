from fastapi import HTTPException

# Function to join user data with linked IDs
def join_user_ids(user_id, users_collection, linking_ids_collection):
    user = users_collection.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    linked_ids = list(linking_ids_collection.find({"user_id": user_id}))
    user["linked_ids"] = [str(linked_id["linked_id"]) for linked_id in linked_ids]
    
    return user
