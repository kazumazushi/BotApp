#! /usr/bin/python

import sqlalchemy as sa

url = sa.create_engine("mysql+pymysql://root:root@localhost/auth_info?charset=utf8", echo=True, encoding='utf-8', max_overflow=10, pool_size=6)
url.connect()
print(url)

#engine = sa.create_engine(url, echo=True)

#engine.execute('DROP TABLE zoo')
#engine.execute('CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)')

# SQL文に「?」が使用できないので、代わりに「%s」を使用
#ins = "INSERT INTO zoo (critter, count, damages) VALUES (%s, %s, %s)"
#engine.execute(ins, "あひる", 10, 0.0)
#engine.execute(ins, "くま", 2, 1000.0)
#engine.execute(ins, "いたち", 1, 2000.0)
#rows = engine.execute('SELECT * FROM zoo')

