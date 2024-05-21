#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2024-05-21 13:22
# @Author  : huangfujue
# @File    : pai_liu_ren.py
# @Date    : 2024-05-21 
"""
用来表示小六壬的排盘结果
"""
# ----------------------------------------------------------------------------------------------------------------------
from datetime import datetime
from lunar_python import Lunar, Solar


class Xiao_Liu_Ren:
    liu_shen = ["大安", "流连", "速喜", "赤口", "小吉", "空亡"]

    def __init__(self, yue, ri, shi):
        """
        需要输入的是农历的月日还有时辰
        :param yue:
        :param ri:
        :param shi:
        """
        self.yue = yue
        self.ri = ri
        self.shi = shi

        self.index = 0
        for i in range(yue - 1):
            self.next()

        self.yue_shen = self.current()

        for i in range(ri - 1):
            self.next()

        self.ri_shen = self.current()

        for i in range(shi - 1):
            self.next()

        self.shi_shen = self.current()

    def current(self):

        return Xiao_Liu_Ren.liu_shen[self.index]

    def next(self):
        temp = self.index + 1
        self.index = 0 if temp > 5 else temp

    def up(self):
        temp = self.index - 1
        self.index = 5 if temp < 0 else temp

    def __next__(self):
        self.next()


def pai_liu_ren(date=None):
    """
    根据给定的日期（新历）对象排六壬
    :param date: datetime 对象
    :return: {
        "yue": yue_shen,
        "ri": p.ri_shen,
        "shi": p.shi_shen
    }
    """
    d = datetime.now() if date is None else date
    lu = Lunar.fromSolar(Solar(d.year, d.month, d.day, d.hour, d.minute, d.second))
    yue = abs(lu.getMonth())
    ri = lu.getDay()
    shi_zi = lu.getBaZi()[3][1]
    print(lu)
    print(lu.getBaZi())
    shi_biao = {
        "子": 1,
        "丑": 2,
        "寅": 3,
        "卯": 4,
        "辰": 5,
        "巳": 6,
        "午": 7,
        "未": 8,
        "申": 9,
        "酉": 10,
        "戌": 11,
        "亥": 12
    }

    p = Xiao_Liu_Ren(yue=yue, ri=ri, shi=shi_biao.get(shi_zi))

    return {
        "月令": p.yue_shen,
        "日令": p.ri_shen,
        "时令": p.shi_shen,
        "时间": f"{lu} {shi_zi}时",
        "八字": "".join(lu.getBaZi())
    }


def nong_li_pai(date=None):
    """
    根据农历排六壬
    :param date:
    :return:
    """
    d = date
    lu = Lunar.fromSolar(d.year, d.month, d.day, d.hour, d.minute, d.second)
    d = lu.getSolar()
    new_date = datetime(d.getYear(), d.getMonth(), d.getDay(), d.getHour())
    return pai_liu_ren(new_date)


if __name__ == '__main__':
    print(pai_liu_ren())

    print(pai_liu_ren(datetime(2024, 5, 21, 13)))
