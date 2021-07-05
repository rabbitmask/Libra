#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _    
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   < 
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
                                                    
'''
import time
import os

from Config.config_push import push_token, push
from Moudle.Comparer.comparer import comparer
from Moudle.DiedLink.diedlink import diedlink
from Moudle.HiddenLink.hlfinder import hlfind
from Tools.tools import getDate


def libra_log(url,master,res_comparer,res_hlfind,res_diedlink,filename):

    if res_comparer or res_hlfind or res_diedlink != 200:
        fw = open(filename, 'a',encoding="utf-8")

        fw.write('### '+url+' `'+str(res_diedlink)+'` '+'\n')
        fw.write('* Master: `'+master+'`\n')
        fw.write('* Time: `'+ getDate()+'`\n')
        fw.write('```\n')

        if res_comparer:
            fw.write('========================篡改监测===============================\n')
            if push_token:
                push(master, "篡改监测", getDate())
            for i in res_comparer:
                if i[0]=='+' or i[0]== '-' or i[0] =='?':
                    fw.write(i+'\n')
        if res_hlfind:
            fw.write('========================暗链监测===============================\n')
            if push_token:
                push(master, "暗链监测", getDate())
            for i in res_hlfind:
                fw.write(i+'\n')
        if res_diedlink != 200:
            fw.write('========================死链监测===============================\n')
            if push_token:
                push(master, "死链监测", getDate())
            fw.write(url+' '+str(res_diedlink)+'\n')
        fw.write('==============================================================\n')
        fw.write('```\n\n')

        fw.close()

def run(res):
    timetoken = str(int(time.time()))
    filename = 'Report/libra_report_{}.md'.format(timetoken)

    for i in res:
        res_comparer = comparer(i['url'], i['html'])
        res_hlfind = hlfind(i['html'])
        res_diedlink = diedlink(i['status_code'])
        libra_log(i['url'],i['master'], res_comparer, res_hlfind, res_diedlink,filename)


    if os.path.exists(filename):
        print('报告已保存至：' + filename)
    else:
        print("本次测试未检测到有效问题......")