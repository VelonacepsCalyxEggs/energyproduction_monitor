import eel
import sys
import subprocess
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import json
from datetime import datetime
import os
import hashlib

script_path = os.path.abspath(sys.argv[0])
script_directory = os.path.dirname(script_path)
parent_directory = os.path.dirname(script_directory)
eel.init(parent_directory + "\\appl\\gui") 

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

@eel.expose
def configEdit(username,ip,port,password):
    data = {
    "user": username,
    "ip": ip,
    "port": port,
    "password": password
    }
    print(ip)
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\config\\config.json'
    print(jsonPath)
    try:
        con = psycopg2.connect(host=ip, port=port, database='energydb', user=username, password=password)
        con.close()
        e = 42
        exception1 = e
    except Exception as e:
        print('Config invalid!!! ', e)
        exception1 = json.dumps(str(e))
    with open(jsonPath, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print('config changed.')
    
    return(exception1)

@eel.expose
def saveDataForAnalysis(dataCons,DataProd,labels):
    data = {
    "consumption": dataCons,
    "production": DataProd,
    "labels": labels
    }
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\files\\data.json'
    print(jsonPath)
    with open(jsonPath, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print('data saved for analysis')
    return()

@eel.expose
def dataAnalysis():
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\files\\data.json'
    print(jsonPath)
    with open(jsonPath, 'r') as json_file:
        data = json.load(json_file)
    consumption = []
    production = []
    effectiveness = []
    i = 0
    for num in data['production']:
        efficiency = (float(num) / float(data['consumption'][i])) * 100
        effectiveness.append(int(efficiency))
        i = i + 1
    print(effectiveness) 
    effectivenessAnomaly = []
    effectivenessAnomalyLabelNumber = []
    i = 0
    for num in effectiveness:
        if num < 95:
            effectivenessAnomaly.append(num)
            effectivenessAnomalyLabelNumber.append(i) 
        i = i + 1

    print(effectivenessAnomaly)
    print(effectivenessAnomalyLabelNumber)
    dateformat = len(data['labels'])
    print(dateformat)
    jsonData = {
        'effectiveness': effectiveness,
        'effectivenessAnomaly': effectivenessAnomaly,
        'effectivenessAnomalyLabel': effectivenessAnomalyLabelNumber,
        'dateformat': dateformat
    }
    jsonifiedData = json.dumps(jsonData)
    print(jsonifiedData)
    return jsonifiedData

@eel.expose
def login(login,passwordUser):
    if len(passwordUser) == 64:
        print('logincheck')
    else:
        passwordUser = hashlib.sha256(passwordUser.encode('UTF-8'))
        passwordUser = passwordUser.hexdigest()
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\config\\config.json'
    with open(jsonPath) as json_file:
        SQLData = json.load(json_file)
    ip = SQLData['ip']
    port = SQLData['port']
    username = SQLData['user']
    password = SQLData['password']

    print(passwordUser," ",login)
    con = psycopg2.connect(host=ip, port=port, database='energydb', user=username, password=password)
    cur = con.cursor()
    cur.execute(sql.SQL("SELECT login,password,role FROM users WHERE password = %s and login = %s"), [passwordUser, login])
    data = cur.fetchall()
    con.close()
    print(data)
    jsonPath = parent_directory + '\\appl\\gui\\scripts\\userdata.json'
    if len(data) > 0:
        loggedin = 1
        
    elif len(data) == 0:
        loggedin = 0
    else: 
        loggedin = 0
    if str(data) == '[]':
        dataJson = {
             'password': '11111111111111111111111111111111111111111111111111111111111111111',
             'login': 'fuck'
        }
        with open(jsonPath, 'w') as json_file:
            json.dump(dataJson, json_file, indent=4)
        print('le pizdon')
    else:
        print('balls')
        dataJson = {
             'password': data[0][0],
             'login': data[0][1],
             'role': data[0][2]
        }
        with open(jsonPath, 'w') as json_file:
            json.dump(dataJson, json_file, indent=4)
    return loggedin

@eel.expose
def logout():
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\gui\\scripts\\userdata.json'
    dataJson = {
            'password': '11111111111111111111111111111111111111111111111111111111111111111',
            'login': 'fuck'
        }
    with open(jsonPath, 'w') as json_file:
        json.dump(dataJson, json_file, indent=4)
    return

@eel.expose 
def createNewUser(accLogin,accPassword):
    accPassword = hashlib.sha256(accPassword.encode('UTF-8'))
    accPassword = accPassword.hexdigest()
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\config\\config.json'
    with open(jsonPath) as json_file:
        SQLData = json.load(json_file)
    ip = SQLData['ip']
    port = SQLData['port']
    username = SQLData['user']
    password = SQLData['password']
    con = psycopg2.connect(host=ip, port=port, database='energydb', user=username, password=password)
    cur = con.cursor()
    try:
        cur.execute(sql.SQL("INSERT INTO users (login,password,role) VALUES (%s, %s, 'manager')"), [accLogin, accPassword])
        e = 'good'
        print('Excecuted query with password and login: ', accPassword, accLogin)
    except Exception as e:
        print('Error ', e)
    con.commit()
    con.close()
    return '123'

@eel.expose
def removeUser(accLogin):
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)
    parent_directory = os.path.dirname(script_directory)
    jsonPath = parent_directory + '\\appl\\config\\config.json'
    with open(jsonPath) as json_file:
        SQLData = json.load(json_file)
    ip = SQLData['ip']
    port = SQLData['port']
    username = SQLData['user']
    password = SQLData['password']
    con = psycopg2.connect(host=ip, port=port, database='energydb', user=username, password=password)
    cur = con.cursor()
    try:
        cur.execute(sql.SQL("DELETE FROM users WHERE login = %s"), [accLogin])
        e = 'good'
        print('Removed account with login: ', accLogin)
    except Exception as e:
        print('Error ', e)
    con.commit()
    con.close()
    return 
eel.start('login.html', size=(1920, 1080), port=55045)