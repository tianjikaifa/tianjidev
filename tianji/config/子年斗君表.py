#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/14 22:49
# @Author  : huangfujue
# @File    : 子年斗君表.py
# @Date    : 2023/11/14 
"""
用来根据月和时辰确定斗君在哪个宫起子，然后顺数
"""

# ----------------------------------------------------------------------------------------------------------------------
from tianji.config.十二支所属表 import Di_Zhi_Iter, di_zhi

"""
用来根据月和时辰确定斗君在哪个宫起子，然后顺数流年到年支，哪个宫就是流年的斗君
"""


class Dou_jun:
    def __init__(self, yue, shi):
        """
        :param yue: 月份
        :param shi: 时辰
        """
        shi_chen_biao = {
            1: "子",
            2: "丑",
            3: "寅",
            4: "卯",
            5: "辰",
            6: "巳",
            7: "午",
            8: "未",
            9: "申",
            10: "酉",
            11: "戌",
            12: "亥"
        }
        self.__yue = yue
        self.__shi = shi_chen_biao.get(shi)
        # 子年斗君表
        biao = {
            1: {
                "子": "子",
                "丑": "丑",
                "寅": "寅",
                "卯": "卯",
                "辰": "辰",
                "巳": "巳",
                "午": "午",
                "未": "未",
                "申": "申",
                "酉": "酉",
                "戌": "戌",
                "亥": "亥"},
            2: {
                "子": "亥",
                "丑": "子",
                "寅": "丑",
                "卯": "寅",
                "辰": "卯",
                "巳": "辰",
                "午": "巳",
                "未": "午",
                "申": "未",
                "酉": "申",
                "戌": "酉",
                "亥": "戌"},
            3: {
                "子": "戌",
                "丑": "亥",
                "寅": "子",
                "卯": "丑",
                "辰": "寅",
                "巳": "卯",
                "午": "辰",
                "未": "巳",
                "申": "午",
                "酉": "未",
                "戌": "申",
                "亥": "酉"},
            4: {
                "子": "酉",
                "丑": "戌",
                "寅": "亥",
                "卯": "子",
                "辰": "丑",
                "巳": "寅",
                "午": "卯",
                "未": "辰",
                "申": "巳",
                "酉": "午",
                "戌": "未",
                "亥": "申"},
            5: {
                "子": "申",
                "丑": "酉",
                "寅": "戌",
                "卯": "亥",
                "辰": "子",
                "巳": "丑",
                "午": "寅",
                "未": "卯",
                "申": "辰",
                "酉": "巳",
                "戌": "午",
                "亥": "未"},
            6: {
                "子": "未",
                "丑": "申",
                "寅": "酉",
                "卯": "戌",
                "辰": "亥",
                "巳": "子",
                "午": "丑",
                "未": "寅",
                "申": "卯",
                "酉": "辰",
                "戌": "巳",
                "亥": "午"},
            7: {
                "子": "午",
                "丑": "未",
                "寅": "申",
                "卯": "酉",
                "辰": "戌",
                "巳": "亥",
                "午": "子",
                "未": "丑",
                "申": "寅",
                "酉": "卯",
                "戌": "辰",
                "亥": "巳"},
            8: {
                "子": "巳",
                "丑": "午",
                "寅": "未",
                "卯": "申",
                "辰": "酉",
                "巳": "戌",
                "午": "亥",
                "未": "子",
                "申": "丑",
                "酉": "寅",
                "戌": "卯",
                "亥": "辰"},
            9: {
                "子": "辰",
                "丑": "巳",
                "寅": "午",
                "卯": "未",
                "辰": "申",
                "巳": "酉",
                "午": "戌",
                "未": "亥",
                "申": "子",
                "酉": "丑",
                "戌": "寅",
                "亥": "卯"},
            10: {
                "子": "卯",
                "丑": "辰",
                "寅": "巳",
                "卯": "午",
                "辰": "未",
                "巳": "申",
                "午": "酉",
                "未": "戌",
                "申": "亥",
                "酉": "子",
                "戌": "丑",
                "亥": "寅"},
            11: {
                "子": "寅",
                "丑": "卯",
                "寅": "辰",
                "卯": "巳",
                "辰": "午",
                "巳": "未",
                "午": "申",
                "未": "酉",
                "申": "戌",
                "酉": "亥",
                "戌": "子",
                "亥": "丑"},
            12: {
                "子": "丑",
                "丑": "寅",
                "寅": "卯",
                "卯": "辰",
                "辰": "巳",
                "巳": "午",
                "午": "未",
                "未": "申",
                "申": "酉",
                "酉": "戌",
                "戌": "亥",
                "亥": "子"},
        }
        self.start_location = biao.get(self.__yue).get(self.__shi)
        self.di_zhi_iter = Di_Zhi_Iter(-1)
        # 因为要按它起子，所以实际上要更新子的位置
        self.di_zhi_iter.update(self.start_location)

    def get_liu_nian_location(self, liu_nian_nian_zhi):
        for zhi in di_zhi.values():
            if zhi == liu_nian_nian_zhi:
                break
            else:
                self.di_zhi_iter.next()  # 顺数

        return self.di_zhi_iter.now()


if __name__ == '__main__':
    yue = 7
    shi = 1
    nian_zhi = "寅"
    dou_jun = Dou_jun(yue, shi)
    print(f"流年{nian_zhi} {dou_jun.start_location} 流年之斗君所在的宫 {dou_jun.get_liu_nian_location(nian_zhi)}")
