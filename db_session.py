#! /usr/bin/python

import sqlalchemy as sa
from sqlalchemy import *
from sqlalchemy.dialects.mysql import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base as dec
import bcrypt
	#from setting import Base
	#from setting import ENGINE
import urllib as ul
import sys
import tkinter.messagebox as tm
import time
from simplebot_test import TkinterGUIExample

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
		Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
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
		#self.pwd = bcrypt.hashpw(pwd.encode('utf8'), bcrypt.gensalt())
		#self.query_result = self.session.query(Query_table.account, Query_table.password).filter(Query_table.account == usr).filter(Query_table.password == self.pwd).count()
		#print(self.query_result)
		self.text_usr = usr
		self.pwd = bcrypt.hashpw(pwd.encode('utf8'), bcrypt.gensalt())
		self.query_result = self.session.query(Query_table.account).filter(Query_table.account == self.text_usr).count()
		if self.query_result == 1:
			 #if bcrypt.hashpw(pwd.encode, self.pwd) == self.pwd: #should be modified.
			tm.showinfo("Login info", " Welcome {}".format(self.text_usr))
			time.sleep(1.5)
			self.botwindow = TkinterGUIExample()
			self.botwindow.display_usr(self.text_usr)
			self.botwindow.greeting_msg() 
			self.botwindow.mainloop()
			 #else:
			 #tm.showerror("Login error", "Incorrect username. Please input again correctly")
		else:
			tm.showerror("Login error", "Incorrect username. Please input again correctly")
		self.session.close()


	#@classmethod
	#def User_info(cls):
	#	display_user = cls(auth_session.text_usr)
	#	print(display_user)


class Userregister(DB_session):
	def __init__(self):
		super().__init__()

	def register(self, newusr, newpwd, newemail):
		#self.id = Query_table(id = 200)
		self.newusr = newusr
		self.newpwd =  bcrypt.hashpw(newpwd.encode('utf8'), bcrypt.gensalt())
		self.newemail = newemail
		self.reg_data = Query_table(account = self.newusr, password = self.newpwd, email = self.newemail)
		self.session.add(self.reg_data)
		self.session.commit() #here
		self.usercount = self.session.query(Query_table.account, Query_table.password).filter(Query_table.account == self.newusr).filter(Query_table.password == self.newpwd).filter(Query_table.password == self.newpwd).count()
		if  self.usercount == 1:
			tm.showinfo("User {} has been successfully created".format(self.newusr))
		else:
			tm.showerror("Registeration error happened!!")

class Session_close(DB_session):
	def __init__(self):
		super().__init__()

	def auth_close(self):
		self.session.close()
		self.session_evidence = self.session
		if self.session_evidence == "":
			tm.showinfo("Thank you for coming today, currently I have closed session{}.".format(self.session))
		else:
			tm.showinfo("Umm, something wrong with closing session. I still have your session strangely{}.".format(self.session))


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

