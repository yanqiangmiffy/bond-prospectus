# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 22:47
# @Author  : quincyqiang
# @File    : demo.py
# @Software: PyCharm

import pandas as pd

keep_cols = ['CCHANNELCODE', 'CTITLE_TXT', 'CONTENT', 'CRELEASETIME', 'CRELEASETIME2', 'CURL',
             'DOCID', 'FILESIZE', 'MIMETYPE']
df = pd.DataFrame(columns=keep_cols)
df.to_csv('demo.csv', index=False, header=True)
one_page = [
    {'CCHANNELCODE': '9860', 'CONTENT': '2018 年第二期北京市基础设施投资有限公司公司债券募集说明书 1 声明及提示 一、发行人', 'CRELEASETIME': '2018-12-06',
     'CRELEASETIME2': '00:00:00', 'CSITECODE': '28',
     'CTITLE': '2018年第二期北京市基础设施投资有限公司公司<font color=#FF0000>债券募集说明书</font>',
     'CTITLE_TXT': '2018年第二期北京市基础设施投资有限公司公司债券募集说明书',
     'CURL': '/disclosure/bond/announcement/corporate/c/3414167252895919.pdf', 'DOCID': 'CMS4687754_28_9860',
     'FILESIZE': '921912', 'KEYWORD': None, 'MIMETYPE': 'pdf'},
    {'CCHANNELCODE': '8349', 'CONTENT': '股票简称：福能股份 股票代码：600483 福建福能股份有限公司 （住所：南平市安丰桥）', 'CRELEASETIME': '2018-12-05',
     'CRELEASETIME2': '17:49:47', 'CSITECODE': '28', 'CTITLE': '福能股份公开发行可转换公司<font color=#FF0000>债券募集说明书</font>',
     'CTITLE_TXT': '福能股份公开发行可转换公司债券募集说明书',
     'CURL': '/disclosure/listedinfo/announcement/c/2018-12-05/600483_20181205_5.pdf', 'DOCID': 'CMS4686872_1_599',
     'FILESIZE': '6072407', 'KEYWORD': None, 'MIMETYPE': 'pdf'},
    {'CCHANNELCODE': '8349', 'CONTENT': '股票简称：福能股份 股票代码： 600483 福建福能股份有限公司 （住所：南平市安丰桥）', 'CRELEASETIME': '2018-12-05',
     'CRELEASETIME2': '17:49:46', 'CSITECODE': '28', 'CTITLE': '福能股份公开发行可转换公司<font color=#FF0000>债券募集说明书</font>摘要',
     'CTITLE_TXT': '福能股份公开发行可转换公司债券募集说明书摘要',
     'CURL': '/disclosure/listedinfo/announcement/c/2018-12-05/600483_20181205_4.pdf', 'DOCID': 'CMS4686871_1_599',
     'FILESIZE': '2125597', 'KEYWORD': None, 'MIMETYPE': 'pdf'},
    {'CCHANNELCODE': '9860', 'CONTENT': '重要提示：本募集说明书全部内容遵循《中华人民共和国证券法》、《企业债券管理条例》', 'CRELEASETIME': '2018-12-05',
     'CRELEASETIME2': '00:00:00', 'CSITECODE': '28',
     'CTITLE': '2018年海宁市城市发展投资集团有限公司公司<font color=#FF0000>债券募集说明书</font>',
     'CTITLE_TXT': '2018年海宁市城市发展投资集团有限公司公司债券募集说明书',
     'CURL': '/disclosure/bond/announcement/corporate/c/3413202086731523.pdf', 'DOCID': 'CMS4686823_28_9860',
     'FILESIZE': '2551925', 'KEYWORD': None, 'MIMETYPE': 'pdf'},
    {'CCHANNELCODE': '9860', 'CONTENT': '2018年第二期兴义市信恒城市建设技资有 限公司公司债券 募集说明书 发行人 , ,11111 孩',
     'CRELEASETIME': '2018-12-05', 'CRELEASETIME2': '00:00:00', 'CSITECODE': '28',
     'CTITLE': '18年第二期兴义市信恒城市建设投资有限公司公司<font color=#FF0000>债券募集说明书</font>',
     'CTITLE_TXT': '2018年第二期兴义市信恒城市建设投资有限公司公司债券募集说明书',
     'CURL': '/disclosure/bond/announcement/corporate/c/3412467240861454.pdf', 'DOCID': 'CMS4686817_28_9860',
     'FILESIZE': '1964450', 'KEYWORD': None, 'MIMETYPE': 'pdf'},
    {'CCHANNELCODE': '9860', 'CONTENT': '2018 年第二期绵阳安州投资控股集团有限公司城市停车场建设专项债券募集说明书 2018年', 'CRELEASETIME': '2018-12-03',
     'CRELEASETIME2': '00:00:00', 'CSITECODE': '28',
     'CTITLE': '阳安州投资控股集团有限公司城市停车场建设专项<font color=#FF0000>债券募集说明书</font>',
     'CTITLE_TXT': '2018年第二期绵阳安州投资控股集团有限公司城市停车场建设专项债券募集说明书',
     'CURL': '/disclosure/bond/announcement/corporate/c/3409835734185655.pdf', 'DOCID': 'CMS4685458_28_9860',
     'FILESIZE': '3076828', 'KEYWORD': None, 'MIMETYPE': 'pdf'},
    {'CCHANNELCODE': '9860', 'CONTENT': '2018年第二期宿迁高新开发投资有限公司 公司债券募集说明书 发行人 宿迁高新开发投资有', 'CRELEASETIME': '2018-11-28',
     'CRELEASETIME2': '00:00:00', 'CSITECODE': '28',
     'CTITLE': '2018年第二期宿迁高新开发投资有限公司公司<font color=#FF0000>债券募集说明书</font>',
     'CTITLE_TXT': '2018年第二期宿迁高新开发投资有限公司公司债券募集说明书',
     'CURL': '/disclosure/bond/announcement/corporate/c/3407273739191125.pdf', 'DOCID': 'CMS4682914_28_9860',
     'FILESIZE': '895088', 'KEYWORD': None, 'MIMETYPE': 'pdf'},
    {'CCHANNELCODE': '9860', 'CONTENT': '1 声明及提示 一、发行人声明 发行人已批准本期债券募集说明书，承诺其中不存在虚假记', 'CRELEASETIME': '2018-11-28',
     'CRELEASETIME2': '00:00:00', 'CSITECODE': '28',
     'CTITLE': '区城市旅游开发投资有限公司城市停车场建设专项<font color=#FF0000>债券募集说明书</font>',
     'CTITLE_TXT': '2018年青岛市即墨区城市旅游开发投资有限公司城市停车场建设专项债券募集说明书',
     'CURL': '/disclosure/bond/announcement/corporate/c/3407254404195710.pdf', 'DOCID': 'CMS4682910_28_9860',
     'FILESIZE': '2312321', 'KEYWORD': None, 'MIMETYPE': 'pdf'},
    {'CCHANNELCODE': '9860', 'CONTENT': '十一 2018年第二期海宁市尖山新区开发有限公司公司债券募集说明书 I 重要声明及提示 一', 'CRELEASETIME': '2018-11-27',
     'CRELEASETIME2': '00:00:00', 'CSITECODE': '28',
     'CTITLE': '2018年第二期海宁市尖山新区开发有限公司公司<font color=#FF0000>债券募集说明书</font>',
     'CTITLE_TXT': '2018年第二期海宁市尖山新区开发有限公司公司债券募集说明书',
     'CURL': '/disclosure/bond/announcement/corporate/c/3406363031124768.pdf', 'DOCID': 'CMS4682259_28_9860',
     'FILESIZE': '1707646', 'KEYWORD': None, 'MIMETYPE': 'pdf'},
    {'CCHANNELCODE': '9860', 'CONTENT': 'I 重要声明及提示 一、发行人董事会声明 发行人董事会或股东会已批准本期债券募集说明', 'CRELEASETIME': '2018-11-27',
     'CRELEASETIME2': '00:00:00', 'CSITECODE': '28',
     'CTITLE': '2018年第二期华晨汽车集团控股有限公司公司<font color=#FF0000>债券募集说明书</font>',
     'CTITLE_TXT': '2018年第二期华晨汽车集团控股有限公司公司债券募集说明书',
     'CURL': '/disclosure/bond/announcement/corporate/c/3402991158708041.pdf', 'DOCID': 'CMS4682250_28_9860',
     'FILESIZE': '2251216', 'KEYWORD': None, 'MIMETYPE': 'pdf'}]
for data in one_page:
    data.pop('CSITECODE')
    data.pop('CTITLE')
    data.pop('KEYWORD')
    one_df = pd.DataFrame(data=data, index=[0])
    one_df.to_csv('demo.csv', mode='a', index=False, header=False, columns=keep_cols)
