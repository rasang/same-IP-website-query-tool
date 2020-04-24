# -*- coding: UTF-8 -*-
import requests
import re
from sys import argv

try:
    urlToQuery = argv[1]
except IndexError:
    print("请指定要查询的域名，格式如：\npython 同IP网站查询.py taobao.com")
    exit(1)

pageNumber = 1
finalResult = []
regRule = '<a href=\'javascript:\' onclick="window.open\(\'http.*?\'\)'

try:
    html = requests.get("http://stool.chinaz.com/same?s=" + urlToQuery + "&page=" + str(pageNumber)).text
    pageResult = re.findall(regRule, html)

    while len(pageResult) != 0:
        finalResult += pageResult
        pageNumber += 1
        html = requests.get("http://stool.chinaz.com/same?s=" + urlToQuery + "&page=" + str(pageNumber)).text
        pageResult = re.findall(regRule, html)

except requests.exceptions.ConnectionError:
    print("请检查你的网络连接")
    exit(1)

print("共查询到" + str(finalResult.__len__()) + "条结果")

for i in finalResult:
    print(i[44:-2])
