import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import random
from datetime import datetime, timedelta



dbName = 'postgres'
dbUser = 'postgres'
con = psycopg2.connect(database = dbName, user = dbUser, password = 424212)
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

try:
    cur = con.cursor()
    cur.execute(sql.SQL("CREATE DATABASE energydb"))

except Exception as e:
    print('An error occured while creating a database! ', e)

con.close()
dbName = "energydb"
con = psycopg2.connect(database = 'energydb', user = dbUser, password = 424212)
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
try:
    #cur.execute(sql.SQL("CREATE TABLE ENERGYDATA (id serial PRIMARY KEY, kw integer, date TIMESTAMPTZ NOT NULL DEFAULT NOW());"))
    cur.execute(sql.SQL("CREATE TABLE ENERGYDATA (id serial PRIMARY KEY, kw integer, date timestamp);"))
except Exception as e:
    print("An error occured while creating the table! ", e)

start_date = datetime(year=2019, month=1, day=1, hour=0, minute=0, second=0)
end_date = datetime(year=2023, month=12, day=31, hour=23, minute=59, second=59)
current_date = start_date
while current_date <= end_date:
    randomNum = random.randint(1,10000)
    current_date += timedelta(hours=1)
    cur.execute("INSERT INTO ENERGYDATA (kw, date) VALUES (%s, %s)", [randomNum,current_date])
    print('inserted ', randomNum)

