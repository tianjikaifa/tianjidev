#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/20 13:47
# @Author  : huangfujue
# @File    : FontSetModule.py
# @Date    : 2023/11/20 
"""
对软件的全局使用字体进行设置
"""

# ----------------------------------------------------------------------------------------------------------------------
import os

import kivy
from kivy.metrics import sp
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.metrics import Metrics

from tianji.proj_config import my_dir

dpi=Metrics.dpi


if kivy.platform == "android":
    if dpi <100:
        font_size =  sp(18)
    else:
        if dpi<200:
            font_size = sp(19)
        else:
            if dpi < 400:
                font_size = sp(20)
            else:
                font_size=  sp(24)

if kivy.platform == "win":
    if dpi <100:
        font_size =  sp(12)
    else:
        if dpi<120:
            font_size = sp(12)
        else:
            if dpi < 150:
                font_size = sp(18)
            else:
                font_size=  sp(20)

# font_size = 22
#
# if kivy.platform == "win":
#     font_size = 18


font_path=os.path.join(my_dir,"data", "font","NotoSansSC-Light.ttf").replace("\\","/")
# if kivy.platform == "win" or kivy.platform == "linux":
#     font_path = os.path.join(my_dir, "data", "font", "NotoSansSC-Light.ttf").replace("\\", "/")
def set_font(*objs):
    for obj in objs:
        obj.bold = True
        obj.font_name = font_path

        if isinstance(obj, FileChooserIconView):
            continue

        if isinstance(obj, Button):
            obj.padding=10

        if isinstance(obj, Label):
            obj.color = (0, 0, 0, 1)

        if isinstance(obj, Button):
            obj.padding=10

        if isinstance(obj, TextInput):
            obj.color = (0, 0, 0, 1)

        if isinstance(obj, Popup):
            obj.title_font = os.path.join(os.path.dirname(__file__), "../config", "font",
                                          "NotoSansSC-VariableFont_wght.ttf")

        obj.font_size = font_size

