#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2024/1/11 22:12
# @Author  : huangfujue
# @File    : json_module.py
# @Date    : 2024/1/11 
"""
模块说明
"""
import json
# ----------------------------------------------------------------------------------------------------------------------
import os
from tianji.proj_config import my_dir

# region  紫薇斗数配置
# 长生十二星
json_file = os.path.join(my_dir, "data", "jsonfile", "chang_sheng_shi_er_xing_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    chang_sheng_shi_er_xing_biao = json.load(f)

# 五行局表
json_file = os.path.join(my_dir, "data", "jsonfile", "wu_xing_jv_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    wu_xing_jv_biao = json.load(f)

# 表示星耀在各个宫时的亮度
json_file = os.path.join(my_dir, "data", "jsonfile", "liang_du_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    liang_du_biao = json.load(f)

# 起紫薇表
json_file = os.path.join(my_dir, "data","jsonfile",  "zi_wei_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    zi_wei_biao = json.load(f)
# 根据紫微星的位置确定其他星耀位置的星辰
json_file = os.path.join(my_dir, "data","jsonfile", "bei_dou_zhu_xing_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    bei_dou_zhu_xing_biao = json.load(f)
# 根据天府星位置确定的星耀
json_file = os.path.join(my_dir, "data","jsonfile", "nan_dou_zhu_xing_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    nan_dou_zhu_xing_biao = json.load(f)
# 根据年干确定的星辰表
json_file = os.path.join(my_dir, "data", "jsonfile", "nian_gan_xing_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    nian_gan_xing_biao = json.load(f)

# 根据年支确定的星辰表
json_file = os.path.join(my_dir, "data", "jsonfile", "nian_zhi_xing_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    nian_zhi_xing_biao = json.load(f)
# 安火星铃星表
json_file = os.path.join(my_dir, "data","jsonfile",  "huo_ling_xing_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    huo_ling_xing_biao = json.load(f)
# 四化星对应的星辰表
json_file = os.path.join(my_dir, "data", "jsonfile", "si_hua_xing_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    si_hua_xing_biao = json.load(f)
# 安流年将前诸星表
json_file = os.path.join(my_dir, "data", "jsonfile", "jiang_xing_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    jiang_xing_biao = json.load(f)
# 安流年岁键诸星表
json_file = os.path.join(my_dir, "data", "jsonfile", "sui_jian_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    sui_jian_biao = json.load(f)
# 根据月份确定的星耀
json_file = os.path.join(my_dir, "data","jsonfile", "yue_xing_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    yue_xing_biao = json.load(f)
# 根据时辰确定的星耀
json_file = os.path.join(my_dir, "data","jsonfile",  "shi_chen_xing_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    shi_chen_xing_biao = json.load(f)
# 命主表
json_file = os.path.join(my_dir, "data", "jsonfile", "ming_zhu_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    ming_zhu_biao = json.load(f)

# 身主表
json_file = os.path.join(my_dir, "data", "jsonfile", "shen_zhu_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    shen_zhu_biao = json.load(f)

# 确定子年斗君表
json_file = os.path.join(my_dir, "data", "jsonfile", "dou_jun_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    dou_jun_biao = json.load(f)
# endregion


# region 易经推命配置
# 天干表
json_file = os.path.join(my_dir, "data", "jsonfile", "yi_jing_tian_gan_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    tian_gan_biao = json.load(f)
# 地支表
json_file = os.path.join(my_dir, "data", "jsonfile", "yi_jing_di_zhi_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    di_zhi_biao = json.load(f)

# 每个基本卦如何成卦，哪两个组成什么卦
json_file = os.path.join(my_dir, "data", "jsonfile", "gua_zu_he_biao.json")
with open(json_file, "r", encoding="utf-8") as f:
    gua_zu_he_biao = json.load(f)

# 表示64卦每个卦怎么批
json_file = os.path.join(my_dir, "data", "jsonfile", "gua_dict.json")
with open(json_file, "r", encoding="utf-8") as f:
    gua_dict = json.load(f)

json_file = os.path.join(my_dir, "data", "jsonfile", "gua_seq_name.json")
with open(json_file, "r", encoding="utf-8") as f:
    gua_seq_name = json.load(f)

# endregion
