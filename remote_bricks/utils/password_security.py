from passlib.context import CryptContext

# Create a password context for hashing and verifying passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash a password
def password_hasing(password):
    return pwd_context.hash(password)

# Function to verify a password against a hash
def password_verification(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
