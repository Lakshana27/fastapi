from enum import Enum
from pydantic import BaseModel, EmailStr

class Role(Enum):
    USER = "User"
    ADMIN = "Admin"

class CreateUser(BaseModel):
    username: str
    name: str
    email: EmailStr
    
class CreateUserData(CreateUser):
    password: str

class UserInfo(CreateUser):
    user_id: int
    role: Role

class UpdateUserRequest(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    


