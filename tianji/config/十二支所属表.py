#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/12 18:25
# @Author  : huangfujue
# @File    : 十二支所属表.py
# @Date    : 2023/11/12 
"""
描述十二地支的阴阳五行和生肖
"""
# ----------------------------------------------------------------------------------------------------------------------
# 表示十二地支的迭代器
class Di_Zhi_Iter:

    def __init__(self, yue):
        current = yue + 2  # 因为时机是从寅宫开始的算一月，这里的1-12没有意义，只是为了好算
        if current > 12:
            current = current - 12
        self.__current = current

    def update(self, current_location):
        """
        根据命宫在那个宫更新此人的迭代器，用于后面的余宫使用
        也会在别的方面用到
        :param current_location:设置当前位置
        :return:
        """
        flag=True
        for k in di_zhi:
            dizhi = di_zhi.get(k)
            if dizhi == current_location:
                self.__current = int(k)
                flag=False
                break
        if flag:
            raise Exception("给定非有效地支")

    def next(self):
        self.__current += 1
        if self.__current > 12:
            self.__current = 1

        return di_zhi.get(str(self.__current))

    def now(self):
        return di_zhi.get(str(self.__current))

    def up(self):
        self.__current -= 1
        if self.__current < 1:
            self.__current = 12

        return di_zhi.get(str(self.__current))


class Shi_Er_Zhi:
    def __init__(self,di_zhi,yin_yang,wu_xing,sheng_xiao):
        self.di_zhi=di_zhi
        self.yin_yang=yin_yang
        self.wu_xing=wu_xing
        self.sheng_xiao=sheng_xiao


shi_er_di_zhi_biao={

    "子":Shi_Er_Zhi("子","阳","水","鼠"),
    "丑":Shi_Er_Zhi("丑","阴","土","牛"),
    "寅":Shi_Er_Zhi("寅","阳","木","虎"),
    "卯":Shi_Er_Zhi("卯","阴","木","兔"),
    "辰":Shi_Er_Zhi("辰","阳","土","龙"),
    "巳":Shi_Er_Zhi("巳","阴","火","蛇"),
    "午":Shi_Er_Zhi("午","阳","火","马"),
    "未":Shi_Er_Zhi("未","阴","土","羊"),
    "申":Shi_Er_Zhi("申","阳","金","猴"),
    "酉":Shi_Er_Zhi("酉","阴","金","鸡"),
    "戌":Shi_Er_Zhi("戌","阳","土","狗"),
    "亥":Shi_Er_Zhi("亥","阴","水","猪"),

}

di_zhi = {
    "1": "子",
    "2": "丑",
    "3": "寅",
    "4": "卯",
    "5": "辰",
    "6": "巳",
    "7": "午",
    "8": "未",
    "9": "申",
    "10": "酉",
    "11": "戌",
    "12": "亥"
}