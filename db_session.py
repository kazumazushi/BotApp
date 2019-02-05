#! /usr/bin/python

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base as dec
#from setting import Base
#from setting import ENGINE
import urllib as ul

##session

class DB_state:
	def __init__(self):
		self.engine = sa.create_engine("mysql+pymysql://root:root@localhost/auth_info?charset=utf8", echo=False, encoding='utf8-', max_overflow=10, pool_size=6)
		self.engine.connect()

	def db_communication(self):
		session = scoped_session(sessionmaker(autocommit = False, autoflush = False, bind = self.engine))
		if session == "":
			print("no session and try it again")
		else:
			print("having session and the session is {}".format(session))

	def declaration(self):
		Base = declarative_base():
		Base.query = session.query_property()




## model

class Query_table(Base):

	def usertable(self):
		__tablename__ = 'accepted'
		id = sa.Column('id', Integer, auto_increment, primary_key = True)
		self.db_account = sa.Column('account', Varchar(255))
		self.db_passwoed = sa.Column('password', Varchar(255))
		self.db_email = sa.Column('email', Varchar(255))

"""
	def query_auth(self,,):
		result = self.session.query(Test).filter(Test.id == id).all()
		for row in result:
			print(row.id, row.name)
"""

	def main(args):
		Base.metadata.create_all(bind=self.engine)

	def db_query_user(self):
		pass

	def db_query_password(self):
		pass



if __name__=='__main__':
	conn = DB_state()
	conn.db_communication()
	users = session.query(self.db_account).all()
	for user in users:
		print(self.db_account)

