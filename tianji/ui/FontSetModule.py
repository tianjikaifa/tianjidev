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
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

font_size = 22

if kivy.platform == "win":
    font_size = 18

font_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"data", "font","NotoSansSC-VariableFont_wght.ttf").replace("\\","/")

def set_font(*objs):
    for obj in objs:
        obj.font_size = font_size
        obj.bold = True
        obj.font_name = font_path

        if isinstance(obj, Label):
            obj.color = (0, 0, 0, 1)

        if isinstance(obj, Button):
            obj.padding=10



        if isinstance(obj, TextInput):
            obj.color = (0, 0, 0, 1)

        if isinstance(obj, Popup):
            obj.title_font = os.path.join(os.path.dirname(__file__), "../config", "font",
                                          "NotoSansSC-VariableFont_wght.ttf")



