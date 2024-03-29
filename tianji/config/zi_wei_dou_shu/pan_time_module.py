#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/20 0:59
# @Author  : huangfujue
# @File    : pan_time_module.py
# @Date    : 2023/11/20 
"""
模块说明
"""

# ----------------------------------------------------------------------------------------------------------------------
import datetime
from lunar_python import Lunar, Solar


class PanTime:
    """
    表示紫微斗数的一个排盘时间,使用农历时间作为输入
    """

    def __init__(self, nian, yue, ri, shi):
        """
        默认农历
        :param nian: 农历年
        :param yue: 农历月
        :param ri: 农历日
        :param shi: 几点,1点以后2点之前输入1,
        """

        self.nian = nian

        self.yue = yue
        self.ri = ri
        self.shi = shi
        self.day_info = Lunar(nian, yue, ri, shi, 0, 0)
        # 紫微斗数排盘时年与年之间是按正月初一分割的，而不是春分，所以年的天干地支在排的时候要按
        current_bazi = Lunar(nian, 6, 6, 12, 0, 0).getBaZi()

        self.current_year_ntg = current_bazi[0][0]
        self.current_year_ndz = current_bazi[0][1]

        y, m, d = self.lunar_to_solar()
        self.xin_li_y = y
        self.xin_li_m = m
        self.xin_li_d = d

    def get_ba_zi(self):
        bazi = self.day_info.getBaZi()

        # 因为紫微斗数的年实际要按
        self.ntg = bazi[0][0]
        self.ndz = bazi[0][1]
        self.ytg = bazi[1][0]
        self.ydz = bazi[1][1]
        self.rtg = bazi[2][0]
        self.rdz = bazi[2][1]
        self.stg = bazi[3][0]
        self.sdz = bazi[3][1]
        return [self.ntg, self.ndz, self.ytg, self.ydz, self.rtg, self.rdz, self.stg, self.sdz]

    def lunar_to_solar(self):
        """
        农历转新历,时间是不变的
        :param nian:
        :param yue:
        :param ri:
        :return:
        """

        y = self.day_info.getSolar().getYear()
        m = self.day_info.getSolar().getMonth()
        d = self.day_info.getSolar().getDay()
        return y, m, d

    def liu_nian_ba_zi(self):
        t = datetime.datetime.now()
        y, m, d = PanTime.solar_to_lunar(t.year, t.month, t.day)
        t = PanTime(y, m, d, 3)
        return t.get_ba_zi()

    def is_xia_zhi_qian(self):
        """
        判断指定日期是否是冬至以后夏至以前（阳令）
        之所以是阳令是因为阳气从这开始复苏
        :param y: 年份
        :param m:
        :param d:
        :param H:
        :param M:
        :param S:
        :return:
        """
        # 节气的公历时间表
        jieqi1 = Lunar.fromYmd(self.nian, 8, 1).getJieQiTable()
        chushengri = self.day_info.getSolar()
        summer_before = chushengri.isBefore(jieqi1.get("夏至"))
        #print(chushengri,jieqi1.get("夏至"))
        return summer_before

    @staticmethod
    def solar_to_lunar(nian, yue, ri):
        """
               新历转农历
               :param nian:
               :param yue:
               :param ri:
               :return:
               """
        s = Solar.fromYmd(nian, yue, ri)
        l = Lunar.fromSolar(s)

        y = l.getYear()
        m = l.getMonth()
        d = l.getDay()

        return y, m, d






