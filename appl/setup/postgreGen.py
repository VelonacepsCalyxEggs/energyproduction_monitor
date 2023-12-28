import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import random
from datetime import datetime, timedelta



dbName = 'postgres'
dbUser = 'postgres'
dbHost = '192.168.0.50'
dbPort = '5432'
dbPassword = '111LZo0l4S7dzO0PXA3KOkasw2rcMtO46hY2FbUPxS'
con = psycopg2.connect(database = dbName, user = dbUser, password = dbPassword, host=dbHost, port=dbPort)
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

try:
    cur = con.cursor()
    cur.execute(sql.SQL("CREATE DATABASE energydb"))

except Exception as e:
    print('An error occured while creating a database! ', e)

con.close()
dbName = "energydb"
con = psycopg2.connect(database = dbName, user = dbUser, password = dbPassword, host=dbHost, port=dbPort)
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
    if current_date.hour == 6:
        randomNum = random.randint(5000,7000)
    elif current_date.hour == 7:
        randomNum = random.randint(5800,7000)
    elif current_date.hour == 8:
        randomNum = random.randint(6000,7500)
    elif current_date.hour == 9:
        randomNum = random.randint(6000,7500)
    elif current_date.hour == 10:
        randomNum = random.randint(6000,7500)
    elif current_date.hour == 11:
        randomNum = random.randint(7000,7500)
    elif current_date.hour == 12:
        randomNum = random.randint(7000,8500)
    elif current_date.hour == 13:
        randomNum = random.randint(7000,8800)
    elif current_date.hour == 14:
        randomNum = random.randint(7000,8900)
    elif current_date.hour == 15:
        randomNum = random.randint(7000,8900)
    elif current_date.hour == 16:
        randomNum = random.randint(7000,9500)
    elif current_date.hour == 17:
        randomNum = random.randint(7000,10000)
    elif current_date.hour == 18:
        randomNum = random.randint(7000,10000)
    elif current_date.hour == 19:
        randomNum = random.randint(7000,10000)
    elif current_date.hour == 20:
        randomNum = random.randint(6000,8000)
    elif current_date.hour == 21:
        randomNum = random.randint(6000,7500)
    elif current_date.hour == 22:
        randomNum = random.randint(5000,6300)
    elif current_date.hour == 23:
        randomNum = random.randint(2000,3500)
    elif current_date.hour == 00:
        randomNum = random.randint(0,2000)
    elif current_date.hour == 1:
        randomNum = random.randint(0,1800)
    elif current_date.hour == 2:
        randomNum = random.randint(0,1800)
    elif current_date.hour == 3:
        randomNum = random.randint(0,1800)
    elif current_date.hour == 4:
        randomNum = random.randint(100,2800)
    elif current_date.hour == 5:
         randomNum = random.randint(1000,3800)
    else:
        print('я ебалай!')

    current_date += timedelta(hours=1)
    cur.execute("INSERT INTO ENERGYDATA (kw, date) VALUES (%s, %s)", [randomNum,current_date])
    print('inserted ', randomNum)
try:
    cur.execute(sql.SQL("CREATE TABLE ENERGYPRODUCTIONDATA (id serial PRIMARY KEY, kw integer, date timestamp);"))
except Exception as e:
    print("An error occured while creating the table! ", e)
start_date2 = datetime(year=2019, month=1, day=1, hour=0, minute=0, second=0)
end_date2 = datetime(year=2023, month=12, day=31, hour=23, minute=59, second=59)
current_date2 = start_date2
while current_date2 <= end_date2:
    if current_date2.hour == 6:
        randomNum = random.randint(5000,7000)
    elif current_date2.hour == 7:
        randomNum = random.randint(5800,7000)
    elif current_date2.hour == 8:
        randomNum = random.randint(6000,7500)
    elif current_date2.hour == 9:
        randomNum = random.randint(6000,7500)
    elif current_date2.hour == 10:
        randomNum = random.randint(6000,7500)
    elif current_date2.hour == 11:
        randomNum = random.randint(7000,7500)
    elif current_date2.hour == 12:
        randomNum = random.randint(7000,8500)
    elif current_date2.hour == 13:
        randomNum = random.randint(7000,8800)
    elif current_date2.hour == 14:
        randomNum = random.randint(7000,8900)
    elif current_date2.hour == 15:
        randomNum = random.randint(7000,8900)
    elif current_date2.hour == 16:
        randomNum = random.randint(7000,9500)
    elif current_date2.hour == 17:
        randomNum = random.randint(7000,10000)
    elif current_date2.hour == 18:
        randomNum = random.randint(7000,10000)
    elif current_date2.hour == 19:
        randomNum = random.randint(7000,10000)
    elif current_date2.hour == 20:
        randomNum = random.randint(6000,8000)
    elif current_date2.hour == 21:
        randomNum = random.randint(6000,7500)
    elif current_date2.hour == 22:
        randomNum = random.randint(5000,6300)
    elif current_date2.hour == 23:
        randomNum = random.randint(2000,3500)
    elif current_date2.hour == 00:
        randomNum = random.randint(0,2000)
    elif current_date2.hour == 1:
        randomNum = random.randint(0,1800)
    elif current_date2.hour == 2:
        randomNum = random.randint(0,1800)
    elif current_date2.hour == 3:
        randomNum = random.randint(0,1800)
    elif current_date2.hour == 4:
        randomNum = random.randint(100,2800)
    elif current_date2.hour == 5:
         randomNum = random.randint(1000,3800)
    else:
        print('я ебалай!')
    current_date2 += timedelta(hours=1)
    cur.execute("INSERT INTO ENERGYPRODUCTIONDATA (kw, date) VALUES (%s, %s)", [randomNum,current_date2])
    print('inserted ', randomNum)
try:
    cur.execute(sql.SQL("CREATE TABLE users (id serial PRIMARY KEY, login text UNIQUE, password text, role text);"))
    cur.execute(sql.SQL("INSERT INTO users (login, password, role) VALUES ('admin', 4242, 'admin');"))
except Exception as e:
    print('уже есть... ', e)


