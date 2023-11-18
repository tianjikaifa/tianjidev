#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/12 23:32
# @Author  : huangfujue
# @File    : 五行局表.py
# @Date    : 2023/11/12 
"""
根据命宫位置和年干位置确定起运年分和五行局
"""

# ----------------------------------------------------------------------------------------------------------------------

wu_xing_list = {
    2: "水二局",
    3: "木三局",
    4: "金四局",
    5: "土五局",
    6: "火六局"
}


class Wu_Xing:
    def __init__(self, nian_gan, ming_gong):
        self.nian_gan = nian_gan
        self.ming_gong = ming_gong

    def __get_info(self, num):
        return [num, wu_xing_list.get(num)]

    def get_wu_xing(self):
        """
        获取起运岁数和五行局对象，一个键值对对象
        :return:
        """
        wu_xing_biao = {
            "甲": {
                "子": self.__get_info(2),
                "丑": self.__get_info(2),
                "寅": self.__get_info(6),
                "卯": self.__get_info(6),
                "辰": self.__get_info(3),
                "巳": self.__get_info(3),
                "午": self.__get_info(5),
                "未": self.__get_info(5),
                "申": self.__get_info(4),
                "酉": self.__get_info(4),
                "戌": self.__get_info(6),
                "亥": self.__get_info(6),

            },
            "己": {
                "子": self.__get_info(2),
                "丑": self.__get_info(2),
                "寅": self.__get_info(6),
                "卯": self.__get_info(6),
                "辰": self.__get_info(3),
                "巳": self.__get_info(3),
                "午": self.__get_info(5),
                "未": self.__get_info(5),
                "申": self.__get_info(4),
                "酉": self.__get_info(4),
                "戌": self.__get_info(6),
                "亥": self.__get_info(6),
            },
            "乙": {

                "子": self.__get_info(6),
                "丑": self.__get_info(6),
                "寅": self.__get_info(5),
                "卯": self.__get_info(5),
                "辰": self.__get_info(4),
                "巳": self.__get_info(4),
                "午": self.__get_info(3),
                "未": self.__get_info(3),
                "申": self.__get_info(2),
                "酉": self.__get_info(2),
                "戌": self.__get_info(5),
                "亥": self.__get_info(5),
            },
            "庚": {
                "子": self.__get_info(6),
                "丑": self.__get_info(6),
                "寅": self.__get_info(5),
                "卯": self.__get_info(5),
                "辰": self.__get_info(4),
                "巳": self.__get_info(4),
                "午": self.__get_info(3),
                "未": self.__get_info(3),
                "申": self.__get_info(2),
                "酉": self.__get_info(2),
                "戌": self.__get_info(5),
                "亥": self.__get_info(5),
            },
            "丙": {
                "子": self.__get_info(5),
                "丑": self.__get_info(5),
                "寅": self.__get_info(3),
                "卯": self.__get_info(3),
                "辰": self.__get_info(2),
                "巳": self.__get_info(2),
                "午": self.__get_info(4),
                "未": self.__get_info(4),
                "申": self.__get_info(6),
                "酉": self.__get_info(6),
                "戌": self.__get_info(3),
                "亥": self.__get_info(3),
            },
            "辛": {
                "子": self.__get_info(5),
                "丑": self.__get_info(5),
                "寅": self.__get_info(3),
                "卯": self.__get_info(3),
                "辰": self.__get_info(2),
                "巳": self.__get_info(2),
                "午": self.__get_info(4),
                "未": self.__get_info(4),
                "申": self.__get_info(6),
                "酉": self.__get_info(6),
                "戌": self.__get_info(3),
                "亥": self.__get_info(3),
            },
            "丁": {
                "子": self.__get_info(3),
                "丑": self.__get_info(3),
                "寅": self.__get_info(4),
                "卯": self.__get_info(4),
                "辰": self.__get_info(6),
                "巳": self.__get_info(6),
                "午": self.__get_info(2),
                "未": self.__get_info(2),
                "申": self.__get_info(5),
                "酉": self.__get_info(5),
                "戌": self.__get_info(4),
                "亥": self.__get_info(4),
            },
            "壬": {
                "子": self.__get_info(3),
                "丑": self.__get_info(3),
                "寅": self.__get_info(4),
                "卯": self.__get_info(4),
                "辰": self.__get_info(6),
                "巳": self.__get_info(6),
                "午": self.__get_info(2),
                "未": self.__get_info(2),
                "申": self.__get_info(5),
                "酉": self.__get_info(5),
                "戌": self.__get_info(4),
                "亥": self.__get_info(4),
            },
            "戊": {
                "子": self.__get_info(4),
                "丑": self.__get_info(4),
                "寅": self.__get_info(2),
                "卯": self.__get_info(2),
                "辰": self.__get_info(5),
                "巳": self.__get_info(5),
                "午": self.__get_info(6),
                "未": self.__get_info(6),
                "申": self.__get_info(3),
                "酉": self.__get_info(3),
                "戌": self.__get_info(2),
                "亥": self.__get_info(2),
            },
            "葵": {
                "子": self.__get_info(4),
                "丑": self.__get_info(4),
                "寅": self.__get_info(2),
                "卯": self.__get_info(2),
                "辰": self.__get_info(5),
                "巳": self.__get_info(5),
                "午": self.__get_info(6),
                "未": self.__get_info(6),
                "申": self.__get_info(3),
                "酉": self.__get_info(3),
                "戌": self.__get_info(2),
                "亥": self.__get_info(2),
            }
        }
        return wu_xing_biao.get(self.nian_gan).get(self.ming_gong)


if __name__ == '__main__':
    from tianji.config.十二支所属表 import di_zhi
    from tianji.config.十干表 import tian_gan

    for gong in di_zhi.values():
        print("-----" * 20 + "\n命宫在{}".format(gong))
        for gan in tian_gan.values():
            ming_gong = gong
            nian_gan = gan
            w = Wu_Xing(nian_gan, ming_gong)
            print("{} :".format(gan), w.get_wu_xing())
