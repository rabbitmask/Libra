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

import requests
from multiprocessing import Pool, Manager
from Config.config_requests import headers

file_type_black=['.css','.jpg','png','bmp','.gif','.zip','.rar']

def GetData(url):
    try:
        r = requests.get(url, headers=headers, timeout=5)
        r.encoding = 'utf-8'
        return r.status_code,r.text
    except(requests.exceptions.ReadTimeout,requests.exceptions.ConnectTimeout,requests.exceptions.ConnectionError):
        return 'Timeout','Timeout'


def crawler_api(url):
    if isinstance(url, str):
        out_link=[]
        in_link=[]
        html=GetData(url)[1]
        href = re.compile('href="(.*?)"')
        src = re.compile('src="(.*?)"')
        res_href = href.findall(html)
        res_src = src.findall(html)
        res_html = res_href+res_src
        in_link.append(url)
        for i in res_html:
            file_ok=True
            for j in file_type_black:
                if j in i:
                    file_ok = False
                    break
            if file_ok:
                if i[:4] == 'http':
                    out_link.append(i)
                else:
                    if i[0]=='/':
                        in_link.append(url+i)
                    else:
                        in_link.append(url+'/'+ i)

        res=[]
        for i in list(set(out_link+in_link)):
            tmp=[]
            tmp.append(i)
            tmp.append(url)
            res.append(tmp)
        return res
    elif isinstance(url, list):
        out_link=[]
        in_link=[]
        res = []
        for i in url:
            i=i.replace('\n','')
            html=GetData(i)[1]
            data=re.compile('href="(.*?)"')
            in_link.append(i)
            for j in data.findall(html):
                if 'http' in j:
                    out_link.append(j)
                else:
                    if j:
                        if j[0]=='/':
                            in_link.append(i+j)
                        else:
                            in_link.append(i +'/'+ j)
            for k in list(set(out_link+in_link)):
                tmp=[]
                tmp.append(k)
                tmp.append(i)
                res.append(tmp)
        return res

# 多进程版本
def GetData_q(url,webdata,master,q):
    try:
        r = requests.get(url, headers=headers, timeout=5)
        r.encoding = 'utf-8'
        data={}
        data["url"]=url
        data["status_code"]=r.status_code
        data["master"]=master
        data["html"]=r.text
        print( data["url"],data["status_code"])
        webdata.append(data)
    except(requests.exceptions.ReadTimeout,requests.exceptions.ConnectTimeout,requests.exceptions.ConnectionError):
        data={}
        data["url"]=url
        data["status_code"]='Timeout'
        data["master"]=master
        data["html"]='Timeout'
        print( data["url"],data["status_code"])
        webdata.append(data)
    q.put(url)



# 多进程版本
def poolmana(url):
    urls = crawler_api(url)
    p = Pool(10)
    q = Manager().Queue()
    webdata = Manager().list([])
    for i in urls:
        p.apply_async(GetData_q, args=(i[0],webdata,i[1],q,))
    p.close()
    p.join()
    return webdata

def run(url):
    res = poolmana(url)
    return res

if __name__ == '__main__':
    print(crawler_api('http://127.0.0.1'))
