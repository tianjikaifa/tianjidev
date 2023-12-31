#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/13 22:45
# @Author  : huangfujue
# @File    : nian_xi_zhu_xing_biao_module.py
# @Date    : 2023/11/13 
"""
根据年干确定星耀位置，
根据年干确定四化星是什么星耀
根据年支确定星耀

"""
import json
import os

# ----------------------------------------------------------------------------------------------------------------------
from tianji.config.zi_wei_dou_shu.shi_er_di_zhi_biao_module import di_zhi, Di_Zhi_Iter
from tianji.config.zi_wei_dou_shu.ming_gong_shen_gong_module import Ming_Shen_Gong
from tianji.config.zi_wei_dou_shu.yu_gong_biao_module import Yu_Gong
from tianji.proj_config import my_dir

json_file = os.path.join(my_dir, "data","jsonfile", "nian_gan_xing_biao.json")
nian_gan_xing_biao = None
with open(json_file, "r", encoding="utf-8") as f:
    nian_gan_xing_biao = json.load(f)

json_file = os.path.join(my_dir, "data","jsonfile", "si_hua_xing_biao.json")
si_hua_xing_biao = None
with open(json_file, "r", encoding="utf-8") as f:
    si_hua_xing_biao = json.load(f)

json_file = os.path.join(my_dir, "data","jsonfile", "nian_zhi_xing_biao.json")
nian_zhi_xing_biao = None
with open(json_file, "r", encoding="utf-8") as f:
    nian_zhi_xing_biao = json.load(f)


"""
用来计算表示天寿星的位置的类，传入月份，时辰和年支
用来计算表示天才星和天寿星的位置
"""


class Tian_Cai_Tian_Show_xing:
    def __init__(self, yue, shi_zhi, nian_zhi):
        """
        根据月份，时辰和年支计算天才、天寿星位置

        :param yue:
        :param shi_zhi:表示时支
        :param nian_zhi:
        """
        ming_shen = Ming_Shen_Gong(yue, shi_zhi)
        self.shen_gong = ming_shen.shen

        self.yu_gong_iter = Yu_Gong(ming_shen.ming)  # 获取所有宫所在的位置
        self.__shi_zhi = shi_zhi
        self.__nian_zhi = nian_zhi
        self.__tian_cai_gong_biao = {
            "子": "命",
            "丑": "父母",
            "寅": "福德",
            "卯": "田宅",
            "辰": "事业",
            "巳": "友仆",
            "午": "迁移",
            "未": "疾厄",
            "申": "财帛",
            "酉": "子女",
            "戌": "夫妻",
            "亥": "兄弟"
        }

    def get_tian_cai_loaction(self):
        gong = self.__tian_cai_gong_biao.get(self.__nian_zhi)
        flag = True
        location = "子"
        for temp in di_zhi.values():
            yu_gong = self.yu_gong_iter.__getattribute__(temp)
            if yu_gong == gong:
                location = temp
                flag = False
                break
        if flag:
            raise Exception("为能找到天才星的位置，也许是参数错了，时辰是用1-12表示的")
        return location

    def get_tian_show_loaction(self):

        flag = True
        di_zhi_iter = Di_Zhi_Iter(-1)  # 从子开始

        for temp in di_zhi.values():

            if temp == self.shen_gong:
                flag = False
                break

            di_zhi_iter.up()

        if flag:
            raise Exception("未能找到天寿星的位置，也许是参数错了，时辰是用1-12表示的")
        return di_zhi_iter.now()


"""
用来表示截空位置
根据年干定下截空星在哪个位置，但是现在看不懂表格，
暂时先按这是两个星辰来看
"""


class Jie_Kong_Xing:
    def __init__(self, nian_gan):

        self.__name = "截空"
        self.__nian_gan = nian_gan
        json_file = os.path.join(my_dir, "data","jsonfile", "jie_kong_biao.json")
        jie_kong_biao = None
        with open(json_file, "r", encoding="utf-8") as f:
            jie_kong_biao = json.load(f)
        self.截路 = jie_kong_biao.get(self.__nian_gan).get("截路")
        self.空亡 = jie_kong_biao.get(self.__nian_gan).get("空亡")


"""
安旬种和空亡星位置，但是表格只是给出了旬中星
"""


