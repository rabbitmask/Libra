#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import json
import requests

push_token=''

def push(target,moudle,time):
	token = push_token
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
		'Content-Type': 'application/json'}
	data = {
		"token": token,
		"title": "【Libra @ Wings】",
		"content": {'预警地址':target,'预警类型':moudle,'预警时间':time},
		"template": "json"
	}
	body = json.dumps(data).encode(encoding='utf-8')
	r = requests.post('http://pushplus.hxtrip.com/send', data=body, headers=headers)



if __name__ == '__main__':
	push('test','test','test')