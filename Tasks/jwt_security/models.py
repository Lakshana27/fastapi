from sqlalchemy import Column, String, Integer, Boolean
from jwt_security.database import Base

class UserData(Base):
    __tablename__ = "userdata_jwt_Autho"

    user_id = Column("Id", Integer, primary_key=True)
    username = Column("Username", String, unique=True, nullable=False)
    password = Column("Password", String, nullable=False)
    name = Column("Name", String, nullable=False)
    email = Column("Email", String, nullable=False)
    role = Column("Role", String, nullable=False)
    active = Column("ActiveStatus", Boolean, default=True) 