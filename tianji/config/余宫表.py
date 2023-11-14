#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/12 20:01
# @Author  : huangfujue
# @File    : 余宫表.py
# @Date    : 2023/11/12 
"""
定下命宫之后，按命宫逆转去确定以下的宫的分别在哪12个地支上

父母
福德
田宅
事业
友仆
迁移
疾厄
财帛
子女
夫妻
兄弟

"""

# ----------------------------------------------------------------------------------------------------------------------
from tianji.config.命宫身宫表 import Di_Zhi_Iter


class Yu_Gong:

    def __init__(self, ming):

        dizhi = Di_Zhi_Iter(1)
        dizhi.update(ming)

        self.__setattr__(ming,"命")
        self.__setattr__(dizhi.next(),"父母")
        self.__setattr__(dizhi.next(), "福德")
        self.__setattr__(dizhi.next(), "田宅")
        self.__setattr__(dizhi.next(), "事业")
        self.__setattr__(dizhi.next(), "友仆")
        self.__setattr__(dizhi.next(), "迁移")
        self.__setattr__(dizhi.next(), "疾厄")
        self.__setattr__(dizhi.next(), "财帛")
        self.__setattr__(dizhi.next(), "子女")
        self.__setattr__(dizhi.next(), "夫妻")
        self.__setattr__(dizhi.next(), "兄弟")


if __name__ == '__main__':
    命宫="申"
    y = Yu_Gong(命宫)
    dizhi = Di_Zhi_Iter(1)
    dizhi.update(命宫)
    for i in  range(12):
        temp=dizhi.next()
        print(temp, y.__getattribute__(temp))

