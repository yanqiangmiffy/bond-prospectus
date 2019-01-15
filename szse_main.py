# !/usr/bin/env python3  
# -*- coding:utf-8 _*-  
""" 
@Author:yanqiang 
@File: szse_main.py
@Time: 2018/12/28 11:29
@Software: PyCharm 
@Description:
"""
import pandas as pd
import jieba
import re

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
    szse_doc_path = 'analysis/szse_doc_v2/'
    with open(szse_doc_path + filename, 'r', encoding='utf-8') as f:
        txt = f.read()
        txt = " ".join([doc for doc in txt.split('\n') if doc.split()]).strip()
        txt = txt.replace(' ', '')
    return txt


def get_raw_txt(filename):
    szse_doc_path = 'analysis/szse_doc_v2/'
    with open(szse_doc_path + filename, 'r', encoding='utf-8') as f:
        raw_txt = f.read()
    return raw_txt


def detect_risk_txt(raw_txt, filename):
    """
    定位风险段落
    :param raw_txt:
    :param filename:
    :return:
    """
    raw_txt = raw_txt.replace('第一章', '标题')
    all_paras = re.split('      第.节|      第.条|      第十.条|      第.章', raw_txt)

    # 风险段落数大于13
    paras = [para for para in re.split('      第.节|      第.条|      第十.条|      第.章', raw_txt) if '风险' in para[:15]]
    paras = [para for para in paras if '...' not in para and '�����' not in para[:10]]
    print(filename)
    # if len(paras) == 1:
    #     flag_index = all_paras.index(paras[0])
    #     for i in range(1, 3):  # 1,2
    #         if flag_index + i + 1<len(all_paras):
    #             next_para = all_paras[flag_index + i + 1]
    #             if '\n' in next_para[:16] and len(next_para) < 1000:
    #                 paras.append(next_para)
    #             if '\n' not in next_para[:18]:
    #                 paras.append(next_para)
    paras=[para.replace('�', '') for para in paras]

    # 段落数小于13
    new_txt = "".join(paras).replace('�', '')
    temp = []
    for para in new_txt.split('\n'):
        if para.strip().endswith('。'):
            temp.append(para)
    # if '复星实业可转换公司债券募集说' in filename:
    #     print(paras)
    #     print(len(temp))
    if 0 < len(temp) <= 15 and '摘要' not in filename:
        new_paras = []
        for para in all_paras:
            if '....' not in para and '风险' in para[:15]:
                flag_para = para
                flag_index = all_paras.index(flag_para)
                new_paras.append(flag_para)
                # if '招商银行发行可转换公' in filename:
                #     print(paras)
                #     print(len(temp))
                #     print(all_paras[flag_index + 1])
                #     print(new_paras)
                for i in range(1, 3):  # 1,2
                    next_para = all_paras[flag_index + i + 1]
                    if '\n' in next_para[:16] and len(next_para) < 1000:
                        new_paras.append(next_para)
                    if '\n' not in next_para[:18]:
                        new_paras.append(next_para)
        return new_paras
        # break

    return paras


def count(txt, raw_txt, filename):
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
    paras = detect_risk_txt(raw_txt, filename)
    if len(paras) != 0:
        risk_txt_len = len("".join("".join(paras).split()))
        sent = []
        all_sent = []
        for para in "".join(paras).split('。'):
            if 70 < len(para) < 500:
                para = para.replace(' ', '')
                sent.append(para)
            if para:
                all_sent.append(para)
        part_sent_cnt = len(sent)  # 风险自然段落句子统计
        all_sent_cnt = len(all_sent)
        flag = "是"
    else:
        sent = []
        all_sent = []
        for para in "".join(paras).split('。'):
            if 70 < len(para) < 500:
                para = para.replace(' ', '')
                sent.append(para)
            if para:
                all_sent.append(para)
        part_sent_cnt = len(sent)  # 风险自然段落句子统计
        all_sent_cnt = len(all_sent)
        risk_txt_len = len("".join(sent))  # 风险描述字数
        flag = "否"
    return risk_cnt, without_risk_cnt, txt_len, \
           risk_txt_len, part_sent_cnt, all_sent_cnt, flag


def count_risk_para(raw_txt, filename):
    """
    统计风险部分段落个数
    :param raw_txt:
    :param filename:
    :return:
    """
    paras = detect_risk_txt(raw_txt, filename)
    txt = "".join(paras)
    temp = []
    for para in txt.split('\n'):
        if para.strip().endswith('。'):
            temp.append(para)
    return len(temp)


szse['filename'] = szse.apply(lambda row: gen_filename(row), axis=1)
szse['txt'] = szse.apply(lambda row: get_text(row.filename), axis=1)
szse['raw_txt'] = szse.apply(lambda row: get_raw_txt(row.filename), axis=1)
szse['risk_cnt'], szse['without_risk_cnt'], szse['txt_len'], szse['risk_txt_len'], szse[
    'part_sent_cnt'], szse['all_sent_cnt'], szse['flag'] = zip(
    *szse.apply(lambda row: count(row.txt, row.raw_txt, row.filename), axis=1))

print("统计风险部分段落个数")
szse['risk_para_cnt'] = szse.apply(lambda row: count_risk_para(row.raw_txt, row.filename), axis=1)


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
    cans = [w for w in str(row.doccontent).split(' ') if '股票简称' in w]
    if len(cans) != 0:
        return "".join(cans).replace('股票简称：', '')
    else:
        return np.nan


szse['sub_name'] = szse.apply(lambda row: get_subname(row), axis=1)

cols = ['full_name', 'sub_name', 'CRELEASETIME', 'risk_cnt',
        'without_risk_cnt', 'txt_len', 'risk_txt_len', 'risk_para_cnt', 'part_sent_cnt', 'all_sent_cnt', 'flag',
        'filename']
szse = szse[~szse['filename'].str.contains('摘要')]
szse = szse[~szse['filename'].str.contains('提示性公告')]

szse.to_csv('result/szse_result.csv', index=False, header=False, columns=cols)
