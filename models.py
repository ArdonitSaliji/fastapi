from sqlalchemy import Column, Integer, String, BigInteger, JSON, BLOB, Boolean
from db import Base

class User(Base):
    __tablename__ = 'users' 
    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(length=50))
    email = Column(String(length=100))
    password = Column(String(length=255))
    cart = Column(JSON)
    profileImage = Column(BLOB)
    profileImageName = Column(String(length=100))
    isActive = Column(Boolean)
    emailVerified = Column(Boolean)