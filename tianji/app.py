#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/12 15:39
# @Author  : huangfujue
# @File    : app.py
# @Date    : 2023/11/12 
"""
模块说明
"""
from kivy.lang import Builder
from kivy.app import App
from tianji.AppScreen import AppScreen
import os
from kivy.config import Config

# Config.set("kivy", "encoding", "utf-8")

Builder.load_string('''
<MyScreen>
    canvas.before:
        Color:
            #rgba: 0.8, 0.8, 0.8, 1
            rgba: 1, 1, 1, 1
            #rgba: 0, 0, 0, 1
        Rectangle:
            # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size

''')


class PhoneApp(App):

    def build(self):

        app = AppScreen()

        return app


if __name__ == '__main__':
    app = PhoneApp()
    app.title = "天纪v1.0   --黄甫觉开发版本"
    app.title = "开发版本"
    app.run()
