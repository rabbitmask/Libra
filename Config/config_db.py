#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import sqlite3

def get_connection1():
    connection = sqlite3.connect('Libra.db')
    # connection = sqlite3.connect('../Libra.db')
    return connection


if __name__ == '__main__':
    pass