#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/14 12:48
# @Author  : huangfujue
# @File    : chang_sheng_shi_er_xing_module.py
# @Date    : 2023/11/14 
"""
根据五行局，男女和阳阴确定长生十二星所在的宫
"""
# ----------------------------------------------------------------------------------------------------------------------


import json
import os

json_file=os.path.join(os.path.dirname(__file__),"jsonfile","chang_sheng_shi_er_xing_biao.json")
chang_sheng_shi_er_xing_biao=None
with open(json_file, "r", encoding="utf-8") as f:
    chang_sheng_shi_er_xing_biao = json.load(f)

if __name__ == '__main__':
    d = chang_sheng_shi_er_xing_biao
    for star in ["长生", "沐浴", "冠带", "临官", "帝旺", "衰", "病", "死", "墓", "绝", "胎", "养", ]:
        print(star, [[d.get(jv).get("阳男").get(star),d.get(jv).get("阴男").get(star)] for jv in ["水二局", "木三局", "金四局", "土五局", "火六局"]])
