# !/usr/bin/env python3  
# -*- coding:utf-8 _*-  
""" 
@Author:yanqiang 
@File: process.py 
@Time: 2018/12/12 13:36
@Software: PyCharm 
@Description:
"""
import pandas as pd

sse = pd.read_csv('data/sse.csv')
cols = ['债券募集说明书名称', '公告发布日', '半透明小字']
sse.rename(columns={'CTITLE_TXT': '债券募集说明书名称', 'CRELEASETIME': '公告发布日', 'CONTENT': '半透明小字'}, inplace=True)
sse[['债券募集说明书名称', '公告发布日', '半透明小字']].to_csv('result/上证交易所.csv', index=False, header=True, columns=cols)


szse = pd.read_csv('data/szse.csv')
cols = ['债券募集说明书名称', '公告发布日', '半透明小字']
szse.rename(columns={'doctitle': '债券募集说明书名称', 'docpubtime': '公告发布日', 'doccontent': '半透明小字'}, inplace=True)
szse[['债券募集说明书名称', '公告发布日', '半透明小字']].to_csv('result/深圳证券交易所.csv', index=False, header=True, columns=cols)
