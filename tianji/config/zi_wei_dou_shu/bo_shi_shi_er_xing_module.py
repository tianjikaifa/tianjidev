#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/15 13:47
# @Author  : huangfujue
# @File    : bo_shi_shi_er_xing_module.py
# @Date    : 2023/11/15 
"""
禄存星在哪，博士就在哪，
寻禄存星起博士，阳男阴女顺行，阴男阳女逆行。按顺序排下这些星
博 士--> 力士 青龙 小耗 将军 奏书 飞廉 喜神 病符 大耗 伏兵 官府

"""

# ----------------------------------------------------------------------------------------------------------------------
from tianji.config.zi_wei_dou_shu.shi_er_di_zhi_biao_module import Di_Zhi_Iter


class Bo_Shi_Shi_Er_Xing:
    def __init__(self, lu_cun_location, yin_yang_nan_nv="阳男"):
        self.__lu_cun_location = lu_cun_location
        di_zhi_iter = Di_Zhi_Iter(-1)
        di_zhi_iter.update(lu_cun_location)
        func = di_zhi_iter.up if (yin_yang_nan_nv == "阳男") or (yin_yang_nan_nv == "阴女") else di_zhi_iter.next
        self.__setattr__("博士", lu_cun_location)
        self.__setattr__("力士", func())
        self.__setattr__("青龙", func())
        self.__setattr__("小耗", func())
        self.__setattr__("将军", func())
        self.__setattr__("奏书", func())
        self.__setattr__("飞廉", func())
        self.__setattr__("喜神", func())
        self.__setattr__("病符", func())
        self.__setattr__("大耗", func())
        self.__setattr__("伏兵", func())
        self.__setattr__("官府", func())


if __name__ == '__main__':
    lu_cun_location = "巳"
    yin_yang_nan_nv = "阳男"
    bo = Bo_Shi_Shi_Er_Xing(lu_cun_location, yin_yang_nan_nv)
    print("博士  ", "力士  ", "青龙  ", "小耗  ", "将军  ", "奏书  ", "飞廉  ", "喜神  ", "病符  ", "大耗  ", "伏兵  ", "官府\n",
          [bo.__getattribute__(att)
           for att in ["博士", "力士", "青龙", "小耗", "将军", "奏书", "飞廉", "喜神", "病符", "大耗", "伏兵", "官府"]])
