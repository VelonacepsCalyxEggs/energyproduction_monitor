import eel
import sys
import subprocess
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import json
from datetime import datetime
import os

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
def dataRequestYear(date,measure):
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\config\\config.json'
    with open(jsonPath) as json_file:
        SQLData = json.load(json_file)
    ip = SQLData['ip']
    port = SQLData['port']
    user = SQLData['user']
    password = SQLData['password']
    print(SQLData)
    con = psycopg2.connect(host=ip, port=port, database='energydb', user=user, password=password)
    print(date)
    stringifiedDate = date.split('-')
    year = stringifiedDate[0]
    month = stringifiedDate[1]
    day = stringifiedDate[2]
    cur = con.cursor()
    cur.execute(sql.SQL("SELECT SUM(kw) AS total_kw FROM energydata WHERE EXTRACT(YEAR FROM date) = %s GROUP BY DATE_TRUNC('month', date) ORDER BY DATE_TRUNC('month', date);"), [year])
    data = cur.fetchmany(12)
    cur.close()
    con.close()
    dividedData = []
    if measure == 'Watts':
        divisor = 1
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('Watts')
    elif measure == 'KiloWatts':
        divisor = 1000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('KiloWatts')
    elif measure == 'MegaWatts':
        divisor = 10000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('MegaWatts')
    else:
        print('What the fuck?!')
        dividedData = data
        
    jsonifiedData = json.dumps(dividedData)
    return jsonifiedData

@eel.expose
def dataRequestMonth(date,measure):
    print(date)
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\config\\config.json'
    with open(jsonPath) as json_file:
        SQLData = json.load(json_file)
    ip = SQLData['ip']
    port = SQLData['port']
    user = SQLData['user']
    password = SQLData['password']
    con = psycopg2.connect(host=ip, port=port, database='energydb', user=user, password=password)
    stringifiedDate = date.split('-')
    year = stringifiedDate[0]
    month = stringifiedDate[1]
    day = stringifiedDate[2]
    cur = con.cursor()
    cur.execute(sql.SQL("SELECT kw FROM energydata WHERE DATE_TRUNC('month', date) = DATE_TRUNC('month', %s::date) AND EXTRACT(hour FROM date) = 12;"), [date])
    data = cur.fetchall()
    cur.close()
    con.close()
    dividedData = []
    if measure == 'Watts':
        divisor = 1
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('Watts')
    elif measure == 'KiloWatts':
        divisor = 1000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('KiloWatts')
    elif measure == 'MegaWatts':
        divisor = 10000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('MegaWatts')
    else:
        print('What the fuck?!')
        dividedData = data
    jsonifiedData = json.dumps(dividedData)
    return jsonifiedData

@eel.expose
def dataRequestDay(date,measure):
    print(date)
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\config\\config.json'
    with open(jsonPath) as json_file:
        SQLData = json.load(json_file)
    ip = SQLData['ip']
    port = SQLData['port']
    user = SQLData['user']
    password = SQLData['password']
    con = psycopg2.connect(host=ip, port=port, database='energydb', user=user, password=password)
    stringifiedDate = date.split('-')
    year = stringifiedDate[0]
    month = stringifiedDate[1]
    day = stringifiedDate[2]
    cur = con.cursor()
    cur.execute(sql.SQL("SELECT kw FROM energydata WHERE DATE_TRUNC('month', date) = DATE_TRUNC('month', %s::date) AND EXTRACT(day FROM date) = %s;"), [date,day])
    data = cur.fetchall()
    cur.close()
    con.close()
    dividedData = []
    if measure == 'Watts':
        divisor = 1
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('Watts')
    elif measure == 'KiloWatts':
        divisor = 1000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('KiloWatts')
    elif measure == 'MegaWatts':
        divisor = 10000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('MegaWatts')
    else:
        print('What the fuck?!')
        dividedData = data
    jsonifiedData = json.dumps(dividedData)
    return jsonifiedData

@eel.expose
def dataRequestYearPeriod(measure):
    current_year = datetime.now().year
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\config\\config.json'
    with open(jsonPath) as json_file:
        SQLData = json.load(json_file)
    ip = SQLData['ip']
    port = SQLData['port']
    user = SQLData['user']
    password = SQLData['password']
    con = psycopg2.connect(host=ip, port=port, database='energydb', user=user, password=password)
    cur = con.cursor()
    cur.execute(sql.SQL("SELECT SUM(kw) AS year_total_kilowatts FROM energydata GROUP BY EXTRACT(YEAR FROM date) ORDER BY EXTRACT(YEAR FROM date) ASC;"))
    data = cur.fetchall()
    cur.close()
    con.close()
    dividedData = []
    if measure == 'Watts':
        divisor = 1
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('Watts')
    elif measure == 'KiloWatts':
        divisor = 1000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('KiloWatts')
    elif measure == 'MegaWatts':
        divisor = 10000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('MegaWatts')
    else:
        print('What the fuck?!')
        dividedData = data
    jsonifiedData = json.dumps(dividedData)
    print(jsonifiedData)
    return jsonifiedData

