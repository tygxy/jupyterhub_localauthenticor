# coding:utf-8

import sys
from sqlalchemy import Column, String, Integer 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash,generate_password_hash

Base = declarative_base()

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, unique=True)
    password = Column(String(64), nullable=False)

    def set_password(self, passwd):
        self.password = generate_password_hash(passwd)

    def check_password(self, passwd):
        return check_password_hash(self.password, passwd)

class UserManager(object):

	"""docstring for UserManager"""

	username = None
	password = None
	db_url = "mysql+mysqlconnector://root:<password>@<ip>:3306/<table_name>"

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def add_user(self):
		new_user = User(username = self.username)
		new_user.set_password(self.password)

		engine = create_engine(self.db_url)
		smaker = sessionmaker(bind=engine)
		session = smaker() 
		session.add(new_user)
		session.commit()
		session.close()
		print("add user " + self.username + " success !")


if __name__ == "__main__":

	username = sys.argv[1]
	password = sys.argv[2]
	um = UserManager(username, password)
	um.add_user()
    
		
		

