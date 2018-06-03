# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 10:55:37 2018

@author: lenovo
"""

import urllib.request as r
city_pinyin=input("请输入城市拼音：")
address='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)
print("欢迎使用本应用查看天气信息")

#json(dict)格式工具包
import json
tianqi=json.loads(info)
for i in range(38):
    riqi=tianqi['list'][i]['dt_txt']
    print("日期和时间:"+str(riqi))
    wendu=tianqi['list'][i]['main']['temp']
    print("温度:"+str(wendu)+"开氏度")
    zuidi=tianqi['list'][i]['main']['temp_min']
    print("最低温度:"+str(zuidi)+"开氏度")
    uigao=tianqi['list'][i]['main']['temp_max']
    print("最高温度:"+str(zuigao)+"开氏度")
    qiya=tianqi['list'][i]['main']['pressure']
    print("气压:"+str(qiya)+"pa")
    qingkuang=tianqi['list'][i]['weather'][0]['description']
    print("天气情况:"+str(qingkuang))
    print("********************************************")
