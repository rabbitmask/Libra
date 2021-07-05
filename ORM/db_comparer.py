#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _    
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   < 
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
                                                    
'''
import sqlite3

from Tools.tools import getDate



def save_data(url,data):
    conn = sqlite3.connect('Libra.db')
    c = conn.cursor()
    c.execute('INSERT INTO "webdata" (url,data,datetime) VALUES (?,?,?);',[url,data,getDate()])
    conn.commit()
    conn.close()

def get_data(url):
    conn = sqlite3.connect('Libra.db')
    c = conn.cursor()
    res=c.execute('SELECT data FROM  "webdata" WHERE url = ? ORDER BY id DESC LIMIT 1;',[url])
    res=list(res)
    if res:
        return res[0][0]
    conn.close()


if __name__ == '__main__':
    print(get_data('111'))