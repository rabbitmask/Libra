#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import hashlib
import re
import requests
from multiprocessing import Pool, Manager
from Config.config_crawler import file_type_black
from Config.config_proxies import proxies
from Config.config_requests import baiduspider_headers, normal_headers
from ORM.db_rules import getwhiteips

requests.packages.urllib3.disable_warnings()

def getmd5(hash):
    md5 = hashlib.md5()
    md5.update(hash)
    return md5.hexdigest()

# 获取单页面内容
def GetData(url):
    try:
        r = requests.get(url, headers=baiduspider_headers, timeout=10, verify=False, proxies=proxies)
        if r.status_code != 200:
            r = requests.get(url, headers=normal_headers, timeout=10, verify=False, proxies=proxies)
        return r.status_code, r.text, getmd5(r.content)

        # return r.status_code,html.unescape(r.text),getmd5(r.content)
    # except(requests.exceptions.ReadTimeout,requests.exceptions.ConnectTimeout,requests.exceptions.ConnectionError):
    except:
        return 'Timeout','Timeout'

# 爬单页面url列表 获取外链和内链
def Crawler_for_url(url, taskurl):
    out_link=[]
    in_link=[]
    html=GetData(url)[1]
    res_href = re.compile(r'[\'\"\.]?href[\'\"]?=?[\'\"](.*?)[\'\"]').findall(html)
    res_src = re.compile(r'[\'\"\.]?src[\'\"]?[:=]?[\'\"](.*?)[\'\"]').findall(html)
    res_html = res_href+res_src
    res_html = [i for i in res_html if i != '']
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
                    in_link.append(taskurl+i)
                else:
                    in_link.append(taskurl+'/'+ i)

    res_out_link=[]
    res_in_link=[]


    whiteips=getwhiteips()

    for i in list(set(out_link)):
        white_ip = True
        for whiteip in whiteips:    # 对外链进行白名单，不影响内链 因为加白，所以显示的外链比实际外链要小，一定要取数的话取上一步好一些
            if whiteip in i:
                white_ip = False
                break

        if i != taskurl and white_ip:                 #猜测重复连接是内链和外链都记录目标地址造成的所以去掉自己
            tmp=[]
            tmp.append(i)
            tmp.append([url])
            res_out_link.append(tmp)
    for i in list(set(in_link)):
        tmp=[]
        tmp.append(i)
        tmp.append([url])
        res_in_link.append(tmp)
    return res_out_link,res_in_link



# 多进程版本 - 爬取页面内容
def GetData_q(url,webdata,master,q):
    url=url.strip('0').strip('/')
    try:
        r = requests.get(url, headers=baiduspider_headers, timeout=10, verify=False, proxies=proxies)

        if r.status_code != 200:
            r = requests.get(url, headers=normal_headers, timeout=10, verify=False, proxies=proxies)

        try:
            body=r.text
            encode1 = r.encoding
            encode2 = r.apparent_encoding
            body = body.encode(encode1).decode(encode2)
        except:
            body=r.text


        data={}
        data["url"]=url
        data["status_code"]=r.status_code   #这就是int。别听ide的
        data["master"]=master
        data["html"] = body
        # data["html"] = html.unescape(r.text)
        data["hash"]=getmd5(r.content)
        # data["html"]='test'
        # print( data["url"],data["status_code"])
        webdata.append(data)




    # except(requests.exceptions.ReadTimeout,requests.exceptions.ConnectTimeout,requests.exceptions.ConnectionError):
    except:
        data={}
        data["url"]=url
        data["status_code"]='Timeout'
        data["master"]=master
        data["html"]='Timeout'
        data["hash"] = ''
        # print( data["url"],data["status_code"])
        webdata.append(data)
    q.put(url)



# 多进程版本
def poolmana_for_webdata(urls):
    p = Pool(60)
    q = Manager().Queue()
    webdata = Manager().list([])
    for i in urls:
        p.apply_async(GetData_q, args=(i[0],webdata,i[1],q,))
    p.close()
    p.join()

    return webdata

def GetDatatest(url):
    # try:
        r = requests.get(url, headers=baiduspider_headers, timeout=10, verify=False, proxies=proxies)
        if r.status_code != 200:
            r = requests.get(url, headers=normal_headers, timeout=10, verify=False, proxies=proxies)
        return r.status_code, r.text, getmd5(r.content)



if __name__ == '__main__':
    print(GetDatatest('https://x.com'))
