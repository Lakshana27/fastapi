from pydantic import BaseModel, EmailStr

# Schema for user login request
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# Schema for user registration request, extends LoginRequest
class RegisterRequest(LoginRequest):
    username: str

# Schema for linking ID request
class LinkingIDRequest(BaseModel):
    user_id: str
    linked_id: str

# Schema for join response model
class JoinResponseModel(BaseModel):
    _id: int
    email: str
    username: str
    linked_ids: list[str]
