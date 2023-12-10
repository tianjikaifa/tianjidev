#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/20 0:59
# @Author  : huangfujue
# @File    : PanTime.py
# @Date    : 2023/11/20 
"""
模块说明
"""



# ----------------------------------------------------------------------------------------------------------------------
from lunar_python import Lunar, Solar


class PanTime:
    """
    表示紫薇斗数的一个排盘时间,使用农历时间作为输入
    """

    def __init__(self, nian, yue, ri, shi):
        """
        默认农历
        :param nian: 农历年
        :param yue: 农历月
        :param ri: 农历日
        :param shi: 几点,会转化成时辰
        """

        self.nian = nian
        self.yue = yue
        self.ri = ri
        self.shi = shi
        self.day_info =Lunar(nian,yue,ri,shi,0,0)


    def get_ba_zi(self):
        bazi = self.day_info.getBaZi()
        self.ntg=bazi[0][0]
        self.ndz=bazi[0][1]
        self.ytg=bazi[1][0]
        self.ydz=bazi[1][1]
        self.rtg=bazi[2][0]
        self.rdz=bazi[2][1]
        self.stg=bazi[3][0]
        self.sdz=bazi[3][1]
        return [self.ntg, self.ndz, self.ytg, self.ydz, self.rtg, self.rdz, self.stg, self.sdz]


    def lunar_to_solar(self):
        """
        农历转新历,时间是不变的
        :param nian:
        :param yue:
        :param ri:
        :return:
        """

        y=self.day_info.getSolar().getYear()
        m=self.day_info.getSolar().getMonth()
        d=self.day_info.getSolar().getYear()
        return y, m, d

    @staticmethod
    def solar_to_lunar(nian, yue, ri):
        """
               新历转农历
               :param nian:
               :param yue:
               :param ri:
               :return:
               """
        s = Solar(1998, 1, 31, 6, 0, 0)
        l = Lunar.fromSolar(s)

        y = l.getYear()
        m = l.getMonth()
        d = l.getDay()

        return y, m, d



