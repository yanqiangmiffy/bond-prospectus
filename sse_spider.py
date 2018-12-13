# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 22:03
# @Author  : quincyqiang
# @File    : python.py
# @Software: PyCharm

import requests
import random
import json
import time
import pandas as pd

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': 'yfx_c_g_u_id_10000042=_ck18121121550113938755039951395; yfx_f_l_v_t_10000042=f_t_1544536501378__r_t_1544536501378__v_t_1544536501378__r_c_0; VISITED_MENU=%5B%228307%22%5D',
    'Host': 'query.sse.com.cn',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.sse.com.cn/home/search/?webswd=%E5%80%BA%E5%88%B8%E5%8B%9F%E9%9B%86%E8%AF%B4%E6%98%8E%E4%B9%A6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}


url = 'http://query.sse.com.cn//search/getSearchResult.do'
keep_cols = ['CCHANNELCODE', 'CTITLE_TXT', 'CONTENT', 'CRELEASETIME', 'CRELEASETIME2', 'CURL',
             'DOCID', 'FILESIZE', 'MIMETYPE']
# df = pd.DataFrame(columns=keep_cols)
# df.to_csv('sse.csv', index=False, header=True)

for i in range(305):
    print("正在爬取{}页".format(i+1))
    payload = {
        'search': 'qwjs',
        'jsonCallBack': 'jQuery111208367765368522406_1544536506331',
        'page': i+1,
        'searchword': 'T_L CTITLE T_D E_KEYWORDS T_JT_E T_L债券募集说明书T_R  and cchannelcode T_E T_L0T_D8311T_D8348T_D8349T_D8365T_D8414T_D8415T_D9856T_D9860T_D9862T_D9865T_D9868T_D8638T_D8659T_D8661T_D88888888T_DT_RT_R',
        'orderby': '-CRELEASETIME',
        'perpage': 10,
    }
    res = requests.get(url, params=payload, headers=headers)
    try:
        one_page = json.loads(res.text.replace('jQuery111208367765368522406_1544536506331(', '').rstrip(')'))
        for data in one_page['data']:
            data.pop('CSITECODE')
            data.pop('CTITLE')
            data.pop('KEYWORD')
            one_df = pd.DataFrame(data=data, index=[0])
            one_df.to_csv('sse.csv', mode='a', index=False, header=False, columns=keep_cols)
        time.sleep(0.2)
    except:
        print(res.text)
        print("发生错误：{}页".format(i+1))
        time.sleep(2)
