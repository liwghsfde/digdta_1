# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:43:14 2018

@author: lenovo
"""

import urllib.request as r
city_pinyin=input("请输入城市拼音：")
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996 

'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)

#json(dict)格式工具包
import json
data=json.loads(info)
wendu=data['main']['temp']
print("温度:"+str(wendu))
zuidi=data['main']['temp_min']
print("最低温度:"+str(zuidi))
zuigao=data['main']['temp_max']
print("最高温度:"+str(zuigao))
qiya=data['main']['pressure']
print("气压:"+str(qiya))
shidu=data['main']['humidity']
print("湿度:"+str(shidu))
qingkuang=data['weather'][0]['description']
print("天气情况:"+str(qingkuang))
9:42:18
15  2018/6/3 9:42:18
weather={'日期':['6.2','6.3','6.4','6.5','6.6'],
         '天气情况':['小雨','多云','晴','晴','多云'],
         '温度':['25','24','28','30','31']}
print("未来五天最高温度"+max(weather['温度']))
weeks=['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
print('今天是：'+weeks[5])
