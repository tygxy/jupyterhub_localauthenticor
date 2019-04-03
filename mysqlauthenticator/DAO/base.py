# coding:utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = None
smaker = None


def init(url):
	global engine, smaker, Base, session

	engine = create_engine(url)
	smaker = sessionmaker(bind=engine)
	session = smaker()

	return session
