#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/13 18:28
# @Author  : huangfujue
# @File    : zhu_xing_biao_module.py
# @Date    : 2023/11/13 
"""

紫微星的位置定下来后，其余的13个主星也会随着定下来
这个表是北斗星君表和南斗星表

"""
# ----------------------------------------------------------------------------------------------------------------------
import json
import os

from tianji.config.json_module import bei_dou_zhu_xing_biao, nan_dou_zhu_xing_biao
from tianji.proj_config import my_dir

# 紫微星所在的宫为键，对应星辰的名称取值为对应位置,
# 其中包含了没指定的南斗星君-天府星，但是天府星不在北斗星系里


if __name__ == '__main__':
    from tianji.config.zi_wei_dou_shu.shi_er_di_zhi_biao_module import di_zhi

    for gong in di_zhi.values():
        print("-----" * 20 + "\n紫微星在{}".format(gong))

        for item in ["天机", "太阳", "武曲", "天同", "廉贞", "天府"]:
            print(f"{item} => {bei_dou_zhu_xing_biao.get(gong).get(item)}")

    for gong in di_zhi.values():
        print("-----" * 20 + "\n天府星在{}".format(gong))

        for item in ["太阴", "贪狼", "巨门", "天相", "天梁", "七杀", "破军"]:
            print(f"{item} => {nan_dou_zhu_xing_biao.get(gong).get(item)}")
