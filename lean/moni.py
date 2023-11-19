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
class MyApp(App):
    def build(self):
        layout = GridLayout(cols=4,rows=4,spacing=10)
        for i in range(4):
            for j in range(4):
                button = Label(text="(%d,%d)" % (i, j))
                button.border_color = (255, 0, 0)
                button.foreground_color = (1, 1, 1)
                button.back = (1, 1, 1)

                layout.add_widget(button)
                # 添加边界线

        return layout

if __name__ == "__main__":
    MyApp().run()