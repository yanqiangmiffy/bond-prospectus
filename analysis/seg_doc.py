# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 22:04
# @Author  : quincyqiang
# @File    : seg_doc.py
# @Software: PyCharm
import jieba

temp = []
with open('sse_doc.txt', 'r', encoding='utf-8') as doc_file:
    for para in doc_file.read().split('。'):
        if '风险' in para and len(para) < 500:
            para=para.replace(' ','')
            para=" ".join(para.split('\n')).strip()
            print(para)
            print('文本长度：{}'.format(len(para)))
            print([word for word in jieba.cut(para) if word!=' '])
            print('-' * 100)
            temp.append(para)

print(len(temp))
