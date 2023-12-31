#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/13 21:29
# @Author  : huangfujue
# @File    : yue_xi_zhu_xing_biao_module.py
# @Date    : 2023/11/13 
"""
根据出生月份确定的星耀,如果出生的月份是
"""
# ----------------------------------------------------------------------------------------------------------------------
import json
import os

from tianji.proj_config import my_dir

json_file = os.path.join(my_dir, "data","jsonfile", "yue_xing_biao.json")
yue_xing_biao = None
with open(json_file, "r", encoding="utf-8") as f:
    yue_xing_biao = json.load(f)



if __name__ == '__main__':
    for start in [
        "左辅",
        "右弼",
        "天刑",
        "天姚",
        "天巫",
        "天月",
        "阴煞",
    ]:
        print(start,[yue_xing_biao.get(str(yue) ).get(start)  for yue in range(1,13)])
