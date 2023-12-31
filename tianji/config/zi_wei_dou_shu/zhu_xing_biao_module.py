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

from tianji.proj_config import my_dir

# 紫微星所在的宫为键，对应星辰的名称取值为对应位置,
# 其中包含了没指定的南斗星君-天府星，但是天府星不在北斗星系里
# bei_dou_zhu_xing_biao = {
#     "子": {
#         "天机": "亥",
#         "太阳": "酉",
#         "武曲": "申",
#         "天同": "未",
#         "廉贞": "辰",
#         "天府": "辰",
#     },
#     "丑": {
#         "天机": "子",
#         "太阳": "戌",
#         "武曲": "酉",
#         "天同": "申",
#         "廉贞": "巳",
#         "天府": "卯",
#     },
#     "寅": {
#         "天机": "丑",
#         "太阳": "亥",
#         "武曲": "戌",
#         "天同": "酉",
#         "廉贞": "午",
#         "天府": "寅",
#     },
#     "卯": {
#         "天机": "寅",
#         "太阳": "子",
#         "武曲": "亥",
#         "天同": "戌",
#         "廉贞": "未",
#         "天府": "丑",
#     },
#     "辰": {
#         "天机": "卯",
#         "太阳": "丑",
#         "武曲": "子",
#         "天同": "亥",
#         "廉贞": "申",
#         "天府": "子",
#     },
#     "巳": {
#         "天机": "辰",
#         "太阳": "寅",
#         "武曲": "丑",
#         "天同": "子",
#         "廉贞": "酉",
#         "天府": "亥",
#     },
#     "午": {
#         "天机": "巳",
#         "太阳": "卯",
#         "武曲": "寅",
#         "天同": "丑",
#         "廉贞": "戌",
#         "天府": "戌",
#     },
#     "未": {
#         "天机": "午",
#         "太阳": "辰",
#         "武曲": "卯",
#         "天同": "寅",
#         "廉贞": "亥",
#         "天府": "酉",
#     },
#     "申": {
#         "天机": "未",
#         "太阳": "巳",
#         "武曲": "辰",
#         "天同": "卯",
#         "廉贞": "子",
#         "天府": "申",
#     },
#     "酉": {
#         "天机": "申",
#         "太阳": "午",
#         "武曲": "巳",
#         "天同": "辰",
#         "廉贞": "丑",
#         "天府": "未",
#     },
#     "戌": {
#         "天机": "酉",
#         "太阳": "未",
#         "武曲": "午",
#         "天同": "巳",
#         "廉贞": "寅",
#         "天府": "午",
#     },
#     "亥": {
#         "天机": "戌",
#         "太阳": "申",
#         "武曲": "未",
#         "天同": "午",
#         "廉贞": "卯",
#         "天府": "巳",
#     },
# }
json_file = os.path.join(my_dir, "data","jsonfile", "bei_dou_zhu_xing_biao.json")
bei_dou_zhu_xing_biao = None
with open(json_file, "r", encoding="utf-8") as f:
    bei_dou_zhu_xing_biao = json.load(f)
# 天府星的位置根据紫微星确定下来之后，就可以根据天府星确定其他主星
# nan_dou_zhu_xing_biao = {
#     "子": {
#         "太阴": "丑",
#         "贪狼": "寅",
#         "巨门": "卯",
#         "天相": "辰",
#         "天梁": "巳",
#         "七杀": "午",
#         "破军": "戌"
#     },
#     "丑": {
#         "太阴": "寅",
#         "贪狼": "卯",
#         "巨门": "辰",
#         "天相": "巳",
#         "天梁": "午",
#         "七杀": "未",
#         "破军": "亥"},
#     "寅": {
#         "太阴": "卯",
#         "贪狼": "辰",
#         "巨门": "巳",
#         "天相": "午",
#         "天梁": "未",
#         "七杀": "申",
#         "破军": "子"},
#     "卯": {
#         "太阴": "辰",
#         "贪狼": "巳",
#         "巨门": "午",
#         "天相": "未",
#         "天梁": "申",
#         "七杀": "酉",
#         "破军": "丑"},
#     "辰": {
#         "太阴": "巳",
#         "贪狼": "午",
#         "巨门": "未",
#         "天相": "申",
#         "天梁": "酉",
#         "七杀": "戌",
#         "破军": "寅"},
#     "巳": {
#         "太阴": "午",
#         "贪狼": "未",
#         "巨门": "申",
#         "天相": "酉",
#         "天梁": "戌",
#         "七杀": "亥",
#         "破军": "卯"},
#     "午": {
#         "太阴": "未",
#         "贪狼": "申",
#         "巨门": "酉",
#         "天相": "戌",
#         "天梁": "亥",
#         "七杀": "子",
#         "破军": "辰"},
#     "未": {
#         "太阴": "申",
#         "贪狼": "酉",
#         "巨门": "戌",
#         "天相": "亥",
#         "天梁": "子",
#         "七杀": "丑",
#         "破军": "巳"},
#     "申": {
#         "太阴": "酉",
#         "贪狼": "戌",
#         "巨门": "亥",
#         "天相": "子",
#         "天梁": "丑",
#         "七杀": "寅",
#         "破军": "午"},
#     "酉": {
#         "太阴": "戌",
#         "贪狼": "亥",
#         "巨门": "子",
#         "天相": "丑",
#         "天梁": "寅",
#         "七杀": "卯",
#         "破军": "未"},
#     "戌": {
#         "太阴": "亥",
#         "贪狼": "子",
#         "巨门": "丑",
#         "天相": "寅",
#         "天梁": "卯",
#         "七杀": "辰",
#         "破军": "申"},
#     "亥": {
#         "太阴": "子",
#         "贪狼": "丑",
#         "巨门": "寅",
#         "天相": "卯",
#         "天梁": "辰",
#         "七杀": "巳",
#         "破军": "酉"},
# }
json_file = os.path.join(my_dir, "data","jsonfile", "nan_dou_zhu_xing_biao.json")
nan_dou_zhu_xing_biao = None
with open(json_file, "r", encoding="utf-8") as f:
    nan_dou_zhu_xing_biao = json.load(f)

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
