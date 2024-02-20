#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/14 22:49
# @Author  : huangfujue
# @File    : zi_nian_dou_jun_biao_module.py
# @Date    : 2023/11/14 
"""
用来根据月和时辰确定斗君在哪个宫起子，然后顺数
"""
import json
import os

from tianji.config.json_module import dou_jun_biao
# ----------------------------------------------------------------------------------------------------------------------
from tianji.config.zi_wei_dou_shu.shi_er_di_zhi_biao_module import Di_Zhi_Iter, di_zhi
from tianji.proj_config import my_dir

"""
用来根据月和时辰确定斗君在哪个宫起子，然后顺数流年到年支，哪个宫就是流年的斗君
"""


class Dou_jun:
    def __init__(self, yue, shi_zhi):
        """
        :param yue: 月份
        :param shi_zhi: 时辰
        """
        # shi_chen_biao = {
        #     1: "子",
        #     2: "丑",
        #     3: "寅",
        #     4: "卯",
        #     5: "辰",
        #     6: "巳",
        #     7: "午",
        #     8: "未",
        #     9: "申",
        #     10: "酉",
        #     11: "戌",
        #     12: "亥"
        # }
        #
        # self.__shi = shi_chen_biao.get(shi_zhi)
        self.__yue = yue
        self.__shi_zhi = shi_zhi

        # self.start_location = dou_jun_biao.get(str(self.__yue)).get(self.__shi_zhi)
        # self.di_zhi_iter = Di_Zhi_Iter(-1)
        # # 因为要按它起子，所以实际上要更新子的位置
        # self.di_zhi_iter.update(self.start_location)
        self.di_zhi_iter = Di_Zhi_Iter(-1)
        self.di_zhi_iter.update("子")
        for _ in range(1, self.__yue):
            self.di_zhi_iter.next()

        dd = Di_Zhi_Iter(-1)
        zhi = "子"
        dd.update(zhi)
        for i in range(12):
            if zhi == shi_zhi:
                self.start_location = self.di_zhi_iter.now()
                break
            zhi = dd.up()
            self.di_zhi_iter.up()

    def get_liu_nian_location(self, liu_nian_nian_zhi):
        self.di_zhi_iter.update(self.start_location)
        for zhi in di_zhi.values():
            if zhi == liu_nian_nian_zhi:
                break
            else:
                self.di_zhi_iter.up()  # 顺数

        return self.di_zhi_iter.now()


if __name__ == '__main__':
    yue = 1
    shi_zhi = "卯"
    nian_zhi = "寅"
    dou_jun = Dou_jun(yue, shi_zhi)
    print(dou_jun.start_location)
    print(f"流年{nian_zhi} {dou_jun.start_location} 流年之斗君所在的宫 {dou_jun.get_liu_nian_location(nian_zhi)}")
