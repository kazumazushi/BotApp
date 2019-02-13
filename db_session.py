#! /usr/bin/python

import sqlalchemy as sa
from sqlalchemy import *
from sqlalchemy.dialects.mysql import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base as dec
	#from setting import Base
	#from setting import ENGINE
import urllib as ul
import sys
import tkinter.messagebox as tm
	#from  login import Loginwindow

##DB_Session Management:
class DB_engine():
	def __init__(self):
		engine = sa.create_engine("mysql+pymysql://root:root@localhost/auth_info?charset=utf8", echo=False, encoding='utf8', max_overflow=10, pool_size=6)
		self.engine = engine.connect()

	#		Base = dec(bind=engine)
	#		metadata = MetaData(bind=engine)
			
class DB_session(DB_engine):
	def __init__(self):
		super().__init__()
		Session = sessionmaker(autocommit=True, autoflush=False, bind=self.engine)
		self.session = Session()
		metadata = MetaData(bind=self.engine)
		if self.session == "":
			print("no session and try it again")
		else:
			print("having session and the session is {}".format(self.session))


class Userquery(DB_session):
	def __init__(self):
		super().__init__()

	def auth_session(self, usr, pwd):
		self.query_result = self.session.query(Query_table.account, Query_table.password).filter(Query_table.account == usr).filter(Query_table.password == pwd).count()
		#print(self.query_result)
		if self.query_result == 1:
			#tm.showinfo("Login info", " Welcome {}".format(usr))
			print("Login info", " Welcome {}".format(usr) , "!!")
		else:
			#tm.showerror("Login error", "Incorrect username")
			print("Login error", "Incorrect username")
		self.session.close()

#Base = dec(bind=engine)
Base = dec()
class Query_table(Base):
	__tablename__ = 'accepted'
	id = sa.Column('id',Integer, autoincrement = True, primary_key = True)
	account = sa.Column('account', VARCHAR(255))
	password = sa.Column('password',VARCHAR(255))
	email = sa.Column('email', VARCHAR(255))

class Query_table2(Base):
	__tablename__ = 'testing'
	id = sa.Column('id',Integer, autoincrement = True, primary_key = True)
	account = sa.Column('account', VARCHAR(255))
	password = sa.Column('password',VARCHAR(255))
	email = sa.Column('email', VARCHAR(255))


if __name__=='__main__':
	test = Userquery()
	test.auth_session("Suzuki", "ls")