@eel.expose
def configEdit(username,ip,port,password):
    data = {
    "user": username,
    "ip": ip,
    "port": port,
    "password": password
    }
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\config\\config.json'
    print(jsonPath)
    with open(jsonPath, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print('config changed.')
    return()

@eel.expose
def dataRequestYearProduction(date,measure):
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\config\\config.json'
    with open(jsonPath) as json_file:
        SQLData = json.load(json_file)
    ip = SQLData['ip']
    port = SQLData['port']
    user = SQLData['user']
    password = SQLData['password']
    print(SQLData)
    con = psycopg2.connect(host=ip, port=port, database='energydb', user=user, password=password)
    print(date)
    stringifiedDate = date.split('-')
    year = stringifiedDate[0]
    month = stringifiedDate[1]
    day = stringifiedDate[2]
    cur = con.cursor()
    cur.execute(sql.SQL("SELECT SUM(kw) AS total_kw FROM energyproductiondata WHERE EXTRACT(YEAR FROM date) = %s GROUP BY DATE_TRUNC('month', date) ORDER BY DATE_TRUNC('month', date);"), [year])
    data = cur.fetchmany(12)
    cur.close()
    con.close()
    dividedData = []
    if measure == 'Watts':
        divisor = 1
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('Watts')
    elif measure == 'KiloWatts':
        divisor = 1000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('KiloWatts')
    elif measure == 'MegaWatts':
        divisor = 10000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('MegaWatts')
    else:
        print('What the fuck?!')
        dividedData = data
        
    jsonifiedData = json.dumps(dividedData)
    return jsonifiedData

@eel.expose
def dataRequestMonthProduction(date,measure):
    print(date)
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\config\\config.json'
    with open(jsonPath) as json_file:
        SQLData = json.load(json_file)
    ip = SQLData['ip']
    port = SQLData['port']
    user = SQLData['user']
    password = SQLData['password']
    con = psycopg2.connect(host=ip, port=port, database='energydb', user=user, password=password)
    stringifiedDate = date.split('-')
    year = stringifiedDate[0]
    month = stringifiedDate[1]
    day = stringifiedDate[2]
    cur = con.cursor()
    cur.execute(sql.SQL("SELECT kw FROM energyproductiondata WHERE DATE_TRUNC('month', date) = DATE_TRUNC('month', %s::date) AND EXTRACT(hour FROM date) = 12;"), [date])
    data = cur.fetchall()
    cur.close()
    con.close()
    dividedData = []
    if measure == 'Watts':
        divisor = 1
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('Watts')
    elif measure == 'KiloWatts':
        divisor = 1000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('KiloWatts')
    elif measure == 'MegaWatts':
        divisor = 10000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('MegaWatts')
    else:
        print('What the fuck?!')
        dividedData = data
    jsonifiedData = json.dumps(dividedData)
    return jsonifiedData

@eel.expose
def dataRequestDayProduction(date,measure):
    print(date)
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\config\\config.json'
    with open(jsonPath) as json_file:
        SQLData = json.load(json_file)
    ip = SQLData['ip']
    port = SQLData['port']
    user = SQLData['user']
    password = SQLData['password']
    con = psycopg2.connect(host=ip, port=port, database='energydb', user=user, password=password)
    stringifiedDate = date.split('-')
    year = stringifiedDate[0]
    month = stringifiedDate[1]
    day = stringifiedDate[2]
    cur = con.cursor()
    cur.execute(sql.SQL("SELECT kw FROM energyproductiondata WHERE DATE_TRUNC('month', date) = DATE_TRUNC('month', %s::date) AND EXTRACT(day FROM date) = %s;"), [date,day])
    data = cur.fetchall()
    cur.close()
    con.close()
    dividedData = []
    if measure == 'Watts':
        divisor = 1
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('Watts')
    elif measure == 'KiloWatts':
        divisor = 1000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('KiloWatts')
    elif measure == 'MegaWatts':
        divisor = 10000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('MegaWatts')
    else:
        print('What the fuck?!')
        dividedData = data
    jsonifiedData = json.dumps(dividedData)
    return jsonifiedData

@eel.expose
def dataRequestYearPeriodProduction(measure):
    current_year = datetime.now().year
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\config\\config.json'
    with open(jsonPath) as json_file:
        SQLData = json.load(json_file)
    ip = SQLData['ip']
    port = SQLData['port']
    user = SQLData['user']
    password = SQLData['password']
    con = psycopg2.connect(host=ip, port=port, database='energydb', user=user, password=password)
    cur = con.cursor()
    cur.execute(sql.SQL("SELECT SUM(kw) AS year_total_kilowatts FROM energyproductiondata GROUP BY EXTRACT(YEAR FROM date) ORDER BY EXTRACT(YEAR FROM date) ASC;"))
    data = cur.fetchall()
    cur.close()
    con.close()
    dividedData = []
    if measure == 'Watts':
        divisor = 1
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('Watts')
    elif measure == 'KiloWatts':
        divisor = 1000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('KiloWatts')
    elif measure == 'MegaWatts':
        divisor = 10000
        for num in data:
            dividedData.append(int(num[0]) / divisor)
        print('MegaWatts')
    else:
        print('What the fuck?!')
        dividedData = data
    jsonifiedData = json.dumps(dividedData)
    print(jsonifiedData)
    return jsonifiedData



eel.start('index.html', size=(1024, 512), port=55045)