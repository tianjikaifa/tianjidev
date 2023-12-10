#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/20 13:47
# @Author  : huangfujue
# @File    : font_set.py
# @Date    : 2023/11/20 
"""
对软件的全局使用字体进行设置
"""

# ----------------------------------------------------------------------------------------------------------------------
import os

def set_font(*objs):
    for obj in objs:
        obj.font_name = os.path.join(os.path.dirname(__file__), "../config", "font", "NotoSansSC-VariableFont_wght.ttf")
        obj.color = (0, 0, 0, 1)
        obj.font_size = 14
        obj.bold = True



