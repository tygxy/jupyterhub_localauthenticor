# coding:utf-8
from sqlalchemy import Column, String, Integer 
from mysqlauthenticator.DAO.base import Base
from werkzeug.security import check_password_hash,generate_password_hash


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, unique=True)
    password = Column(String(64), nullable=False)

    def set_password(self, passwd):
        self.password = generate_password_hash(passwd)

    def check_password(self, passwd):
        return check_password_hash(self.password, passwd)
