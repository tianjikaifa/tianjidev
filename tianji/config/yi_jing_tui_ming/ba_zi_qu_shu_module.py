#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/12/22 10:47
# @Author  : huangfujue
# @File    : ba_zi_qu_shu_module.py
# @Date    : 2023/12/22 
"""
天地支配数
"""

# ----------------------------------------------------------------------------------------------------------------------
import json
import os

di_zhi_biao = {}
tian_gan_biao = {}

json_file = os.path.join(os.path.dirname(__file__), "../../data/jsonfile", "yi_jing_tian_gan_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    tian_gan_biao = json.load(f)

json_file = os.path.join(os.path.dirname(__file__), "../../data/jsonfile", "yi_jing_di_zhi_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    di_zhi_biao = json.load(f)