class Xun_Kong_Xing:
    def __init__(self, nian_gan, nian_zhi):
        self.__nian_gan = nian_gan
        self.__nian_zhi = nian_zhi
        json_file = os.path.join(my_dir, "data","jsonfile", "xun_kong_biao.json")
        xun_kong_biao = None
        with open(json_file, "r", encoding="utf-8") as f:
            xun_kong_biao = json.load(f)
        self.旬空 = xun_kong_biao.get(nian_zhi).get(nian_gan)
        # biao = {
        #     "戌": {
        #         "甲": "子",
        #         "乙": "丑",
        #         "丙": "寅",
        #         "丁": "卯",
        #         "戊": "辰",
        #         "己": "巳",
        #         "庚": "午",
        #         "辛": "未",
        #         "壬": "申",
        #         "癸": "酉"
        #     },
        #     "申": {
        #         "甲": "戌",
        #         "乙": "亥",
        #         "丙": "子",
        #         "丁": "丑",
        #         "戊": "寅",
        #         "己": "卯",
        #         "庚": "辰",
        #         "辛": "巳",
        #         "壬": "午",
        #         "癸": "未"},
        #     "午": {
        #         "甲": "申",
        #         "乙": "酉",
        #         "丙": "戌",
        #         "丁": "亥",
        #         "戊": "子",
        #         "己": "丑",
        #         "庚": "寅",
        #         "辛": "卯",
        #         "壬": "辰",
        #         "癸": "巳"},
        #     "辰": {
        #         "甲": "午",
        #         "乙": "未",
        #         "丙": "申",
        #         "丁": "酉",
        #         "戊": "戌",
        #         "己": "亥",
        #         "庚": "子",
        #         "辛": "丑",
        #         "壬": "寅",
        #         "癸": "卯"},
        #     "寅": {
        #         "甲": "辰",
        #         "乙": "巳",
        #         "丙": "午",
        #         "丁": "未",
        #         "戊": "申",
        #         "己": "酉",
        #         "庚": "戌",
        #         "辛": "亥",
        #         "壬": "子",
        #         "癸": "丑"},
        #     "子": {
        #         "甲": "寅",
        #         "乙": "卯",
        #         "丙": "辰",
        #         "丁": "巳",
        #         "戊": "午",
        #         "己": "未",
        #         "庚": "申",
        #         "辛": "酉",
        #         "壬": "戌",
        #         "癸": "亥"},
        #     "亥": {
        #         "甲": "子",
        #         "乙": "丑",
        #         "丙": "寅",
        #         "丁": "卯",
        #         "戊": "辰",
        #         "己": "巳",
        #         "庚": "午",
        #         "辛": "未",
        #         "壬": "申",
        #         "癸": "酉"
        #     },
        #     "酉": {
        #         "甲": "戌",
        #         "乙": "亥",
        #         "丙": "子",
        #         "丁": "丑",
        #         "戊": "寅",
        #         "己": "卯",
        #         "庚": "辰",
        #         "辛": "巳",
        #         "壬": "午",
        #         "癸": "未"},
        #     "未": {
        #         "甲": "申",
        #         "乙": "酉",
        #         "丙": "戌",
        #         "丁": "亥",
        #         "戊": "子",
        #         "己": "丑",
        #         "庚": "寅",
        #         "辛": "卯",
        #         "壬": "辰",
        #         "癸": "巳"},
        #     "巳": {
        #         "甲": "午",
        #         "乙": "未",
        #         "丙": "申",
        #         "丁": "酉",
        #         "戊": "戌",
        #         "己": "亥",
        #         "庚": "子",
        #         "辛": "丑",
        #         "壬": "寅",
        #         "癸": "卯"},
        #     "卯": {
        #         "甲": "辰",
        #         "乙": "巳",
        #         "丙": "午",
        #         "丁": "未",
        #         "戊": "申",
        #         "己": "酉",
        #         "庚": "戌",
        #         "辛": "亥",
        #         "壬": "子",
        #         "癸": "丑"},
        #     "丑": {
        #         "甲": "寅",
        #         "乙": "卯",
        #         "丙": "辰",
        #         "丁": "巳",
        #         "戊": "午",
        #         "己": "未",
        #         "庚": "申",
        #         "辛": "酉",
        #         "壬": "戌",
        #         "癸": "亥"},
        # }
        # self.旬空 = xun_kong_biao.get(nian_zhi).get(nian_gan)


"""
天伤星
天使星
天伤永在仆役宫。
天使永在疾厄宫。
"""


class Tian_Shang_Tian_Shi_Xing:
    def __init__(self, ming_gong):
        self.ming_gong = ming_gong
        yu_gong_iter = Yu_Gong(ming_gong)  # 获取所有宫所在的位置
        for temp in di_zhi.values():
            yu_gong = yu_gong_iter.__getattribute__(temp)
            if yu_gong == "疾厄":
                self.天使 = temp
            if yu_gong == "友仆":
                self.天伤 = temp


if __name__ == '__main__':
    from tianji.config.zi_wei_dou_shu.shi_gan_biao_module import tian_gan

    d = nian_gan_xing_biao
    for star in nian_gan_xing_biao.get("甲").keys():
        print(star, [d.get(gan).get(star) for gan in tian_gan.values()])
    d = si_hua_xing_biao
    print("---" * 30, "\n四化星")
    for hua in ["化禄", "化权", "化科", "化忌"]:
        print(hua, [d.get(gan).get(hua) for gan in tian_gan.values()])
    print("---" * 30, "\n年支确定的星耀 \n")

    d = nian_zhi_xing_biao
    for star in ["天马", "解神", "天哭", "天虚", "龙池", "凤阁", "红鸾", "天喜", "孤辰", "寡宿", "蜚廉", "破碎", "天空",
                 "月德"]:
        print(star, [d.get(gan).get(star) for gan in di_zhi.values()])
    print("---" * 30, "\n确定天才、天寿星 \n")
    t = Tian_Cai_Tian_Show_xing(yue=5, shi_zhi="子", nian_zhi="子")
    print("天才星位置  {} ".format(t.get_tian_cai_loaction()))
    print("天寿星位置  {} ".format(t.get_tian_show_loaction()))
    print("---" * 30, "\n确定截路空亡星 \n")
    nian_gan = "丙"
    jie_kong = Jie_Kong_Xing(nian_gan)
    print(f"年干 {nian_gan}  \n截路位置 {jie_kong.截路}  空亡位置 {jie_kong.空亡}")
    print("---" * 30, "\n确定旬中空亡星 \n")
    nian_zhi = "寅"
    xun_zhong = Xun_Kong_Xing(nian_gan, nian_zhi)
    print(f"年干年支 {nian_gan}{nian_zhi}  \n旬中位置 {xun_zhong.旬空}  空亡位置 未知")

    print("---" * 30, "\n确定天伤天使星 \n")
    ming_gong = "亥"
    t = Tian_Shang_Tian_Shi_Xing(ming_gong)
    print(f"天伤 -> {t.天伤}  天使 {t.天使} ")
