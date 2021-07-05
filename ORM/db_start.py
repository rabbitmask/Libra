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


def db_start():
    conn = sqlite3.connect('Libra.db')
    c = conn.cursor()
    res = c.execute('select * from sqlite_master')
    dblist=[]
    for i in res:
        if i:
            dblist.append(i[1])
    if 'webdata' not in dblist:
        c.execute('CREATE TABLE "webdata" (  "id" INTEGER NOT NULL,  "url" TEXT,  "data" TEXT,  "datetime" TEXT,  PRIMARY KEY ("id"));')
    if 'hiddenlink_rules' not in dblist:
        c.execute('CREATE TABLE "hiddenlink_rules" (  "id" INTEGER NOT NULL,  "re" TEXT,  PRIMARY KEY ("id"));')
    conn.commit()
    conn.close()