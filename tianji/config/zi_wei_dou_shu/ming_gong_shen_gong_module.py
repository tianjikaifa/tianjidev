#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/12 18:35
# @Author  : huangfujue
# @File    : ming_gong_shen_gong_module.py
# @Date    : 2023/11/12 
"""
凡是闰月生的，按下月算，比如闰四月按五月算
以当前月份所在的宫起子，顺数到时辰是身，逆数时辰是命
"""

# ----------------------------------------------------------------------------------------------------------------------


from tianji.config.json_module import ming_zhu_biao, shen_zhu_biao
from tianji.config.zi_wei_dou_shu.shi_er_di_zhi_biao_module import Di_Zhi_Iter, di_zhi


class Ming_Shen_Gong:

    def __init__(self, yue, shi_zhi):
        self.yue = yue
        self.shi = shi_zhi

        ming = Di_Zhi_Iter(yue)
        shen = Di_Zhi_Iter(yue)

        flag = True
        for i in range(1, 13):
            dz = di_zhi.get(str(i))
            if dz != self.shi:
                ming.next()
                shen.up()
            else:
                flag = False
                break
        if flag:
            raise Exception("未能匹配时辰，查找命宫身宫失败")
        # for i in range(1, shi_zhi):
        #     ming.up()
        #     shen.next()

        self.ming = ming.now()
        self.shen = shen.now()


class Ming_Zhu:
    def __init__(self, ming_gong):
        # biao = {
        #     "子": "贪狼",
        #     "丑": "巨门",
        #     "寅": "禄存",
        #     "卯": "文曲",
        #     "辰": "廉贞",
        #     "巳": "武曲",
        #     "午": "破军",
        #     "未": "武曲",
        #     "申": "廉贞",
        #     "酉": "文曲",
        #     "戌": "禄存",
        #     "亥": "巨门",
        # }

        self.__ming_gong = ming_gong
        self.命主 = ming_zhu_biao.get(ming_gong)


class Shen_Zhu:
    def __init__(self, nian_zhi):
        self.__nian_zhi = nian_zhi
        # biao = {
        #     "子": "火星",
        #     "丑": "天相",
        #     "寅": "天梁",
        #     "卯": "天同",
        #     "辰": "文昌",
        #     "巳": "天机",
        #     "午": "火星",
        #     "未": "天相",
        #     "申": "天梁",
        #     "酉": "天同",
        #     "戌": "文昌",
        #     "亥": "天机",
        # }

        self.身主 = shen_zhu_biao.get(nian_zhi)


if __name__ == '__main__':


    for dz in di_zhi.values():
        for i in range(1, 13):
            a = Ming_Shen_Gong(i, dz)
            print(f"{a.ming}  {a.shen}")
        print("_" * 20,f"{dz}时")


    # for i in range(1, 13):
    #     a = Ming_Shen_Gong(i, "亥")
    #     #print(f"月{i} 时{24} 命宫 {a.ming} 身宫 {a.shen}")
    #     print(f"{a.ming}  {a.shen}")
    #     print(f"命主 {Ming_Zhu(a.ming).命主}")
    #     print("_" * 20)

    # for zhi in di_zhi.values():
    #     print(f"年支 {zhi} 身主 {Shen_Zhu(zhi).身主}")
    # m=Ming_Shen_Gong(1,5)
    # print(m.ming)
