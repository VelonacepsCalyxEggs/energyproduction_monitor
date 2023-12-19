import eel
import sys
import subprocess
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import json

eel.init("C:/Users/ivank/source/repos/energyproduction_monitor/appl/gui") #gotta auto detect the path...

@eel.expose
def startup():
    text = "test"
    return text

@eel.expose
def shutdownServer():
    eel._shutdown
    print('goodbye world!')
    subprocess.call("TASKKILL /F /IM chrome.exe", shell=True) # This can have serious reprecussions... and I am too lazy to fix this. Fuck chrome anyway.
    sys.exit()

@eel.expose
def locationChanger():
    return()

@eel.expose
def dataRequestYear(date,mw,kw,w):
    mw = False
    kw = False
    w = False
    
    print(date)
    stringifiedDate = date.split('-')
    year = stringifiedDate[0]
    month = stringifiedDate[1]
    day = stringifiedDate[2]
    con = psycopg2.connect(database='energydb', user='postgres', password='424212')
    cur = con.cursor()
    cur.execute(sql.SQL("SELECT SUM(kw) AS total_kw FROM energydata WHERE EXTRACT(YEAR FROM date) = %s GROUP BY DATE_TRUNC('month', date) ORDER BY DATE_TRUNC('month', date);"), [year])
    data = cur.fetchmany(12)
    cur.close()
    con.close()
    dividedData = []
    if mw == True:
        divisor = 100
        for num in data:
            dividedData.append(num / divisor)
    elif kw == True:
        divisor = 10
        for num in data:
            dividedData.append(num / divisor)
    elif w == True:
        divisor = 1
        dividedData.append(num / divisor)
    else:
        print('What the fuck?!')
        
    jsonifiedData = json.dumps(dividedData)
    return jsonifiedData

@eel.expose
def dataRequestMonth(date):
    print(date)
    stringifiedDate = date.split('-')
    year = stringifiedDate[0]
    month = stringifiedDate[1]
    day = stringifiedDate[2]
    con = psycopg2.connect(database='energydb', user='postgres', password='424212')
    cur = con.cursor()
    cur.execute(sql.SQL("SELECT kw FROM energydata WHERE DATE_TRUNC('month', date) = DATE_TRUNC('month', %s::date) AND EXTRACT(hour FROM date) = 12;"), [date])
    data = cur.fetchall()
    cur.close()
    con.close()
    jsonifiedData = json.dumps(data)
    return jsonifiedData

@eel.expose
def dataRequestDay(date):
    print(date)
    stringifiedDate = date.split('-')
    year = stringifiedDate[0]
    month = stringifiedDate[1]
    day = stringifiedDate[2]
    con = psycopg2.connect(database='energydb', user='postgres', password='424212')
    cur = con.cursor()
    cur.execute(sql.SQL("SELECT kw FROM energydata WHERE DATE_TRUNC('month', date) = DATE_TRUNC('month', %s::date) AND EXTRACT(day FROM date) = %s;"), [date,day])
    data = cur.fetchall()
    cur.close()
    con.close()
    jsonifiedData = json.dumps(data)
    return jsonifiedData




eel.start('index.html', size=(1024, 512), port=55045)