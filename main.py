# !/usr/bin/env python3  
# -*- coding:utf-8 _*-  
""" 
@Author:yanqiang 
@File: main.py 
@Time: 2018/12/26 17:40
@Software: PyCharm 
@Description: # 统计任务
"""
import pandas as pd
import jieba

sse = pd.read_csv('data/sse.csv')
szse = pd.read_csv('data/szse.csv')


def gen_filename(row):
    """
    生成文档名称
    :param row:
    :return:
    """
    filename = row.CTITLE_TXT + '_' + row.CURL.split('/')[-1]
    filename = filename.rstrip('.pdf').replace('.PDF', '') + '.txt'
    return filename


def get_text(filename):
    """
    根据文档名字获取txt内容
    :param filename:
    :return:
    """
    sse_doc_path = 'analysis/sse_doc/'
    with open(sse_doc_path + filename, 'r', encoding='utf-8') as f:
        txt = f.read()
        txt = " ".join([doc for doc in txt.split('\n') if doc.split()]).strip()
        txt = txt.replace(' ', '')
    return txt


def count(txt):
    risk_cnt = txt.count('风险')  # 风险词语个数

    without_risk_cnt = 0
    tag_word = ['无', '低', '小', '没有', '不高', '不大']
    for seg in txt.split('风险'):
        for word in tag_word:
            if word in seg[:6] or word in seg[:-5]:
                without_risk_cnt += 1

    txt_len = len(txt)  # 文本字数

    temp = []
    for para in txt.split('。'):
        if '风险' in para and len(para) < 500:
            para = para.replace(' ', '')
            temp.append(para)
    risk_txt_len = len("".join(temp))  # 风险描述字数
    risk_para_cnt = len(temp)//2  # 风险自然段落统计
    return risk_cnt, without_risk_cnt, txt_len, risk_txt_len, risk_para_cnt


def count_risk_word(txt):
    """
    统计文档中风险出现的次数
    :return:
    """
    return txt.count('风险')


def count_without_risk(txt):
    cnt = 0
    tag_word = ['无', '低', '小', '没有', '不高', '不大']
    for seg in txt.split('风险'):
        for word in tag_word:
            if word in seg[:6] or word in seg[:-5]:
                cnt += 1
    return cnt


def count_risk_len(txt):
    """
    统计风险部分文字个数
    :return:
    """
    temp = []
    for para in txt.split('。'):
        if '风险' in para and len(para) < 500:
            para = para.replace(' ', '')
            temp.append(para)
    return len("".join(temp)), len(temp)


# df_test['size_kb'], df_test['size_mb'], df_test['size_gb'] = zip(*df_test['size'].apply(sizes))

sse['filename'] = sse.apply(lambda row: gen_filename(row), axis=1)
sse['txt'] = sse.apply(lambda row: get_text(row.filename), axis=1)
# sse['risk_cnt'] = sse.apply(lambda row: count_risk_word(row.txt), axis=1)
# sse['without_risk_cnt'] = sse.apply(lambda row: count_without_risk(row.txt), axis=1)
# sse['txt_len'] = sse.apply(lambda row: len(row.txt), axis=1)
# print(sse['txt','risk_cnt','without_risk_cnt','txt_len'])
sse['risk_cnt'], sse['without_risk_cnt'], sse['txt_len'], sse['risk_txt_len'], sse[
    'risk_para_cnt'] = zip(*sse['txt'].map(count))
print(sse[['risk_cnt', 'without_risk_cnt', 'txt_len', 'risk_txt_len', 'risk_para_cnt']])
