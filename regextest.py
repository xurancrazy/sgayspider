# -*- coding: utf-8 -*-
import re

str = '日本AV女优桃谷绘里香、参演的作品番号ABP-138，该片（桃谷エリカがご奉仕しちゃう◆超最新やみつきエステ）时长 137分钟，本番号作品分类定义于：打手枪、 ，正式发片日期是2014-05-01'
res = re.search('定义于：.*正式发片',str,flags=0)
print(len(res.group()))
print(res.group(0))
str1=res.group(0)
str2=str1[4:-5]
print(str2)
str4=str2.split("、")
print(str4)
print(ord(' '))

s=''
print(len(s.strip()))