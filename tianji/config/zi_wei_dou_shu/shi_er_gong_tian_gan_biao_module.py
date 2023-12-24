#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/12 22:11
# @Author  : huangfujue
# @File    : shi_er_gong_tian_gan_biao_module.py
# @Date    : 2023/11/12 
"""
定十二宫天干表- 按本生年干
输入本生年年干，返回一个保存了十二个宫的天干对象
属性名为十二宫名，属性值为十二宫对应的天干值
"""

# ----------------------------------------------------------------------------------------------------------------------

from tianji.config.zi_wei_dou_shu.shi_gan_biao_module import Tian_Gan_Iter, tian_gan
from tianji.config.zi_wei_dou_shu.shi_er_di_zhi_biao_module import Di_Zhi_Iter, di_zhi


class Shi_Er_Gong_Tian_Gan:
    def __init__(self, nian_gan):
        if nian_gan in tian_gan.values():
            self.nian_gan = nian_gan
            tian_gan_iter = self.get_tian_gan_iter()
            di_zhi = Di_Zhi_Iter(0)
            for i in range(12):
                t = tian_gan_iter.next()
                d = di_zhi.up()
                self.__setattr__(d, t)
        else:
            raise Exception(f"指定了不存在的天干 =>  {nian_gan}")

    def get_tian_gan_iter(self):
        if self.nian_gan == "甲" or self.nian_gan == "己":
            return Tian_Gan_Iter("乙")  # 设置未乙，下一个是丙
        if self.nian_gan == "乙" or self.nian_gan == "庚":
            return Tian_Gan_Iter("丁")  # 设置为丁，下一个是戊
        if self.nian_gan == "丙" or self.nian_gan == "辛":
            return Tian_Gan_Iter("己")
        if self.nian_gan == "丁" or self.nian_gan == "壬":
            return Tian_Gan_Iter("辛")
        if self.nian_gan == "戊" or self.nian_gan == "癸":
            return Tian_Gan_Iter("癸")


if __name__ == '__main__':
    t = Shi_Er_Gong_Tian_Gan("丁")
    for dz in di_zhi.values():
        print(dz, t.__getattribute__(dz))
