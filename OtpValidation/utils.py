import random
import os
from dotenv import load_dotenv
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from fastapi.security import HTTPBearer
from passlib.context import CryptContext

load_dotenv()

# Retrieving the SECRET_KEY, ALGORITH, ACCESS_TOKEN_EXPIRE_MINUTES environment variable and assigning it to the SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES variable
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM= os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES= os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

# Retrieving the SENDER_EMAIL, SENDER_PASSWORD environment variable and assigning it to the SENDER_EMAIL, SENDER_PASSWORD variable
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

pwd_context= CryptContext(schemes=["bcrypt"], deprecated="auto")

bearer_scheme = HTTPBearer()

# Generate OTP function
def get_otp():
    return random.randint(100000, 999999)

# Verifying and Hashing Password
def password_hasing(password):
    return pwd_context.hash(password)

def password_verification(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)

# Maximum duration (in seconds) for which an OTP remains valid
OTP_TIME_LIMIT = 10

# Send the email containing the OTP to the receiver's email address.
def send_otp(receiver_email, otp):
    # Create message
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = receiver_email
    message['Subject'] = 'One-Time Password for Account Verification'

    # Email body
    body = f'Dear User, Use this OTP {otp} to verify your account. \
             Keep it confidential and do not share it with anyone.'
    
    message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server
    with SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Start TLS encryption
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message.as_string())

