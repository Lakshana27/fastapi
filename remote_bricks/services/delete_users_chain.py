from fastapi import HTTPException

# Function to delete a user and their associated data
def delete_users_chain(user_id, users_collection, linking_ids_collection):
    result = users_collection.delete_one({"_id": user_id})
    if not result.deleted_count:
        raise HTTPException(status_code=404, detail="User not found")
    
    linking_ids_collection.delete_many({"user_id": user_id})
    
    return {"message": "User and all associated data deleted successfully"}
