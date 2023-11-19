#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/18 20:34
# @Author  : huangfujue
# @File    : 01.py
# @Date    : 2023/11/18 
"""
模块说明
"""
# ----------------------------------------------------------------------------------------------------------------------
import kivy

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()