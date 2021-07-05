#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _    
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   < 
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
                                                    
'''
import argparse
from time import sleep

from Framework import LibraLog
from Moudle.Crawler import getweb




def Console():
    parser = argparse.ArgumentParser()


    parser.add_argument("-u", dest='url',help="The Target Url")

    parser.add_argument("-m", dest='monitor',help="Monitor The Target Url")

    parser.add_argument("-f", dest='file',help="The List Of Target Urls")

    args = parser.parse_args()

    if args.url:
        res=getweb.run(args.url)
        print("数据爬取完成，正在生成报告，请稍后......")
        LibraLog.run(res)
    elif args.monitor:
        while 1:
            print("Wings守护 | Libra 持续监测中......")
            res = getweb.run(args.monitor)
            print("数据爬取完成，正在生成报告，请稍后......")
            LibraLog.run(res)
            sleep(3600) #循环监控目标站点，默认时间60分钟
            print('\n\n')
    elif args.file:
        f=open(args.file,'r')
        urls=f.readlines()
        f.close()
        res = getweb.run(urls)
        print("数据爬取完成，正在生成报告，请稍后......")
        LibraLog.run(res)