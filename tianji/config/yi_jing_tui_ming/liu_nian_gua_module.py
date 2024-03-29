#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/12/10 19:51
# @Author  : huangfujue
# @File    : liu_nian_gua_module.py
# @Date    : 2023/12/10 
"""
模块说明
"""
# ----------------------------------------------------------------------------------------------------------------------
from tianji.config.json_module import gua_dict
class LiuNianGua:

    def __init__(self, ming_pan=None, *args, **kwargs):
        self.ming_pan = ming_pan
        self.age = 1
        if self.ming_pan is None:
            self.guas = self.default_gua()
        else:
            self.guas = self.generate()

    def generate(self):
        """
        # TODO
        在这里计算流年卦
        """
        self.age = self.ming_pan.age


        return self.default_gua()

    def default_gua(self):
        guas = {}
        count = 0
        for name in gua_dict:
            count += 1
            guas[count] = name
        return guas
