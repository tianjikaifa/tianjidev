#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/12/22 10:59
# @Author  : huangfujue
# @File    : pai.py
# @Date    : 2023/12/22 
"""
根据根苗花果来排
铁板神数的年代表父母，月是兄弟，日是自己的另一半，时是子女
步骤
1 排八字
2 求天地数
3 根据阴阳男女相当成先天卦
4 取元堂爻（动爻）位将先天卦转后天卦
"""

# ----------------------------------------------------------------------------------------------------------------------
import json
import os

from tianji.config.yi_jing_tui_ming.ba_zi_qu_shu_module import tian_gan_biao, di_zhi_biao
from tianji.config.zi_wei_dou_shu.shi_er_di_zhi_biao_module import shi_er_di_zhi_biao

json_file = os.path.join(os.path.dirname(__file__), "../../data/jsonfile", "gua_zu_he_biao.json")

with open(json_file, "r", encoding="utf-8") as f:
    gua_zu_he_biao = json.load(f)

shu_gua = {
    1: "坎",
    2: "坤",
    3: "震",
    4: "巽",

    6: "乾",
    7: "兑",
    8: "艮",
    9: "离",
}


def kan_fu_mu(bazi):
    num1 = tian_gan_biao.get(bazi[0])
    num2, num3 = di_zhi_biao.get(bazi[1])

    shang_gua = None
    nums = [num1, num2, num3]
    for num in nums:
        if num % 2 == 1:
            shang_gua = shu_gua.get(num)
            nums.remove(num)

    xia_gua = shu_gua.get(sum(nums) % 10)

    print(num1, num2, num3)
    print(shang_gua, xia_gua, gua_zu_he_biao.get(xia_gua).get(shang_gua))

def get_xian_tian_gua(bazi, gender):
    """
    根据给定八字返回结果
    :param bazi:
    :param gender:
    :return:
    """
    gans = bazi[0::2]
    zhis = bazi[1::2]

    yang_shu_he = 0
    yin_shu_he = 0
    for gan in gans:
        num = tian_gan_biao.get(gan)

        if num % 2 == 0:
            yin_shu_he += num
        else:
            yang_shu_he += num

    for zhi in zhis:
        nums = di_zhi_biao.get(zhi)

        for num in nums:
            if num % 2 == 0:
                yin_shu_he += num
            else:
                yang_shu_he += num

    tian_gua = qu_tian_shu_gua(yang_shu_he)
    di_gua = qu_di_zhi_shu_gua(yin_shu_he)
    dang = get_dang_gua(tian_gua, di_gua, zhis[0], gender=gender)
    print(tian_gua, di_gua, dang)

    return dang # tian_gua, di_gua

def get_dang_gua(tian_gua, di_gua, di_zhi, gender):
    """
    根据天数得到的卦和地数得到的卦，结合八字的年地支，判断如何成卦
    :param tian_gua:
    :param di_gua:
    :param bazi:
    :return:
    """
    yin_yang = shi_er_di_zhi_biao.get(di_zhi).yin_yang

    # 需要注意的是成卦字典里是先取下卦再取上卦，所以先取的是地数的卦
    if yin_yang == "阳":
        if gender == "男":
            return gua_zu_he_biao.get(di_gua).get(tian_gua)
        else:
            return gua_zu_he_biao.get(tian_gua).get(di_gua)
    else:
        if gender == "女":
            return gua_zu_he_biao.get(tian_gua).get(di_gua)
        else:
            return gua_zu_he_biao.get(di_gua).get(tian_gua)


def qu_tian_shu_gua(num):
    if num % 10 == 0:
        return shu_gua.get(int(num / 10))

    if num < 10:
        return shu_gua.get(num)
    else:
        if num < 20:
            return shu_gua.get(num - 10)
        else:
            if num <= 25:
                return shu_gua.get(num - 20)
            else:
                temp = num - 25
                if temp < 10:
                    return shu_gua.get(temp)
                else:
                    return qu_tian_shu_gua(temp)


def qu_di_zhi_shu_gua(num):
    if num % 10 == 0:
        return shu_gua.get(int(num / 10))

    if num < 10:
        return shu_gua.get(num)
    else:
        if num < 20:
            return shu_gua.get(num % 10)
        else:
            if num < 30:
                return shu_gua.get(num % 20)
            else:
                temp = num % 30
                if temp < 10:
                    return shu_gua.get(temp)
                else:
                    return qu_tian_shu_gua(temp)







if __name__ == '__main__':
    gender = "男"
    #bazi = ['甲', '子', '丁', '卯', '庚', '申', '庚', '辰']
    bazi = "庚辰 己卯 乙丑 丁丑".replace(" ","")
    bazi=['己', '酉', '戊', '辰', '戊', '寅', '甲', '寅']
    xian_tian=get_xian_tian_gua(bazi, gender)
    print(xian_tian)
    # kan_fu_mu(bazi)

    # bazi=['己', '酉', '戊', '辰', '戊', '寅', '甲', '寅']
    # #get_xian_tian_gua(bazi)
    # kan_fu_mu(bazi)
