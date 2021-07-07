# Libra
Libra [ 天秤座 ] | 网站篡改、暗链、死链监测平台

### 更新日志
```
V 1.1 更新
完善链接标签，丰富爬取维度
增加深度爬取黑名单，不再对css、图片、压缩文件等内容进行监测
具体参见 Libra\Moudle\Crawler\getweb.py file_type_black
优化各项正则语法，提升辨析准确度
```

### 开发背景
重保期间大量单位对关键站点存在防篡改需求，且大量资产存在维护不及时，存在未知暗链死链，这些资产被非法滥用将产生无法估量的损失，so

### 框架功能列表
```

██╗     ██╗██████╗ ██████╗  █████╗
██║     ██║██╔══██╗██╔══██╗██╔══██╗
██║     ██║██████╔╝██████╔╝███████║
██║     ██║██╔══██╗██╔══██╗██╔══██║
███████╗██║██████╔╝██║  ██║██║  ██║
╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

          Libra | 网站篡改、暗链、死链监测平台
          By RabbitMask | V 1.1

usage: Libra.py [-h] [-u URL] [-m MONITOR] [-f FILE]

optional arguments:
  -h, --help  show this help message and exit
  -u URL      The Target Url
  -m MONITOR  Monitor The Target Url
  -f FILE     The List Of Target Urls
```
### 基础监测功能
会自动记录本次扫描结果，用于下次篡改比对，数据库采用sqllite，报告自动生成至Report目录
```
python Libra.py -u http://127.0.0.1


██╗     ██╗██████╗ ██████╗  █████╗
██║     ██║██╔══██╗██╔══██╗██╔══██╗
██║     ██║██████╔╝██████╔╝███████║
██║     ██║██╔══██╗██╔══██╗██╔══██║
███████╗██║██████╔╝██║  ██║██║  ██║
╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

          Libra | 网站篡改、暗链、死链监测平台
          By RabbitMask | V 1.1

http://127.0.0.1 200
数据爬取完成，正在生成报告，请稍后......
报告已保存至：Report/libra_report_1625478929.md
```

![](https://upload-images.jianshu.io/upload_images/11466123-c307dbb17668cbe1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 持续监测功能：
```
python Libra.py -m http://127.0.0.1


██╗     ██╗██████╗ ██████╗  █████╗
██║     ██║██╔══██╗██╔══██╗██╔══██╗
██║     ██║██████╔╝██████╔╝███████║
██║     ██║██╔══██╗██╔══██╗██╔══██║
███████╗██║██████╔╝██║  ██║██║  ██║
╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

          Libra | 网站篡改、暗链、死链监测平台
          By RabbitMask | V 1.1

Wings守护 | Libra 持续监测中......
http://127.0.0.1 200
数据爬取完成，正在生成报告，请稍后......
报告已保存至：Report/libra_report_1625478705.md



Wings守护 | Libra 持续监测中......
```
已内置pushplus微信预警模块：

![](https://upload-images.jianshu.io/upload_images/11466123-2d8c7742feb4e52d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 批量监测功能：
对集团或辖区内资产，可实现快速监测
```
python Libra.py -f urls.txt

场面过度限制级，请自行脑补，略
```
为保持高并发的稳定性和方便资产梳理，log中加入了master字段用于标记所属资产：
```
### http://127.0.0.1 `200` 
* Master: `http://127.0.0.1`
* Time: `2021-07-05 17:57:14`
```
### 框架核心模块
##### Crawler  爬虫模块
##### Comparer  篡改监测模块
借助difflib库实现差异化精准定位：
```
========================篡改监测===============================
-         hack by rabbit
?                 ^^^^^^

+         hack by ccc
?                 ^^^
```
##### DiedLink  死链监测模块
##### HiddenLink  暗链监测模块
基于敏感字的暗链监测模块，随着规则库的完善，误报率直线上升，所以根据自己的需求维护合理的规则库，详见`Libra.db`
##### 其它
微信推送模块默认关闭，请根据自身需求手动设置：`Libra\Config\config_push.py push_token`

为保持启动速度，数据库自建模块默认关闭，如有需求，请手动解除注释：`Libra\Libra.py # db_start()`

持续监测模块默认60分钟间隔，请自行调整：`Libra\Framework\Console.py  sleep(3600) #循环监控目标站点，默认时间60分钟`

### 项目地址
>https://github.com/rabbitmask/Libra
