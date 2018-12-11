# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 22:38
# @Author  : quincyqiang
# @File    : download_file.py
# @Software: PyCharm
from urllib.request import urlretrieve

def download(url,filename):
    urlretrieve(url=url,filename=filename)

url='http://www.sse.com.cn/disclosure/listedinfo/announcement/c/2018-12-12/603677_20181212_3.pdf'
filname='奇精机械公开发行可转换公司债券募集说明书.pdf'
download(url,filname)