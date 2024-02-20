#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/12/12 23:30
# @Author  : huangfujue
# @File    : gong_module.py
# @Date    : 2023/12/12 
"""
模块说明
"""
# ----------------------------------------------------------------------------------------------------------------------


from tianji.config.zi_wei_dou_shu.shi_er_di_zhi_biao_module import  Di_Zhi_Iter
from tianji.config.zi_wei_dou_shu.liang_du_biao_module import liang_du_biao




class Gong:
    """
    表示紫微斗数的十二个宫的容器
    """

    def __init__(self, location):
        nei_zang = {
            "子": "胆",
            "丑": "肝",
            "寅": "肺",
            "卯": "大肠",
            "辰": "胃",
            "巳": "脾",
            "午": "心脏",
            "未": "小肠",
            "申": "膀胱",
            "酉": "肾",
            "戌": "心包",
            "亥": "三焦",
        }
        qu_gan = {
            "子": """膀胱、卵巢、子宫、睾丸""",
            "丑": """膀胱、卵巢、子宫、睾丸""",
            "寅": "右足",
            "卯": "右胁",
            "辰": "右胸",
            "巳": "右肩",
            "午": "脖子、脑袋",
            "未": "脖子、脑袋",
            "申": "左肩",
            "酉": "左胸",
            "戌": "左胁",
            "亥": "左足",
        }
        # 不是身宫
        self.shen_gong = False
        self.location = location
        self.gong_tian_gan = ""
        self.da_xian = ""
        self.name = ""
        self.nei_zang = nei_zang.get(self.location)
        self.qu_gan = qu_gan.get(self.location)

        # 表示每个等级的星耀，不同等级的星耀会排在不同位置
        self.stars = {
            "甲": [],
            "乙": [],
            "丙": [],
            "丁": []
        }

    def get_san_fang(self):
        """
        获取此宫的三方结果
        :return:
        """
        di_zhi_iter = Di_Zhi_Iter(-1)
        di_zhi_iter.update(self.location)
        for i in range(4):
            di_zhi_iter.up()
        guan_lu_location = di_zhi_iter.now()
        for i in range(2):
            di_zhi_iter.up()
        qian_yi_gong_location = di_zhi_iter.now()
        for i in range(2):
            di_zhi_iter.up()
        cai_bo_location = di_zhi_iter.now()
        return [cai_bo_location,qian_yi_gong_location,guan_lu_location]

    def append_start(self, star_info):
        star_name = star_info.name
        level = star_info.start_location
        if level != "四化":  # 不是四化星的直接加
            self.stars.get(level).append(f"{star_name}{liang_du_biao.get(self.location).get(star_name, '')}")
        else:
            # 是四化星
            hua_xing = star_info.belong_star
            old_star_name = f"{hua_xing}{liang_du_biao.get(self.location).get(hua_xing, '')}"
            remove_level = self.__remove_star__(old_star_name)
            new_star_name = f"{hua_xing}{liang_du_biao.get(self.location).get(hua_xing, '')} {star_info.name}"
            self.stars.get(remove_level).append(new_star_name)

    def set_name(self, name):
        """
        设置宫名称
        :param name:
        :return:
        """
        self.name = "{}宫".format(name)

    def set_da_xian(self, da_xain):
        self.da_xian = da_xain

    def set_tian_gan(self, gong_tian_gan):
        """
        设置宫名称
        :param gong_tian_gan:
        :return:
        """
        self.gong_tian_gan = gong_tian_gan

    def __remove_star__(self, remove_star):
        for level, stars in self.stars.items():
            for star in stars:
                if star == remove_star:
                    stars.remove(star)
                    return level

    def pai_pan(self):
        """
        排盘,暂时模拟
        :return:
        """
        print(f"{self.da_xian}")
        print(f"{self.gong_tian_gan}{self.location}\n")
        for k, v in self.stars.items():
            print(k, self.stars.get(k))

