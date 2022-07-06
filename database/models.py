from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    unique_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    avis = relationship('avis', back_populates='user')


class Avis(Base):
    __tablename__ = 'avis'
    unique_id = Column(Integer, primary_key=True, index=True)
    body = Column(Text, nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey('user.unique_id'))
    user = relationship('user', back_populates='avis')
