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
from itertools import product

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


def get_yuan_tang_yao(gua, shi_zhi):
    """
    根据先天卦和八字中的时时支得到元堂爻，阳时取阳
    :param gua:
    :param shi_zhi:
    :return:
    """
    shi_yin_yang = "阴"
    if shi_zhi in "子丑寅卯辰巳":
        shi_yin_yang = "阳"




def wu_shu_ji_gong(year, yin_yang, gender):
    """
    计算先天卦时，天地数如果是5，那没有对应的卦，这时就要根据五数寄卦法

    :param year:
    :return:
    """
    # 以1864-2043 这180 年作为三元九运划分
    # https://zhuanlan.zhihu.com/p/156657364#:~:text=%E4%B8%89%E5%85%83%E4%B9%9D%E8%BF%90%EF%BC%8C%E6%98%AF%E4%B8%AD%E5%9B%BD%E5%88%92%E5%88%86%E5%A4%A7%E6%97%B6%E9%97%B4%E7%9A%84%E6%96%B9%E6%B3%95%EF%BC%8C%E5%8F%A4%E4%BA%BA%E6%8A%8A20%E5%B9%B4%E5%88%92%E5%88%86%E4%B8%BA%E4%B8%80%E8%BF%90%EF%BC%8C%E4%B8%89%E4%B8%AA20%E5%B9%B4%E4%B9%9F%E5%B0%B1%E6%98%AF%E4%B8%89%E8%BF%90%EF%BC%8C%E5%BD%A2%E6%88%90%E4%B8%80%E5%85%83%E3%80%82%20%E4%B8%89%E4%B8%AA%E5%85%83%E8%BF%90%E5%B0%B1%E6%98%AF%E4%B8%8A%E5%85%83%E3%80%81%E4%B8%AD%E5%85%83%E3%80%81%E4%B8%8B%E5%85%83%EF%BC%8C%E6%AF%8F%E4%B8%80%E5%85%83%E4%B8%89%E4%B8%AA%E8%BF%90%EF%BC%8C%E5%90%88%E7%A7%B0%E4%B8%BA%E2%80%9C%E4%B8%89%E5%85%83%E4%B9%9D%E8%BF%90%E2%80%9D%E3%80%82,%E4%B8%8A%E5%85%83%E6%98%AF%E4%B8%80%E3%80%81%E4%BA%8C%E3%80%81%E4%B8%89%E8%BF%90%EF%BC%9B%E4%B8%AD%E5%85%83%E6%98%AF%E5%9B%9B%E3%80%81%E4%BA%94%E3%80%81%E5%85%AD%E8%BF%90%EF%BC%9B%E4%B8%8B%E5%85%83%E6%98%AF%E4%B8%83%E3%80%81%E5%85%AB%E3%80%81%E4%B9%9D%E8%BF%90%E3%80%82%20%E6%AF%8F%E4%B8%80%E4%B8%AA%E5%85%83%E8%BF%90%E5%85%AD%E5%8D%81%E5%B9%B4%EF%BC%8C%E4%B8%89%E5%85%83%E6%80%BB%E5%85%B1%E6%98%AF180%E5%B9%B4%E3%80%82
    if year < 1864:
        return wu_shu_ji_gong(year + 180, yin_yang, gender)

    if year > 2043:
        return wu_shu_ji_gong(year - 180, yin_yang, gender)

    if year < 1924:
        return "艮" if gender == "男" else "坤"
    else:
        if year < 1984:
            biao = {
                "阳男": "艮",
                "阴女": "艮",
                "阴男": "坤",
                "阳女": "坤",
            }
            return biao.get(f"{yin_yang}{gender}")
        else:
            return "离" if gender == "男" else "兑"


def get_tian_di_shu(gans, zhis):
    """
    根据八字返回天地数
    :param gans:
    :param zhis:
    :return:
    """
    yang_shu_he = 0
    yin_shu_he = 0
    for gan in gans:
        num = tian_gan_biao.get(gan)
        # print(gan,num)
        if num % 2 == 0:
            yin_shu_he += num
        else:
            yang_shu_he += num

    for zhi in zhis:
        nums = di_zhi_biao.get(zhi)
        # print(zhi, nums)
        for num in nums:
            if num % 2 == 0:
                yin_shu_he += num
            else:
                yang_shu_he += num

    return yang_shu_he, yin_shu_he


def get_xian_tian_gua(bazi, gender, year):
    """
    根据给定八字返回结果
    :param bazi:
    :param gender:
    :param year:
    :return:
    """
    gans = bazi[0::2]
    zhis = bazi[1::2]

    yin_yang = shi_er_di_zhi_biao.get(zhis[0]).yin_yang
    yang_shu_he, yin_shu_he = get_tian_di_shu(gans, zhis)

    print(yin_yang, gender)
    tian_gan_number=25
    di_zhi_number=30
    tian_gua = qu_shu_gua(yang_shu_he,tian_gan_number)
    print(tian_gua)
    tian_gua = wu_shu_ji_gong(year, yin_yang, gender) if tian_gua is None else tian_gua
    di_gua = qu_shu_gua(yin_shu_he,di_zhi_number)
    print(di_gua)
    di_gua = wu_shu_ji_gong(year, yin_yang, gender) if di_gua is None else di_gua
    dang = get_xiang_dang(tian_gua, di_gua, yin_yang, gender=gender)
    print(tian_gua, di_gua, dang)

    return dang  # tian_gua, di_gua


def get_xiang_dang(tian_gua, di_gua, yin_yang, gender):
    """
    根据天数得到的卦和地数得到的卦，结合八字的年地支，判断如何成卦
    :param tian_gua:
    :param di_gua:
    :param yin_yang:
    :return:
    """

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


def qu_shu_gua(num, base_number):
    if num <= base_number:
        if num % 10 == 0:
            return shu_gua.get(int(num / 10))
        return shu_gua.get(num - 10 * int(num / 10))
    else:
        return qu_shu_gua(num - base_number,base_number)


def ff():
    def f(ba_zi):
        gans = ba_zi[0::2]
        zhis = ba_zi[1::2]
        yang_shu_he, yin_shu_he = get_tian_di_shu(gans, zhis)
        return ba_zi if yang_shu_he == 20 else None

    nian_gan = tian_gan_biao.keys()
    yue_gan = tian_gan_biao.keys()
    ri_gan = tian_gan_biao.keys()
    shi_gan = tian_gan_biao.keys()

    nian_dizhi = di_zhi_biao.keys()
    yue_dizhi = di_zhi_biao.keys()
    ri_dizhi = di_zhi_biao.keys()
    shi_dizhi = di_zhi_biao.keys()

    res = map(f, product(nian_gan, nian_dizhi, yue_gan, yue_dizhi, ri_gan, ri_dizhi, shi_gan, shi_dizhi))

    result = list(filter(lambda x: x != None, res))

    print(result)


if __name__ == '__main__':

    gender_ = "女"
    year_ = 1999
    bazi = "己卯 戊辰 庚戌 丙戌".replace(" ","")

    xian_tian=get_xian_tian_gua(bazi, gender_,year_)

