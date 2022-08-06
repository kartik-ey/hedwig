from sqlalchemy import Column, Integer, String, Text, Time, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(30), nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    email = Column(String(40), nullable=False, unique=True)
    password = Column(String(150), nullable=False)
    is_active = Column(Boolean, nullable=False)
    is_superUser = Column(Boolean, nullable=False)
    avis = relationship('Avis', back_populates='users', cascade="all, delete-orphan")


class Avis(Base):
    __tablename__ = 'avis'
    avis_id = Column(Integer, primary_key=True, index=True)
    body = Column(Text, nullable=False)
    time_created = Column(Time(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey('users.user_id'))
    users = relationship('User', back_populates='avis')


class Otp(Base):
    pass
