#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/13 21:48
# @Author  : huangfujue
# @File    : ri_xi_zhu_xing_biao_module.py
# @Date    : 2023/11/13 
"""
结合其他星耀位置根据出生日计算另外的相关的想要位置
"""

# ----------------------------------------------------------------------------------------------------------------------
from tianji.config.shi_er_di_zhi_biao_module import Di_Zhi_Iter

"""
用来表示根据一个星耀所在位置和出生日计算另一个星耀
用来计算以下星耀位置
三台
八座
恩光
天贵

"""


class CalculateLocation:

    def __init__(self, start_location, day, star_name="八座"):
        """
        :param start_location:  基于哪个星耀计算，给出这个星耀所在的宫
        :param day: 出生日
        :param is_next: 是否是顺行，默认顺行
        """
        self.start_localction = start_location
        if day < 1 or day > 30:
            raise Exception("请给出初一到30的时间，而不是一个无法识别的东西，当前是{}".format(day))
        self.__day = day
        # 只有八座需要逆着算
        self.__is_next = False if star_name == "八座" else True
        self.__name = star_name
        iter = Di_Zhi_Iter(0)
        # 传入星耀所在位置作为开始位置
        iter.update(start_location)
        self.__geter = iter

    def calculate(self):
        """
        获取星耀位置
        :return:
        """
        for _ in range(1, self.__day):
            if self.__is_next:
                self.__geter.next()
            else:
                self.__geter.up()
        if self.__name == "恩光" or self.__name == "天贵":
            self.__geter.up()  # 这两个顺行并且后退一步，那就是往上呗

        return self.__geter.now()


if __name__ == '__main__':
    cal = CalculateLocation("辰", 8,  "天贵")
    print(cal.calculate())
