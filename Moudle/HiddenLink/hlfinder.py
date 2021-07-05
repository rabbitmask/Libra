#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _    
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   < 
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
                                                    
'''
import re
import sqlite3

from ORM.db_hiddenlink import get_re

conn = sqlite3.connect('Libra.db')



def hlfind(res):
    rules = []
    host = True
    re_rules_list = get_re()
    for re_rules in re_rules_list:
        result = re.findall(r'{}'.format(re_rules[0]), res, re.S)
        if result != []:
            rules.append(re_rules[0])
            host = False
    if host == False:
        return rules
    else:
        pass


if __name__ == '__main__':
    hlfind("http://127.0.0.1")