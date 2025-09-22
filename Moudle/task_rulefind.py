#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import html
import re
import requests

requests.packages.urllib3.disable_warnings()
# 数据库访问优化，常驻内存而非频繁访问数据库

def backdoor_find(url,re_rules_list,re_paths_list):
    rules = []
    host = True
    try:
        for path in re_paths_list:
            for re_rules in re_rules_list:
                req = requests.get(url+path,timeout=10)
                result = re.findall(r'{}'.format(re_rules[0]), req.text, re.S)
                if result:
                    vulurl='【'+re_rules[1]+'】 '+ url+path
                    if vulurl not in rules:
                        rules.append(vulurl)
                        host = False
                else:
                    pass
    except:
        pass

    if host == False:
        return rules
    else:
        pass


def violativelink_find(htmltxt,re_rules_list):
    rules = []
    host = True
    htmltxt=html.unescape(htmltxt)

    for re_rules in re_rules_list:
        # print(re_rules)

        result = re.findall(r'{}'.format(re_rules[0]), htmltxt, re.I)
        if result:
            rules.append('【'+re_rules[1]+'】 '+re_rules[0])
            host = False
    if host == False:
        return rules
    else:
        pass

# 黑链检测
def blacklink_find(htmltxt,re_rules_list):
    data = []
    host = True
    for re_rules in re_rules_list:
        html_scripts = re.compile(r'(<script[\s\S]*?</script>)').findall(htmltxt)
        # print(re_rules[0])
        if '<script' in re_rules[0]:
            # print('111111111111111')
            for html_script in html_scripts:
                result = re.compile(r'{}'.format(re_rules[0])).findall(html_script)
                if result:
                    for i in result:
                        data_txt=html.unescape(i)
                        # print(str(len(data_txt)),data_txt)

                        # 这里暂时一刀切了下,单<script>过大的就不看了
                        if len(data_txt)>9999:
                            pass

                        else:
                            if '【'+re_rules[1]+'】 ' + data_txt not in data:
                                data.append('【'+re_rules[1]+'】 '+ data_txt)
                                host = False
        else:
            # print('2222222222')
            result = re.compile(r'{}'.format(re_rules[0])).findall(htmltxt)
            if result:
                for i in result:
                    data_txt = html.unescape(i)
                    if '【' + re_rules[1] + '】 ' + data_txt not in data:
                        data.append('【' + re_rules[1] + '】 ' + data_txt)
                        host = False
    if host == False:
        return data
    else:
        pass


if __name__ == '__main__':
    pass