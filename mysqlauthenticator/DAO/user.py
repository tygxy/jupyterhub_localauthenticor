# coding:utf-8
from sqlalchemy import Column, String, Integer 
from mysqlauthenticator.DAO.base import Base


class User(Base):

	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	username = Column(String(64), nullable=False, unique=True)
	password = Column(String(64), nullable=False)
