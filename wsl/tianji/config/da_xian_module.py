#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/14 18:04
# @Author  : huangfujue
# @File    : da_xian_module.py
# @Date    : 2023/11/14 
"""
用来获取各个宫对应的流年范围
"""

# ----------------------------------------------------------------------------------------------------------------------
from tianji.config.shi_er_di_zhi_biao_module import Di_Zhi_Iter

"""
传入命宫位置，起运年龄和阴阳男女，每个宫就代表了不同的流年范围
"""


class Da_Liu_Nian:
    def __init__(self, ming_gong, start_age, yin_yang_nan_nv):
        dizhi = Di_Zhi_Iter(1)
        dizhi.update(ming_gong)
        func = dizhi.next if (yin_yang_nan_nv == "阳男") or (yin_yang_nan_nv == "阴女") else dizhi.up
        func2 = dizhi.up if (yin_yang_nan_nv == "阳男") or (yin_yang_nan_nv == "阴女") else dizhi.next
        func2()
        interval_time = 10

        self.__setattr__(func(), f"{start_age}-{start_age + interval_time - 1}")
        start_age += interval_time
        self.__setattr__(func(), f"{start_age}-{start_age + interval_time - 1}")
        start_age += interval_time
        self.__setattr__(func(), f"{start_age}-{start_age + interval_time - 1}")
        start_age += interval_time
        self.__setattr__(func(), f"{start_age}-{start_age + interval_time - 1}")
        start_age += interval_time
        self.__setattr__(func(), f"{start_age}-{start_age + interval_time - 1}")
        start_age += interval_time
        self.__setattr__(func(), f"{start_age}-{start_age + interval_time - 1}")
        start_age += interval_time
        self.__setattr__(func(), f"{start_age}-{start_age + interval_time - 1}")
        start_age += interval_time
        self.__setattr__(func(), f"{start_age}-{start_age + interval_time - 1}")
        start_age += interval_time
        self.__setattr__(func(), f"{start_age}-{start_age + interval_time - 1}")
        start_age += interval_time
        self.__setattr__(func(), f"{start_age}-{start_age + interval_time - 1}")
        start_age += interval_time
        self.__setattr__(func(), f"{start_age}-{start_age + interval_time - 1}")
        start_age += interval_time
        self.__setattr__(func(), f"{start_age}-{start_age + interval_time - 1}")
        start_age += interval_time


"""
小流年是男顺女逆，
"""


class Xiao_Liu_nian:
    def __init__(self, nian_zhi, gender):
        self.__iter = Di_Zhi_Iter(0)
        self.__gender = gender
        biao = {
            "申": "戌",
            "子": "戌",
            "辰": "戌",
            "巳": "未",
            "酉": "未",
            "丑": "未",
            "亥": "丑",
            "卯": "丑",
            "未": "丑",
            "寅": "辰",
            "午": "辰",
            "戌": "辰",
        }
        # 获取1，13，25，37,49等所在的宫
        qi_shi_gong = biao.get(nian_zhi)
        # 重置1岁的位置到对应的位置上
        self.__iter.update(qi_shi_gong)

    def get_age_location(self, age):
        for i in range(1, age):
            if self.__gender == "男":
                self.__iter.next()
            else:
                self.__iter.up()

        return self.__iter.now()


if __name__ == '__main__':
    from tianji.config.shi_er_di_zhi_biao_module import di_zhi

    print("流年")
    ming_gong = "子"

    da = Da_Liu_Nian(ming_gong, 5, "阴男")
    for zhi in di_zhi.values():
        print(zhi, da.__getattribute__(zhi))

    print("\n小流年")
    nian_zhi="戌"
    gender="女"
    age=1
    cal=Xiao_Liu_nian(nian_zhi,gender)
    print(f"流年 {age}岁 所在的宫 {cal.get_age_location(age)}")