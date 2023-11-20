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
import sxtwl
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
        self.day_info = sxtwl.fromLunar(self.nian, self.yue, self.ri)
        self.get_ba_zi()

    def get_ba_zi(self):
        Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        # ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]

        # yTG = self.day_info.getYearGZ(False) # 按春节这天作为两年分割线
        yTG = self.day_info.getYearGZ(True)  # 按春分这天作为两年的分割线
        mTG = self.day_info.getMonthGZ()
        dTG = self.day_info.getDayGZ()
        self.ntg = Gan[yTG.tg]
        self.ndz = Zhi[yTG.dz]

        self.ytg = Gan[mTG.tg]
        self.ydz = Zhi[mTG.dz]

        self.rtg = Gan[dTG.tg]
        self.rdz = Zhi[dTG.dz]

        # 时干支
        hTG = sxtwl.getShiGz(dTG.tg, self.shi)
        self.stg = Gan[hTG.tg]
        self.sdz = Zhi[hTG.dz]
        return [self.ntg, self.ndz, self.ytg, self.ydz, self.rtg, self.rdz, self.stg, self.sdz]

    def lunar_to_solar(self):
        """
        农历转新历,时间是不变的
        :param nian:
        :param yue:
        :param ri:
        :return:
        """

        y = self.day_info.getSolarYear()
        m = self.day_info.getSolarMonth()
        d = self.day_info.getSolarDay()
        return y, m, d

    def get_jie_qi(self):
        """
        获取这一天是不是节气，因为涉及到跨年
        :return:
        """
        jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏",
                "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
                "立冬", "小雪", "大雪"]
        if self.day_info.hasJieQi():
            # print('节气：%s' % jqmc[self.day_info.getJieQi()])
            # 获取节气的儒略日数
            jd = self.day_info.getJieQiJD()
            # 将儒略日数转换成年月日时秒
            t = sxtwl.JD2DD(jd)

            # 注意，t.s是小数，需要四舍五入
            # print("节气时间:%d-%d-%d %d:%d:%d" % (t.Y, t.M, t.D, t.h, t.m, round(t.s)))
            return True, jqmc[self.day_info.getJieQi()], (t.Y, t.M, t.D, t.h, t.m, round(t.s))
        else:
            return False, None, None

    @staticmethod
    def solar_to_lunar(nian, yue, ri):
        """
        新历转农历
        :param nian:
        :param yue:
        :param ri:
        :return:
        """
        day = sxtwl.fromSolar(nian, yue, ri)
        y = day.getLunarYear()
        m = day.getLunarMonth()
        d = day.getLunarDay()
        return y, m, d
