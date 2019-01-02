# !/usr/bin/env python3  
# -*- coding:utf-8 _*-  
""" 
@Author:yanqiang 
@File: core.py
@Time: 2018/12/26 17:40
@Software: PyCharm 
@Description: # 统计任务
"""
import pandas as pd
import jieba
import re

sse = pd.read_csv('data/sse.csv')


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
    #  风险词语个数
    risk_cnt = txt.count('风险')  # 风险词语个数
    # 无风险个数
    without_risk_cnt = 0
    tag_word = ['无', '低', '小', '没有', '不高', '不大']
    for seg in txt.split('风险'):
        for word in tag_word:
            if word in seg[:5] or word in seg[-5:]:
                without_risk_cnt += 1
    # 文本字数
    txt_len = len(txt)

    # 风险部分统计
    paras = count_risk_txtpara(txt)
    if len(paras) != 0:
        risk_txt_len = len("".join(paras))
        temp = []
        for para in "".join(paras).split('。'):
            if 70 < len(para) < 500:
                para = para.replace(' ', '')
                temp.append(para)
        risk_para_cnt = int(len(temp) // 2)
        flag = "是"
    else:
        temp = []
        for para in txt.split('。'):
            if '风险' in para and 80 < len(para) < 500:
                para = para.replace(' ', '')
                temp.append(para)
        risk_txt_len = len("".join(temp))  # 风险描述字数
        risk_para_cnt = len(temp)  # 风险自然段落统计
        flag = "否"
    return risk_cnt, without_risk_cnt, txt_len, risk_txt_len, risk_para_cnt, flag


def count_risk_txtpara(txt):
    paras = [para for para in re.split('第.节|第.条|第十.条|第.章', txt) if '风险' in para[:10]]
    paras = [para for para in paras if '...' not in para]
    return paras


sse['filename'] = sse.apply(lambda row: gen_filename(row), axis=1)
sse['txt'] = sse.apply(lambda row: get_text(row.filename), axis=1)
sse['risk_cnt'], sse['without_risk_cnt'], sse['txt_len'], sse['risk_txt_len'], sse[
    'risk_para_cnt'], sse['flag'] = zip(*sse['txt'].map(count))
from zhner.core import ner

import numpy as np


def get_fullname(row):
    if row.CTITLE_TXT.count('公司') >= 2:
        s = str(row.CTITLE_TXT)
    else:
        s = str(row.CONTENT)
    return ner(s).split('公司')[0] + '公司'


sse['full_name'] = sse.apply(lambda row: get_fullname(row), axis=1)


def get_subname(row):
    cans = [w for w in str(row.CONTENT).split(' ') if '股票简称' in w]
    if len(cans) != 0:
        return "".join(cans).replace('股票简称：', '')
    else:
        return np.nan


sse['sub_name'] = sse.apply(lambda row: get_subname(row), axis=1)

cols = ['full_name', 'sub_name', 'CRELEASETIME', 'risk_cnt',
        'without_risk_cnt', 'txt_len', 'risk_txt_len', 'risk_para_cnt', 'flag','filename']
sse[~sse['filename'].str.contains('摘要')].to_csv('result/sse_result.csv', index=False, header=False, columns=cols)
