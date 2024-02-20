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

from tianji.config.json_module import yue_xing_biao
from tianji.proj_config import my_dir




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
