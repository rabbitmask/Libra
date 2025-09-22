#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from Config.config_db import  get_connection1

def rulesnum():
    res={}

    connection = get_connection1()
    cursor=connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM `blacklink_rules`;")
    for i in cursor.fetchall():
        res['blacklink_rules_num']=i[0]


    connection = get_connection1()
    cursor=connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM `hacklink_rules`;")
    for i in cursor.fetchall():
        res['hacklink_rules_num']=i[0]

    connection = get_connection1()
    cursor=connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM `violativelink_rules`;")
    for i in cursor.fetchall():
        res['violativelink_rules_num']=i[0]
    res['cmslist']=1379
    return res

def get_blacklink_rules():
    res=[]
    connection = get_connection1()
    cursor=connection.cursor()
    cursor.execute("SELECT re,mark FROM `blacklink_rules`;")
    for i in cursor.fetchall():
        res.append(i)
    return res

def get_backdoor_rules():
    res=[]
    connection = get_connection1()
    cursor=connection.cursor()
    cursor.execute("SELECT re,mark FROM `backdoor_rules`;")
    for i in cursor.fetchall():
        res.append(i)
    return res

def get_backdoor_paths():
    res=[]
    connection = get_connection1()
    cursor=connection.cursor()
    cursor.execute("SELECT path FROM `backdoor_paths`;")
    for i in cursor.fetchall():
        res.append(i[0])
    return res

def get_violativelink_rules():
    res=[]
    connection = get_connection1()
    cursor=connection.cursor()
    cursor.execute("SELECT re,mark FROM `violativelink_rules`;")
    for i in cursor.fetchall():
        res.append(i)
    return res

def getwhiteips():
    res=[]
    connection = get_connection1()
    cursor=connection.cursor()
    cursor.execute("SELECT domain FROM `whiteips`;")
    for i in cursor.fetchall():
        res.append(i[0])
    return res

if __name__ == '__main__':
    print(getwhiteips())