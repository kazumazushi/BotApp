#! /usr/bin/python
import sys
from sqlalchemy.ext.declarative import declarative_base as dec
import sqlalchemy as sa
from setting import Base
from setting import ENGINE

class User(Base):
    """
    user model
    """
    __tablename__ = 'accepted'
    id = sa.Column('id', Integer, auto_increment, primary_key = True)
    account = sa.Column('account', Varchar(255))
    passwoed = sa.Column('password', Varchar(255))
    email = sa.Column('email', Varchar(255))

def main(args):
    """
    main function
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)

