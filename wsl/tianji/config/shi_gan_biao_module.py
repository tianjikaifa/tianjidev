#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/12 18:14
# @Author  : huangfujue
# @File    : shi_gan_biao_module.py
# @Date    : 2023/11/12 
"""
阳年生男女为阳男阳女，阴年生男女为阴男阴女
"""


# ----------------------------------------------------------------------------------------------------------------------

class Shi_Gan:
    def __init__(self, tian_gan, yin_yang, wu_xing):
        self.tian_gan = tian_gan
        self.yin_yang = yin_yang
        self.wu_xing = wu_xing


# 表示十天干的迭代器
class Tian_Gan_Iter:

    def __init__(self, start):
        self.update(start)

    def next(self):
        self.current += 1
        if self.current > 10:
            self.current = 1

        return tian_gan.get(str(self.current))

    def now(self):
        return tian_gan.get(str(self.current))

    def up(self):
        self.current -= 1
        if self.current < 1:
            self.current = 10

        return tian_gan.get(str(self.current))

    def update(self, start):
        """
        设置天干起始位置
        :param start:
        :return:
        """
        flag = True
        for k in tian_gan:
            t = tian_gan.get(k)
            if t == start:
                self.current = int(k)
                flag = False
                break
        if flag:
            raise Exception("给定非有效天干{}".format(start))


shi_gan_biao = {
    "甲": Shi_Gan("甲", "阳", "木"),
    "乙": Shi_Gan("乙", "阴", "木"),
    "丙": Shi_Gan("丙", "阳", "火"),
    "丁": Shi_Gan("丁", "阴", "火"),
    "戊": Shi_Gan("戊", "阳", "土"),
    "己": Shi_Gan("己", "阴", "土"),
    "庚": Shi_Gan("庚", "阳", "金"),
    "辛": Shi_Gan("辛", "阴", "金"),
    "壬": Shi_Gan("壬", "阳", "水"),
    "葵": Shi_Gan("葵", "阴", "水"),
}

# 天干
tian_gan = {
    "1": "甲",
    "2": "乙",
    "3": "丙",
    "4": "丁",
    "5": "戊",
    "6": "己",
    "7": "庚",
    "8": "辛",
    "9": "壬",
    "10": "葵",
}




