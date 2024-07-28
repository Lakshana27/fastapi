from fastapi import APIRouter, HTTPException
from schemas.user_schemas import RegisterRequest, LoginRequest, LinkingIDRequest, JoinResponseModel
from services.register_users import register_users
from services.login_user import login_user
from services.linking_ids import linking_ids
from services.join_user_ids import join_user_ids
from services.delete_users_chain import delete_users_chain
from config.db_config import users_collection, linking_ids_collection

# Create a router for user-related endpoints
router = APIRouter(tags=["users"])

# Endpoint for user registration
@router.post("/register")
async def register(request: RegisterRequest):
    return register_users(request, users_collection)

# Endpoint for user login
@router.post("/login")
async def login(request: LoginRequest):
    return login_user(request, users_collection)

# Endpoint for linking an ID to a user
@router.post("/link_id")
async def link_id(request: LinkingIDRequest):
    return linking_ids(request, users_collection, linking_ids_collection)

# Endpoint for joining user data
@router.get("/join-user-data/{user_id}", response_model=JoinResponseModel)
async def join_user_data(user_id: str):
    return join_user_ids(user_id, users_collection, linking_ids_collection)

# Endpoint for deleting a user and associated data
@router.delete("/delete-user/{user_id}")
async def delete_user(user_id: str):
    return delete_users_chain(user_id, users_collection, linking_ids_collection)
