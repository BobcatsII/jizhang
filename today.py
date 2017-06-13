#-*- coding:utf-8 -*-
"""今天的日期"""
def today():
    import time as t
    import datetime as dt
    today=[t.localtime()[i] for i in range(3)]
    today_date=dt.date(today[0],today[1],today[2])
    date=today_date.isoformat()
    return date

if __name__=='__main__':
    today()
