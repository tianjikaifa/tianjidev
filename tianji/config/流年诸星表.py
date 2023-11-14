#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/14 21:52
# @Author  : huangfujue
# @File    : 流年诸星表.py
# @Date    : 2023/11/14 
"""
按流年地支起将星，但是我没搞清楚到底是出生就固定还是每年都不一样
"""

# ----------------------------------------------------------------------------------------------------------------------

"""
按流年地支起将星，
安流年将前诸星表
按流年之地支起岁建
安流年岁前诸星表
"""


class Liu_Nian_Xing:
    def __init__(self, nian_zhi):
        self.__nian_zhi = nian_zhi
        # 安流年将前诸星表
        self.jiang_xing_biao = {
            "寅": {
                "将星": "午",
                "攀鞍": "未",
                "岁驿": "申",
                "息神": "酉",
                "华盖": "戌",
                "劫煞": "亥",
                "灾煞": "子",
                "天煞": "丑",
                "推背": "寅",
                "咸池": "卯",
                "月煞": "辰",
                "亡神": "巳",
            },
            "申": {
                "将星": "子",
                "攀鞍": "丑",
                "岁驿": "寅",
                "息神": "卯",
                "华盖": "辰",
                "劫煞": "巳",
                "灾煞": "午",
                "天煞": "未",
                "推背": "申",
                "咸池": "酉",
                "月煞": "戌",
                "亡神": "亥",
            },
            "巳": {
                "将星": "酉",
                "攀鞍": "戌",
                "岁驿": "亥",
                "息神": "子",
                "华盖": "丑",
                "劫煞": "寅",
                "灾煞": "卯",
                "天煞": "辰",
                "推背": "巳",
                "咸池": "午",
                "月煞": "未",
                "亡神": "申",
            },
            "亥": {
                "将星": "卯",
                "攀鞍": "辰",
                "岁驿": "巳",
                "息神": "午",
                "华盖": "未",
                "劫煞": "申",
                "灾煞": "酉",
                "天煞": "戌",
                "推背": "亥",
                "咸池": "子",
                "月煞": "丑",
                "亡神": "寅",
            },

            "午": {
                "将星": "午",
                "攀鞍": "未",
                "岁驿": "申",
                "息神": "酉",
                "华盖": "戌",
                "劫煞": "亥",
                "灾煞": "子",
                "天煞": "丑",
                "推背": "寅",
                "咸池": "卯",
                "月煞": "辰",
                "亡神": "巳",
            },
            "子": {
                "将星": "子",
                "攀鞍": "丑",
                "岁驿": "寅",
                "息神": "卯",
                "华盖": "辰",
                "劫煞": "巳",
                "灾煞": "午",
                "天煞": "未",
                "推背": "申",
                "咸池": "酉",
                "月煞": "戌",
                "亡神": "亥",
            },
            "酉": {
                "将星": "酉",
                "攀鞍": "戌",
                "岁驿": "亥",
                "息神": "子",
                "华盖": "丑",
                "劫煞": "寅",
                "灾煞": "卯",
                "天煞": "辰",
                "推背": "巳",
                "咸池": "午",
                "月煞": "未",
                "亡神": "申",
            },
            "卯": "",

            "戌": {
                "将星": "午",
                "攀鞍": "未",
                "岁驿": "申",
                "息神": "酉",
                "华盖": "戌",
                "劫煞": "亥",
                "灾煞": "子",
                "天煞": "丑",
                "推背": "寅",
                "咸池": "卯",
                "月煞": "辰",
                "亡神": "巳",
            },
            "辰": {
                "将星": "子",
                "攀鞍": "丑",
                "岁驿": "寅",
                "息神": "卯",
                "华盖": "辰",
                "劫煞": "巳",
                "灾煞": "午",
                "天煞": "未",
                "推背": "申",
                "咸池": "酉",
                "月煞": "戌",
                "亡神": "亥",
            },
            "丑": {
                "将星": "酉",
                "攀鞍": "戌",
                "岁驿": "亥",
                "息神": "子",
                "华盖": "丑",
                "劫煞": "寅",
                "灾煞": "卯",
                "天煞": "辰",
                "推背": "巳",
                "咸池": "午",
                "月煞": "未",
                "亡神": "申",
            },
            "未": {
                "将星": "卯",
                "攀鞍": "辰",
                "岁驿": "巳",
                "息神": "午",
                "华盖": "未",
                "劫煞": "申",
                "灾煞": "酉",
                "天煞": "戌",
                "推背": "亥",
                "咸池": "子",
                "月煞": "丑",
                "亡神": "寅",
            },
        }
        # 安流年岁前诸星表
        self.sui_jian_biao = {
            "子": {
                "岁建": "子",
                "晦气": "丑",
                "丧门": "寅",
                "贯索": "卯",
                "官府": "辰",
                "小耗": "巳",
                "大耗": "午",
                "龙德": "未",
                "白虎": "申",
                "天德": "酉",
                "吊客": "戌",
                "病符": "亥"},
            "丑": {
                "岁建": "丑",
                "晦气": "寅",
                "丧门": "卯",
                "贯索": "辰",
                "官府": "巳",
                "小耗": "午",
                "大耗": "未",
                "龙德": "申",
                "白虎": "酉",
                "天德": "戌",
                "吊客": "亥",
                "病符": "子"},
            "寅": {
                "岁建": "寅",
                "晦气": "卯",
                "丧门": "辰",
                "贯索": "巳",
                "官府": "午",
                "小耗": "未",
                "大耗": "申",
                "龙德": "酉",
                "白虎": "戌",
                "天德": "亥",
                "吊客": "子",
                "病符": "丑"},
            "卯": {
                "岁建": "卯",
                "晦气": "辰",
                "丧门": "巳",
                "贯索": "午",
                "官府": "未",
                "小耗": "申",
                "大耗": "酉",
                "龙德": "戌",
                "白虎": "亥",
                "天德": "子",
                "吊客": "丑",
                "病符": "寅"},
            "辰": {
                "岁建": "辰",
                "晦气": "巳",
                "丧门": "午",
                "贯索": "未",
                "官府": "申",
                "小耗": "酉",
                "大耗": "戌",
                "龙德": "亥",
                "白虎": "子",
                "天德": "丑",
                "吊客": "寅",
                "病符": "卯"},
            "巳": {
                "岁建": "巳",
                "晦气": "午",
                "丧门": "未",
                "贯索": "申",
                "官府": "酉",
                "小耗": "戌",
                "大耗": "亥",
                "龙德": "子",
                "白虎": "丑",
                "天德": "寅",
                "吊客": "卯",
                "病符": "辰"},
            "午": {
                "岁建": "午",
                "晦气": "未",
                "丧门": "申",
                "贯索": "酉",
                "官府": "戌",
                "小耗": "亥",
                "大耗": "子",
                "龙德": "丑",
                "白虎": "寅",
                "天德": "卯",
                "吊客": "辰",
                "病符": "巳"},
            "未": {
                "岁建": "未",
                "晦气": "申",
                "丧门": "酉",
                "贯索": "戌",
                "官府": "亥",
                "小耗": "子",
                "大耗": "丑",
                "龙德": "寅",
                "白虎": "卯",
                "天德": "辰",
                "吊客": "巳",
                "病符": "午"},
            "申": {
                "岁建": "申",
                "晦气": "酉",
                "丧门": "戌",
                "贯索": "亥",
                "官府": "子",
                "小耗": "丑",
                "大耗": "寅",
                "龙德": "卯",
                "白虎": "辰",
                "天德": "巳",
                "吊客": "午",
                "病符": "未"},
            "酉": {
                "岁建": "酉",
                "晦气": "戌",
                "丧门": "亥",
                "贯索": "子",
                "官府": "丑",
                "小耗": "寅",
                "大耗": "卯",
                "龙德": "辰",
                "白虎": "巳",
                "天德": "午",
                "吊客": "未",
                "病符": "申"},
            "戌": {
                "岁建": "戌",
                "晦气": "亥",
                "丧门": "子",
                "贯索": "丑",
                "官府": "寅",
                "小耗": "卯",
                "大耗": "辰",
                "龙德": "巳",
                "白虎": "午",
                "天德": "未",
                "吊客": "申",
                "病符": "酉"},
            "亥": {
                "岁建": "亥",
                "晦气": "子",
                "丧门": "丑",
                "贯索": "寅",
                "官府": "卯",
                "小耗": "辰",
                "大耗": "巳",
                "龙德": "午",
                "白虎": "未",
                "天德": "申",
                "吊客": "酉",
                "病符": "戌"},
        }


if __name__ == '__main__':
    from tianji.config.十二支所属表 import di_zhi

    print("按流年地支起将星")
    for zhi in ["寅", "申", "巳", "亥"]:
        d = Liu_Nian_Xing(zhi).jiang_xing_biao.get(zhi)
        print(zhi, [d.get(star) for star in
                    ["将星", "攀鞍", "岁驿", "息神", "华盖", "劫煞", "灾煞", "天煞", "推背", "咸池", "月煞", "亡神"]])
    print("\n按流年之地支起岁建")
    for zhi in di_zhi.values():
        d = Liu_Nian_Xing(zhi).sui_jian_biao.get(zhi)
        print(zhi, [d.get(star) for star in
                    ["岁建","晦气", "丧门", "贯索", "官府", "小耗", "大耗", "龙德", "白虎", "天德", "吊客", "病符"]])
