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

##session

engine = sa.create_engine("mysql+pymysql://root:root@localhost/auth_info?charset=utf8", echo=False, encoding='utf8', max_overflow=10, pool_size=6)
engine.connect()
Base = dec(bind=engine)
metadata = MetaData(bind=engine)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()
#session = Session() 
#session = scoped_session(sessionmaker(autocommit = False, autoflush = False, bind = engine))
if Session == "":
	print("no session and try it again")
else:
	print("having session and the session is {}".format(session))

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


metadata.create_all(engine)
#session.add(Query_table(id=10, account='Suzuki', password='ls', email='ll'))
#session.commit()
#query_result = session.query(Query_table).all()
query_result = session.query(Query_table.id, Query_table.account, Query_table.password, Query_table.email).all()
print(query_result)
#print (responses)
session.close()


#for response in responses:
#	print(response)


"""

if __name__=='__main__':
	conn = DB_state()
	conn.db_communication()
	mapper = Query_table():
	users = state(db_account).all()
	for user in users:
		print(db_account)

"""

