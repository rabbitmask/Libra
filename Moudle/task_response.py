#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import json
from Config.config_logging import loglog
from Moudle.task_rulefind import blacklink_find, violativelink_find, backdoor_find
from ORM.db_rules import get_violativelink_rules, get_backdoor_rules, get_blacklink_rules, get_backdoor_paths, getwhiteips
from Tools.tools import getDate


def data_response(webdata,taskurl,tasktype,res_out,res_in):
    # print(webdata,taskurl,tasktype,res_out,res_in)

    # print(res_in,res_out)

    data = {}
    diedlink_list = []
    violativelink_list = []
    backdoor_list = []
    blacklink_list = []

    # 数据库访问优化，常驻内存而非频繁访问数据库
    violativelink_rules_list = get_violativelink_rules()
    blacklink_rules_list = get_blacklink_rules()
    backdoor_rules_list = get_backdoor_rules()
    backdoor_paths_list = get_backdoor_paths()

    # 黑客入侵检测更名为后门检测，模块高度独立化，重要等级由☆变更为☆☆☆☆
    # 当前模块总览：
    # 黑链检测 ☆☆☆☆☆
    # 后门检测 ☆☆☆☆
    # 违规检测 ☆☆☆☆
    # 死链检测 ☆☆
    # 漏洞检测(漏扫)  ☆☆☆
    # 漏洞检测(专项)  ☆☆☆☆☆
    # 篡改检测 取消(模块立项模糊)
    backdoorres = backdoor_find(taskurl, backdoor_rules_list,backdoor_paths_list)
    if backdoorres:
        tmpdata = {}
        tmpdata["url"] = taskurl
        tmpdata["backdoorres"] = backdoorres
        tmpdata["master"] = [taskurl]
        backdoor_list.append(tmpdata)

    for i in webdata:
        if i["status_code"] != 200:
            tmpdata = {}
            tmpdata["url"] = i["url"]
            tmpdata["status_code"] = i["status_code"]
            tmpdata["master"]=i["master"]
            diedlink_list.append(tmpdata)

        violativelinkres = violativelink_find(i["html"], violativelink_rules_list)
        blacklinkres = blacklink_find(i["html"], blacklink_rules_list)



        if violativelinkres:
            tmpdata = {}
            tmpdata["url"] = i["url"]
            tmpdata["violativelinkres"] = violativelinkres
            tmpdata["master"]=i["master"]
            violativelink_list.append(tmpdata)

        if blacklinkres:

            tmpdata = {}
            tmpdata["url"] = i["url"]
            tmpdata["blacklinkres"] = blacklinkres
            tmpdata["master"]=i["master"]
            blacklink_list.append(tmpdata)

        if backdoorres:
            tmpdata = {}
            tmpdata["url"] = i["url"]
            tmpdata["backdoorres"] = backdoorres
            tmpdata["master"] = i["master"]
            backdoor_list.append(tmpdata)



    data["taskurl"] = taskurl
    data["tasktype"] = tasktype
    data["status"] = "sussess"
    data["diedlink_list"] = diedlink_list
    data["blacklink_list"] = blacklink_list
    data["violativelink_list"] = violativelink_list
    data["backdoor_list"] = backdoor_list
    # data["res_out"] = res_out    # 开发暂时不用这俩接口了，关掉~
    # data["res_in"] = res_in
    data["datetime"] = str(getDate())


    printdata=data
    # 原始数据打印 = api返回内容
    # print(json.dumps(data, indent=2,ensure_ascii=False))    # 打印全部
    # md打印
    data_print_md(printdata)

    # keys_to_remove = ['res_in', 'res_out']
    # new_dict = {key: value for key, value in printdata.items() if key not in keys_to_remove}
    # print(json.dumps(new_dict, indent=2,ensure_ascii=False))    # 打印去掉内外链的全部

    # save_task_data(data)      #toB 版本不需要存库
    loglog(printdata)
    return data


def data_print_md(data):
    if data['status']=="sussess":
        print('------------------------------------------------------------')
        print('# 检测地址：'+ data['taskurl'])
        print('------------------------------------------------------------')

        if data['blacklink_list']:
            print('### 黑链检测结果：' + '\n')
            print('```')
            for i in data['blacklink_list']:
                print('问题地址： \n' + i['url'])
                print('黑链信息：')
                for j in i['blacklinkres']:
                    print(j)
                print('来源地址：')
                for j in i['master']:
                    print(j)
                print('\n')
            print('```')
            print('------------------------------------------------------------')

        if data['violativelink_list']:
            print('### 违规检测结果：' + '\n')
            print('```')
            for i in data['violativelink_list']:
                print('问题地址： \n' + i['url'])
                print('违规内容：')
                for j in i['violativelinkres']:
                    print(j)
                print('来源地址：')
                for j in i['master']:
                    print(j)
                print('\n')
            print('```')
            print('------------------------------------------------------------')


        if data['backdoor_list']:
            print('### 后门检测结果：'+ '\n')
            print('```')
            for i in data['backdoor_list']:
                print('问题地址： \n' + i['url'])
                print('后门特征：')
                for j in i['backdoorres']:
                    print(j)
                print('来源地址：')
                for j in i['master']:
                    print(j)
                print('\n')
            print('```')
            print('------------------------------------------------------------')

        if data['diedlink_list']:
            print('### 死链检测结果：'+ '\n')
            print('```')
            for i in data['diedlink_list']:
                print('问题地址： \n' + i['url'])
                print('访问状态： \n' + str(i['status_code']))
                print('来源地址：')
                for j in i['master']:
                    print(j)
                print('\n')
            print('```')
            print('------------------------------------------------------------')

    else:
        print(json.dumps(data, indent=2,ensure_ascii=False))