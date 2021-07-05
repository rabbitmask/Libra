#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _    
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   < 
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
                                                    
'''
import difflib
from ORM.db_comparer import save_data, get_data


def comparer(url,res):
    lastres = get_data(url)

    save_data(url,res)
    if lastres:
        if res==lastres:
            # print("大哥贼牛批，网站稳如磐石")
            pass
        else:
            d = difflib.Differ()
            diff = d.compare(res.splitlines(), lastres.splitlines())
            resdiff=[]
            for i in diff:
                if i[0] == '+' or i[0] == '-' or i[0] == '?':
                    resdiff.append(i)
            # print("大哥，咱好像被日了，详细篡改点已生成报告")
            pass
            return resdiff

if __name__ == '__main__':
    comparer('http://127.0.0.1')