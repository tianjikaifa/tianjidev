#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/18 22:25
# @Author  : huangfujue
# @File    : 04.py
# @Date    : 2023/11/18 
"""
模块说明
"""
import kivy
# ----------------------------------------------------------------------------------------------------------------------
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.graphics import Color, Rectangle

class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        layout_instance=self
        with layout_instance.canvas.before:
            Color(255, 255,255, 1)  #设置绘制矩形的画笔颜色
            self.rect = Rectangle(size=layout_instance.size,
                                  pos=layout_instance.pos)

        def update_rect(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size

        # listen to size and position changes
        layout_instance.bind(pos=update_rect, size=update_rect)

class TestApp(App):

    def build(self):
        layout=RootWidget(padding=30)
        # button=Button(text="my fist button")
        # layout.add_widget(button)


        return layout


if __name__ == '__main__':
    import os
    print(os.path.dirname(kivy.__file__))
    TestApp().run()
