from passlib.context import CryptContext

pwd_context= CryptContext(schemes=["bcrypt"], deprecated="auto")

# Verifying and Hashing Password
def password_hasing(password):
    return pwd_context.hash(password)

def password_verification(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)
