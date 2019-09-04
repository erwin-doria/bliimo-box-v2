from time import time
from datetime import datetime

def timestampNow():
    return datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')

def dateNow():
    return datetime.today().strftime('%Y-%m-%d')

def dateFormat(date, format): 
    return datetime.strptime(date, format).date()

def dateDiff(date1, date2):
    return (date1 - date2).days