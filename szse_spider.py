# !/usr/bin/env python3  
# -*- coding:utf-8 _*-  
""" 
@Author:yanqiang 
@File: szse_spider.py 
@Time: 2018/12/12 10:16
@Software: PyCharm 
@Description:
"""
import requests
import pandas as pd
import time

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': 130,
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.szse.cn',
    'Origin': 'http://www.szse.cn',
    'Referer': ' http://www.szse.cn/application/search/index.html?keyword=%E5%80%BA%E5%88%B8%E5%8B%9F%E9%9B%86%E8%AF%B4%E6%98%8E%E4%B9%A6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'X-Request-Type': 'ajax',
    'X-Requested-With': 'XMLHttpRequest',
}

keep_cols = ['id', 'doctitle', 'doccontent', 'docpuburl', 'docpubtime', 'doctype']
# df = pd.DataFrame(columns=keep_cols)
# df.to_csv('data/szse.csv', index=False, header=True)

for i in range(45):
    print("正在爬取{}页".format(i+1))
    payload = {
        'keyword': '债券募集说明书',
        'range': 'title',
        'time': 1,
        'orderby': 'score',
        'currentPage': i + 1,
        'pageSize': 20,
    }
    url = 'http://www.szse.cn/api/search/content'
    res = requests.post(url=url, data=payload)
    try:
        one_page = res.json()
        for data in one_page['data']:
            data.pop('docpubjsonurl')
            data.pop('chnlcode')
            data.pop('index')
            data['doctitle'] = data['doctitle'].replace('<span class="keyword">', '').replace('</span>', '')
            timeArray = time.localtime(data['docpubtime']/1000)
            data['docpubtime'] = time.strftime("%Y-%m-%d", timeArray)
            one_df = pd.DataFrame(data=data, index=[0])
            one_df.to_csv('data/szse.csv', mode='a', index=False, header=False, columns=keep_cols)
        time.sleep(0.2)
    except Exception as e:
        print(e)
        print(res.text)
        print("发生错误：{}页".format(i + 1))
        time.sleep(2)
