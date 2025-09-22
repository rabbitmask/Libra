#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from Moudle.task_response import data_response
from Moudle.task_crawler import poolmana_for_webdata, Crawler_for_url

'''
理论传参格式为   taskurl ： http://127.0.0.1:8888
不带‘/’
'''
def task_console(taskurl=None, tasktype="HomePage_Scan"):
    taskurl=taskurl.rstrip('/')
    print("* [INFO] 任务开始 目标站点：{}\t任务类型：{}".format(taskurl, tasktype))
    data={}
    if tasktype == "HomePage_Scan":
        try:
            data=task_for_homepage(taskurl)
        except:
            data["taskurl"] = taskurl
            data["tasktype"] = 'HomePage_Scan'
            data["status"] = "error"
    elif tasktype == "SecondPage_Scan":
        try:
            data=task_for_secondpage(taskurl)
        except:
            data["taskurl"] = taskurl
            data["tasktype"] = 'SecondPage_Scan'
            data["status"] = "error"
    elif tasktype == "AllSite_Scan":
        try:
            data=task_for_allsite(taskurl)
        except:
            data["taskurl"] = taskurl
            data["tasktype"] = 'AllSite_Scan'
            data["status"] = "error"
    elif tasktype == "CustomPage_Scan":
        try:
            data=task_for_custompage(taskurl)
        except:
            data["taskurl"] = taskurl
            data["tasktype"] = 'CustomPage_Scan'
            data["status"] = "error"
    else:
        data["taskurl"] = taskurl
        data["tasktype"] = 'NULL'
        data["status"] = "Tasktype Is Incorrect."
    return data



def task_for_homepage(taskurl):
    res_out_link, res_in_link = Crawler_for_url(taskurl, taskurl)
    print("* [INFO] 目标站点：{}\t任务类型：{}\t外链总数：{}\t内链总数：{}".format(taskurl, '主页扫描', len(res_out_link), len(res_in_link)))
    indexurl= [[taskurl,[taskurl]]]
    webdata = poolmana_for_webdata(res_out_link + indexurl)
    return data_response(webdata,taskurl,'HomePage_Scan',res_out_link,res_in_link)


def task_for_secondpage(taskurl):
    res_out_link_homepage, res_in_link_homepage = Crawler_for_url(taskurl, taskurl)
    res_out_link_tmp=res_out_link_homepage
    res_in_link_tmp = []
    for i in res_in_link_homepage:
        out_link,in_link=Crawler_for_url(i[0], taskurl)
        res_in_link_tmp=res_in_link_tmp+in_link

    res_in_link_tmp_ = []
    for l1 in res_in_link_tmp:
        if l1 not in res_in_link_tmp_:
            res_in_link_tmp_.append(l1)

    res_out_link_tmp_ = []
    for l1 in res_out_link_tmp:
        if l1 not in res_out_link_tmp_:
            res_out_link_tmp_.append(l1)

    res_in_link={}
    res_out_link={}
    for i in res_in_link_tmp_:
        if i[0] in res_in_link.keys():
            tmp=res_in_link[i[0]]
            res_in_link[i[0]]=tmp+i[1]
        else:
            tmp=i[1]
            res_in_link[i[0]]=tmp

    for i in res_out_link_tmp_:
        if i[0] in res_out_link.keys():
            tmp=res_out_link[i[0]]
            res_out_link[i[0]]=tmp+i[1]
        else:
            tmp=i[1]
            res_out_link[i[0]]=tmp

    res_in_link_ = []
    res_out_link_=[]
    for i in res_in_link.keys():
        res_in_link_.append([i,res_in_link[i]])
    for i in res_out_link.keys():
        res_out_link_.append([i,res_out_link[i]])

    print("* [INFO] 目标站点：{}\t任务类型：{}\t外链总数：{}\t内链总数：{}".format(taskurl, '二级扫描', len(res_out_link), len(res_in_link)))
    webdata = poolmana_for_webdata(res_out_link_ + res_in_link_)
    return data_response(webdata, taskurl, 'SecondPage_Scan', res_out_link_, res_in_link_)


def task_for_allsite(taskurl):
    res_out_link_homepage, res_in_link_homepage = Crawler_for_url(taskurl, taskurl)
    res_out_link_tmp=res_out_link_homepage
    res_in_link_tmp = []
    for i in res_in_link_homepage:
        out_link,in_link=Crawler_for_url(i[0], taskurl)
        res_in_link_tmp=res_in_link_tmp+in_link

    in_url = []
    for i in res_in_link_tmp:
        out_link, in_link = Crawler_for_url(i[0], taskurl)
        if i[0] not in in_url:
            in_url.append(i[0])
            for url in in_link:
                res_in_link_tmp.append(url)
            for url in out_link:
                res_out_link_tmp.append(url)

    res_in_link_tmp_ = []
    for l1 in res_in_link_tmp:
        if l1 not in res_in_link_tmp_:
            res_in_link_tmp_.append(l1)

    res_out_link_tmp_ = []
    for l1 in res_out_link_tmp:
        if l1 not in res_out_link_tmp_:
            res_out_link_tmp_.append(l1)

    res_in_link={}
    res_out_link={}
    for i in res_in_link_tmp_:
        if i[0] in res_in_link.keys():
            tmp=res_in_link[i[0]]
            res_in_link[i[0]]=tmp+i[1]
        else:
            tmp=i[1]
            res_in_link[i[0]]=tmp

    for i in res_out_link_tmp_:
        if i[0] in res_out_link.keys():
            tmp=res_out_link[i[0]]
            res_out_link[i[0]]=tmp+i[1]
        else:
            tmp=i[1]
            res_out_link[i[0]]=tmp

    res_in_link_ = []
    res_out_link_=[]
    for i in res_in_link.keys():
        res_in_link_.append([i,res_in_link[i]])
    for i in res_out_link.keys():
        res_out_link_.append([i,res_out_link[i]])

    print("* [INFO] 目标站点：{}\t任务类型：{}\t外链总数：{}\t内链总数：{}".format(taskurl, '全站扫描', len(res_out_link_), len(res_in_link_)))

    webdata = poolmana_for_webdata(res_out_link_ + res_in_link_)

    return data_response(webdata,taskurl,'AllSite_Scan',res_out_link_,res_in_link_)

def task_for_custompage(taskurl):
    tmp = taskurl.split('//')
    baseurl = tmp[0] + '//'
    for i in tmp[1].split('/')[0:1]:
        baseurl += i + '/'
    res_out_link, res_in_link = Crawler_for_url(taskurl, baseurl.rstrip('/'))
    print("* [INFO] 目标站点：{}\t任务类型：{}\t外链总数：{}\t内链总数：{}".format(taskurl, '自定义页面扫描', len(res_out_link), len(res_in_link)))
    indexurl= [[taskurl,[taskurl]]]
    webdata = poolmana_for_webdata(res_out_link + indexurl)
    return data_response(webdata,taskurl,'CustomPage_Scan',res_out_link,res_in_link)


if __name__ == '__main__':
    print(task_console('https://www.x.com','HomePage_Scan'))
