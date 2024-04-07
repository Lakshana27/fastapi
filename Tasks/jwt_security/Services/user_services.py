from fastapi import HTTPException, status
from jwt_security.models import UserData
from jwt_security.utils import password_hasing

def get_user(username,db):
    return db.query(UserData).filter(UserData.username==username).first() 
    
def check_user_validity(username, db):
    user = get_user(username, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The Given Username '{username}' is Not Exist")
    return user

def create_new_user(user, role, db):
    hash_password = password_hasing(user.password)
    to_create_user = UserData(username = user.username,
                              name = user.name,
                              email = user.email,
                              role = role.value,
                              password = hash_password)
    
    try:
        db.add(to_create_user)
        db.commit()
        return {"Message" : f"User {to_create_user.name} was Successfully Created"}
    
    except:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,
                            detail=f"The Given Username '{user.username}' is Not Exist")
    
def change_user_activation(user_id, active, admin, db):
    if admin.role != "Admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"Access denied: '{admin.username}' does not have authorization to modify activity status")
    user = db.query(UserData).filter(UserData.user_id==user_id).first()
    if not user:
        raise HTTPException(
            status_code=422,
            detail=f"Given userid '{user_id}' is not found"
            )
    user.active = active
    db.commit()
    return {"message": f"User '{user.name}' is now set to {'Active' if user.active else 'Inactive'}"}

def modify_user_details(username, user_details, db):
    user = check_user_validity(username, db)
    try:
        if user_details.name:
            user.name = user_details.name
        if user_details.email:
            user.email = user_details.email
            
        db.commit()

    except:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="No data provided for user profile update")
    
    return{"message": f"Profile update successful for '{user.username}'"}




    

    


    

