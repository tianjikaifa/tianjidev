#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/12 15:39
# @Author  : huangfujue
# @File    : main.py
# @Date    : 2023/11/12 
"""
模块说明
"""

from kivy.lang import Builder
from kivy.app import App
from tianji.ui.AppScreenUI import AppScreen

__version__="1.0.1"
# Config.set("kivy", "encoding", "utf-8")
# Config.set("graphics", "default_font", "tianji/config/font/simsun.ttc")
Builder.load_string('''
<MyScreen>
    canvas.before:
        Color
            #rgba: 0, 0, 0, 1
            #rgba: 0.8, 0.8, 0.8, 1
            rgba: 1, 1, 1, 1

        Rectangle:
            # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size

''')


class PhoneApp(App):

    def build(self):

        app = AppScreen()
        return app


app = PhoneApp()
app.title = "天纪-紫薇斗数 v1.0  --测试版本"
app.run()
