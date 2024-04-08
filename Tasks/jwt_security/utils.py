import os 
from dotenv import load_dotenv

from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from passlib.context import CryptContext

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2scheme = OAuth2PasswordBearer(tokenUrl="Access-Token")

bearer_scheme = HTTPBearer()

def password_hasing(password):
    return pwd_context.hash(password)
    

def verify_password(plain_password, hash_password):
    return pwd_context.verify(plain_password,hash_password)
