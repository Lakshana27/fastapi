from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from jwt_security.Schemas.oauth_schemas import TokenData
from jwt_security.Schemas.user_schemas import UserInfo, CreateUserData, Role, UpdateUserRequest
from jwt_security.database import Base, engine, get_db
from jwt_security.Services.oauth_services import get_user_token, get_current_user
from jwt_security.Services.user_services import create_new_user, check_user_validity, change_user_activation, modify_user_details
 
route = APIRouter()

Base.metadata.create_all(bind=engine)

@route.post("/User_Data/Generate_Token/login", tags=["Acces Token"])
async def get_token(username: str = Body(...), password: str = Body(...), db: Session = Depends(get_db)):
    return get_user_token(username, password, db)

@route.get("/User_Data/Get_User", tags=['User'], response_model=UserInfo)
async def validate_user(username: str, db: Session = Depends(get_db)):
    return  check_user_validity(username, db)


@route.post("/User_Data/Create_User", tags=['Create User'])
async def create_user(user: CreateUserData, role: Role, db: Session = Depends(get_db)):
    return create_new_user(user, role, db)

@route.put("/User_Data/Update_Activity_Status", tags=["Authentication"])
async def update_user_activation(user_id: int, active: bool = True, admin: TokenData = Depends(get_current_user), db: Session = Depends(get_db)):
    return change_user_activation(user_id, active, admin, db)

@route.put("/User_Data/Update_User", tags=["Authentication"],dependencies=[Depends(get_current_user)])
async def update_user(username: str, user_details: UpdateUserRequest, db: Session = Depends(get_db)):
    return modify_user_details(username, user_details, db)
    
