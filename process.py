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

# sse = pd.read_csv('data/sse.csv')
# cols = ['债券募集说明书名称', '公告发布日', '半透明小字']
# sse.rename(columns={'CTITLE_TXT': '债券募集说明书名称', 'CRELEASETIME': '公告发布日', 'CONTENT': '半透明小字'}, inplace=True)
# sse[['债券募集说明书名称', '公告发布日', '半透明小字']].to_csv('result/上证交易所.csv', index=False, header=True, columns=cols)
#
#
# szse = pd.read_csv('data/szse.csv')
# cols = ['债券募集说明书名称', '公告发布日', '半透明小字']
# szse.rename(columns={'doctitle': '债券募集说明书名称', 'docpubtime': '公告发布日', 'doccontent': '半透明小字'}, inplace=True)
# szse[['债券募集说明书名称', '公告发布日', '半透明小字']].to_csv('result/深圳证券交易所.csv', index=False, header=True, columns=cols)
sse = pd.read_csv('result/sse_result.csv')
szse = pd.read_csv('result/szse_result.csv')

sse.columns = ['公司全称', '公司简称', '公告日期', '风险词汇频数',
               '前后存在无等的风险频数', '整个债券书字数', '风险部分字数统计', '风险自然段落统计',
               '风险限定字数句子统计', '风险所有句子统计', '是否检测到风险章节', '文档名称']
szse.columns = ['公司全称', '公司简称', '公告日期', '风险词汇频数',
               '前后存在无等的风险频数', '整个债券书字数', '风险部分字数统计', '风险自然段落统计',
               '风险限定字数句子统计', '风险所有句子统计', '是否检测到风险章节', '文档名称']
df = pd.concat([sse, szse], axis=0, sort=False)
df['文档名称'] = df['文档名称'].apply(lambda x: x.replace('.txt', ''))
print(sse.shape)
print(szse.shape)
# print(df)

df.to_csv('result/债券募集说明书统计数据.csv', index=False, header=True)
