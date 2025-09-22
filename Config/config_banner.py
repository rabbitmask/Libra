#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import datetime

version='V 3.0'

banner='''

██╗     ██╗██████╗ ██████╗  █████╗ 
██║     ██║██╔══██╗██╔══██╗██╔══██╗
██║     ██║██████╔╝██████╔╝███████║
██║     ██║██╔══██╗██╔══██╗██╔══██║
███████╗██║██████╔╝██║  ██║██║  ██║
╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

          Libra | 网站云监测研判系统
          By RabbitMask | {}
'''.format(version)

banner2 = '''


██╗     ██╗██████╗ ██████╗  █████╗
██║     ██║██╔══██╗██╔══██╗██╔══██╗
██║     ██║██████╔╝██████╔╝███████║
██║     ██║██╔══██╗██╔══██╗██╔══██║
███████╗██║██████╔╝██║  ██║██║  ██║
╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

          Libra | 网站云监测研判报告
          By RabbitMask | {}


    '''.format(datetime.datetime.now().strftime("%Y-%m-%d"))

def Libra_banner():
    print(banner)

def Libra_banner2():
    print('```')
    print(banner2)
    print('```')

if __name__ == '__main__':
    print(banner)
