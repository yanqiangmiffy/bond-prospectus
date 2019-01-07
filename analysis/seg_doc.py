# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 22:04
# @Author  : quincyqiang
# @File    : seg_doc.py
# @Software: PyCharm
import jieba

# temp = []
# with open('浙江台华新材料股份有限公司.txt', 'r', encoding='utf-8') as doc_file:
#     for para in doc_file.read().split('。'):
#         if '风险' in para and len(para) < 500:
#             para=para.replace(' ','')
#             para=" ".join(para.split('\n')).strip()
#             print(para)
#             print('文本长度：{}'.format(len(para)))
#             print([word for word in jieba.cut(para) if word!=' '])
#             print('-' * 100)
#             temp.append(para)
#
# print(len(temp)//2)


# temp = []
# with open('demo.txt', 'r', encoding='utf-8') as doc_file:
#     for para in doc_file.read().split('\n'):
#         # print(para)
#         # temp.append(para)
#         # print('--------')
#         if para.strip().endswith('。'):
#             print(para)
#             temp.append(para)
#             print('--------')
#
# print(len(temp))

import re


def count_risk_txt(txt):
    paras = [para for para in re.split('第.节|第.条|第十.条|第.章', txt) if '风险' in para[:15]]
    paras = [para for para in paras if '...' not in para]
    return paras


def count_risk_para(filename):
    """
    统计风险部分段落个数
    :param filename:
    :return:
    """
    with open(filename, 'r', encoding='utf-8') as f:
        raw_txt = f.read()
    paras = count_risk_txt(raw_txt)
    print(paras)
    txt = "".join(paras)
    temp = []
    for para in txt.split('\n'):
        if para.strip().endswith('。'):
            temp.append(para)
    return len(temp)

count_risk_para('demo.txt')