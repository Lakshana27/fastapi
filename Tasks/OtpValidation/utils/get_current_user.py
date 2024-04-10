from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import HTTPException, status, Security, Depends
from sqlalchemy.orm import Session

from OtpValidation.utils.get_db import get_db
from OtpValidation.utils.get_user import get_user
from OtpValidation.utils.token_management import verify_token


bearer_scheme = HTTPBearer()

def get_current_user(token: HTTPAuthorizationCredentials = Security(bearer_scheme),db : Session = Depends(get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate credentials",
                                         headers={"WWW-Authenticate": "Bearer"})
    
    token_data = verify_token(token.credentials, credential_exception)
    user =  get_user(token_data.email, db)
    if user is None:
        raise credential_exception
    return token_data
