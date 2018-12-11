# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 23:41
# @Author  : quincyqiang
# @File    : sse_download_pdf.py
# @Software: PyCharm
import asyncio
import aiohttp
import time
import pandas as pd
folder_path = 'sse_pdf/'

def break_piont_continue():#读取url
    df=pd.read_csv('data/sse.csv')
    download_urls=df['CURL'].apply(lambda x:'http://www.sse.com.cn'+x).tolist()
    file_names=df['CTITLE_TXT'].tolist()
    return file_names[:10],download_urls[:10]

'''下载图片程序'''
async def download_pics(name,url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            pic = await response.read()    #以Bytes方式读入非文字
            with open (folder_path +name +'_'+ url.split('/')[-1], 'wb') as fout:# 写入文件
                fout.write(pic)
                print(name +'_'+ url.split('/')[-1] + ' done!')

if __name__ == '__main__':
    file_names,download_urls = break_piont_continue()
    print(file_names,download_urls)
    loop = asyncio.get_event_loop() #创建loop asyncio协程要在loop中运行
    start_time = time.time()  # 用于统计时间
    tasks = [download_pics(name,url) for name,url in zip(file_names,download_urls)]
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    end_time = time.time()
    print(end_time - start_time)