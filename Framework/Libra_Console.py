#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import argparse



from Config.config_banner import Libra_banner, Libra_banner2
from Moudle.task_console import task_console

def Console():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", dest='taskurl', help="The Taskurl")
    parser.add_argument("-t", dest='tasktype', help="The Tasktype", default='HomePage_Scan',
                        choices=['HomePage_Scan', 'SecondPage_Scan', 'AllSite_Scan','CustomPage_Scan'])

    args = parser.parse_args()

    if args.taskurl and args.tasktype:
        Libra_banner2()
        task_console(args.taskurl, args.tasktype)
    elif args.taskurl:
        Libra_banner2()
        task_console(args.taskurl)
    else:
        Libra_banner()