import os
from dotenv import load_dotenv
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

# Retrieving the SENDER_EMAIL, SENDER_PASSWORD environment variable and assigning it to the SENDER_EMAIL, SENDER_PASSWORD variable
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

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
