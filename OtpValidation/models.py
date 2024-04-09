from sqlalchemy import Column, String, Integer, TIMESTAMP, func
from OtpValidation.database import Base

class UserData(Base):
    __tablename__ = "otp_table"

    user_id = Column("ID", Integer, primary_key=True)
    email = Column("Email", String, unique=True, nullable=False)
    password = Column("HashPassword", String, nullable=False)
    time = Column("LoginTime", TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    otp = Column("OTP", String)
    otp_time = Column("OTP_TimeLimit", Integer)
