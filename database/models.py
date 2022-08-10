from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(30), nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    email = Column(String(40), nullable=False, unique=True)
    password = Column(String(150), nullable=False)
    created_on = Column(Date)
    dob = Column(Date, nullable=False)
    is_active = Column(Boolean, nullable=False)
    is_superUser = Column(Boolean, nullable=False)
    avis = relationship('Avis', back_populates='users', cascade="all, delete-orphan")


class Avis(Base):
    __tablename__ = 'avis'
    avis_id = Column(Integer, primary_key=True, index=True)
    body = Column(Text, nullable=False)
    time_created = Column(DateTime)
    created_on = Column(Date)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    users = relationship('User', back_populates='avis')


"""
class Otp(Base):
    __tablename__ = 'otp'
    pass


class Following(Base):
    __tablename__ = 'following'
    pass
"""
