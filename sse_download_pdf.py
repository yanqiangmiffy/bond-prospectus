# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 23:41
# @Author  : quincyqiang
# @File    : sse_download_pdf.py
# @Software: PyCharm
import asyncio
import aiohttp
import time
import pandas as pd
import os

folder_path = 'sse_pdf/'


def break_piont_continue(flag=True):  # 读取url
    """
    :param flag: True 只爬取失败的文章链接；False 未爬取的文章
    :return:
    """
    df = pd.read_csv('data/sse.csv')
    print(len(df))
    if flag:
        with open('log/sse_pdf_log.txt', 'r', encoding='utf-8') as log_file:
            fail_urls = [url.strip() for url in log_file.readlines()]
            df['CURL'] = df['CURL'].apply(lambda x: 'http://www.sse.com.cn' + x).tolist()
            file_names = df[df['CURL'].isin(fail_urls)]['CTITLE_TXT'].tolist()
            return file_names, fail_urls
    else:
        df['unique_names'] = [name + '_' + url.split('/')[-1] for name, url in
                              zip(df['CTITLE_TXT'].tolist(), df['CURL'].tolist())]
        # print(df['unique_names'].value_counts()) # 文档有重复的
        # 是否已经下载
        df['CURL'] = df['CURL'].apply(lambda x: 'http://www.sse.com.cn' + x)
        existed_files = os.listdir('sse_pdf/')
        file_names = df[~df['unique_names'].isin(existed_files)]['CTITLE_TXT'].tolist()
        download_urls = df[~df['unique_names'].isin(existed_files)]['CURL'].tolist()
        print(len(file_names))
        return file_names, download_urls

break_piont_continue(flag=False)

# '''下载图片程序'''
# async def download_pics(name, url, semaphore):
#     async with semaphore:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as response:
#                 try:
#                     pdf = await response.read()  # 以Bytes方式读入非文字
#                     with open(folder_path + name + '_' + url.split('/')[-1], 'wb') as fout:  # 写入文件
#                         fout.write(pdf)
#                         print(name + '_' + url.split('/')[-1] + ' done!')
#                     # await asyncio.sleep(2)
#                 except Exception as e:
#                     print(e)
#                     with open('log/sse_pdf_log.txt', 'a', encoding='utf-8') as log_file:
#                         log_file.write(url + '\n')
#
#
# if __name__ == '__main__':
#     file_names, download_urls = break_piont_continue(flag=False)
#     print(file_names, download_urls)
#     loop = asyncio.get_event_loop()  # 创建loop asyncio协程要在loop中运行
#     start_time = time.time()  # 用于统计时间
#     semaphore = asyncio.Semaphore(100)  # 限制并发量为500
#     tasks = [download_pics(name, url, semaphore) for name, url in zip(file_names, download_urls)]
#     loop.run_until_complete(asyncio.gather(*tasks))
#     loop.close()
#     end_time = time.time()
#     print(end_time - start_time)
