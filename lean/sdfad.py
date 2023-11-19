#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/19 11:47
# @Author  : huangfujue
# @File    : moni.py
# @Date    : 2023/11/19
"""
模块说明
"""
# ----------------------------------------------------------------------------------------------------------------------
from kivy.app import App
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

Builder.load_string('''
<GridLayout>
    canvas.before:
        Color:
            rgba: 0.3, 0.3, 0.3, 0
        Rectangle:
            # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size

''')
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        label = Label(text="Hello, world!")
        label.outline_width=10
        label.outline_color=(1,1,1,1)
        return label

if __name__ == "__main__":
    MyApp().run()