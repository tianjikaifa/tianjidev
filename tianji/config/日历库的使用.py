#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/15 23:55
# @Author  : huangfujue
# @File    : 日历库的使用.py
# @Date    : 2023/11/15 
"""
模块说明
"""
from datetime import datetime
import time

# ----------------------------------------------------------------------------------------------------------------------
import  sxtwl

Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]

nong_Li=(2023,11,16)
# 从农历年月日获取一天的信息
day = sxtwl.fromLunar(2023, 11, 30)
day = sxtwl.fromSolar(2023, 11, 8)

s = "公历:%d年%d月%d日" % (day.getSolarYear(), day.getSolarMonth(), day.getSolarDay())
print(s)
# 以立春为界的天干地支 （注，如果没有传参，或者传false，是以立春为界的。刚好和getLunarYear相反）
yTG = day.getYearGZ(False)
print("以立春为界的年干支", Gan[yTG.tg] + Zhi[yTG.dz])
#月干支
mTG = day.getMonthGZ()
print("月干支", Gan[mTG.tg] + Zhi[mTG.dz])
#日干支
dTG  = day.getDayGZ()
print("日干支", Gan[dTG.tg] + Zhi[dTG.dz])


#时干支,传24小时制的时间，分早晚子时
hour = 18
sTG = day.getHourGZ(hour)
print("%d时的干支"%(hour, ), Gan[sTG.tg] + Zhi[sTG.dz])


# #时干支
for hour in range(24):
    # 第一个参数为该天的天干，第二个参数为小时
    hTG  = sxtwl.getShiGz(dTG.tg, hour)
    print('{}:"{}"'.format(hour, Gan[hTG.tg] + Zhi[hTG.dz]))


jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏",
     "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑","白露", "秋分", "寒露", "霜降",
     "立冬", "小雪", "大雪"]
# 当日是否有节气
if day.hasJieQi():
    print('节气：%s'% jqmc[day.getJieQi()])
    #获取节气的儒略日数
    jd = day.getJieQiJD()
    # 将儒略日数转换成年月日时秒
    t = sxtwl.JD2DD(jd )
    print(t)
    # 注意，t.s是小数，需要四舍五入
    now_str="%d-%d-%d %d:%d:%d"%(t.Y, t.M, t.D, t.h, t.m, round(t.s))
    print(now_str)
    #s_t=time.strftime(now_str,"%Y-%m-%d %H:%M:%s")
    s_t=time.strftime(now_str)
    print(s_t)
    # mkt=time.mktime(s_t)
    # print(mkt)
    print("----")
    mkt= time.mktime(s_t)

    print(mkt.__format__("%Y-%m-%d %H:%M:%S"))
    print(mkt)
    mkt=time.localtime(mkt)
    print(time.strftime("%Y-%m-%d %H:%M:%S",mkt))


else:
    print("当天不是节气日")

print(datetime.timestamp())
