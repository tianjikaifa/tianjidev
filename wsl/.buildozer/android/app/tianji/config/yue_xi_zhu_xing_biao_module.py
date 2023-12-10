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

yue_xing_biao = {
    1: {
        "左辅": "辰",
        "右弼": "戌",
        "天刑": "酉",
        "天姚": "丑",
        "天巫": "巳",
        "天月": "戌",
        "阴煞": "寅",
    },
    2: {
        "左辅": "巳",
        "右弼": "酉",
        "天刑": "戌",
        "天姚": "寅",
        "天巫": "申",
        "天月": "巳",
        "阴煞": "子",
    },
    3: {
        "左辅": "午",
        "右弼": "申",
        "天刑": "亥",
        "天姚": "卯",
        "天巫": "寅",
        "天月": "辰",
        "阴煞": "戌",
    },
    4: {
        "左辅": "未",
        "右弼": "未",
        "天刑": "子",
        "天姚": "辰",
        "天巫": "亥",
        "天月": "寅",
        "阴煞": "申",
    },
    5: {
        "左辅": "申",
        "右弼": "午",
        "天刑": "丑",
        "天姚": "巳",
        "天巫": "巳",
        "天月": "未",
        "阴煞": "午",
    },
    6: {
        "左辅": "酉",
        "右弼": "巳",
        "天刑": "寅",
        "天姚": "午",
        "天巫": "申",
        "天月": "卯",
        "阴煞": "辰",
    },
    7: {
        "左辅": "戌",
        "右弼": "辰",
        "天刑": "卯",
        "天姚": "未",
        "天巫": "寅",
        "天月": "亥",
        "阴煞": "寅",
    },
    8: {
        "左辅": "亥",
        "右弼": "卯",
        "天刑": "辰",
        "天姚": "申",
        "天巫": "亥",
        "天月": "未",
        "阴煞": "子",
    },
    9: {
        "左辅": "子",
        "右弼": "寅",
        "天刑": "巳",
        "天姚": "酉",
        "天巫": "巳",
        "天月": "寅",
        "阴煞": "戌",
    },
    10: {
        "左辅": "丑",
        "右弼": "丑",
        "天刑": "午",
        "天姚": "戌",
        "天巫": "申",
        "天月": "午",
        "阴煞": "申",
    },
    11: {
        "左辅": "寅",
        "右弼": "子",
        "天刑": "未",
        "天姚": "亥",
        "天巫": "寅",
        "天月": "戌",
        "阴煞": "午",
    },
    12: {
        "左辅": "卯",
        "右弼": "亥",
        "天刑": "申",
        "天姚": "子",
        "天巫": "亥",
        "天月": "寅",
        "阴煞": "辰",
    }
}


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
        print(start,[yue_xing_biao.get(yue ).get(start)  for yue in range(1,13)])
