# !/usr/bin/env python3  
# -*- coding:utf-8 _*-  
""" 
@Author:yanqiang 
@File: main2.py 
@Time: 2018/12/28 11:29
@Software: PyCharm 
@Description:
"""
import pandas as pd
import jieba

szse = pd.read_csv('data/szse.csv')


def gen_filename(row):
    """
    生成文档名称
    :param row:
    :return:
    """
    filename = row.doctitle + '_' + row.docpuburl.split('/')[-1]
    filename = filename.rstrip('.pdf').replace('.PDF', '') + '.txt'
    return filename


def get_text(filename):
    """
    根据文档名字获取txt内容
    :param filename:
    :return:
    """
    szse_doc_path = 'analysis/szse_doc/'
    with open(szse_doc_path + filename, 'r', encoding='utf-8') as f:
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
            if word in seg[:5] or word in seg[-5:]:
                without_risk_cnt += 1

    txt_len = len(txt)  # 文本字数

    temp = []
    for para in txt.split('。'):
        if '风险' in para and len(para) < 500:
            para = para.replace(' ', '')
            temp.append(para)
    risk_txt_len = len("".join(temp)) // 4  # 风险描述字数
    risk_para_cnt = len(temp) // 4  # 风险自然段落统计
    return risk_cnt, without_risk_cnt, txt_len, risk_txt_len, risk_para_cnt


szse['filename'] = szse.apply(lambda row: gen_filename(row), axis=1)
szse['txt'] = szse.apply(lambda row: get_text(row.filename), axis=1)
szse['risk_cnt'], szse['without_risk_cnt'], szse['txt_len'], szse['risk_txt_len'], szse[
    'risk_para_cnt'] = zip(*szse['txt'].map(count))
from zhner.core import ner

import numpy as np


def get_fullname(row):
    if row.doctitle.count('公司') >= 2:
        s = str(row.doctitle)
    else:
        s = str(row.doccontent)
    return ner(s).split('公司')[0] + '公司'


szse['full_name'] = szse.apply(lambda row: get_fullname(row), axis=1)


def get_subname(row):
    cans = [w for w in str(row.doctitle).split('：')]
    if len(cans) != 0:
        return cans[0]
    else:
        return np.nan


szse['sub_name'] = szse.apply(lambda row: get_subname(row), axis=1)

cols = ['full_name', 'sub_name', 'docpubtime', 'risk_cnt',
        'without_risk_cnt', 'txt_len', 'risk_txt_len', 'risk_para_cnt', 'filename']
szse = szse[~szse['filename'].str.contains('摘要')]
szse = szse[~szse['filename'].str.contains('提示性公告')]

szse.to_csv('szse_result.csv', index=False, header=False, columns=cols)
