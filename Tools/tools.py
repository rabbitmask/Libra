#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import datetime


def getDate():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    print(getDate())