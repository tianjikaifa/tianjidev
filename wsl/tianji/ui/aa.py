#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/12/12 0:06
# @Author  : huangfujue
# @File    : aa.py
# @Date    : 2023/12/12 
"""
模块说明
"""
# ----------------------------------------------------------------------------------------------------------------------
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle


class TestApp(App):
    def build(self):
        content = Button(text='Close me!')
        popup = Popup(title='Test popup', content=content, size_hint=(None, None), size=(400, 400))

        # 自定义背景颜色
        with popup.canvas.before:
            Color(1, 0, 0, 1)  # 设置背景颜色为红色
            self.rect = Rectangle(size=popup.size, pos=popup.pos)

        content.bind(on_press=popup.dismiss)
        return Button(text='Open popup', on_press=popup.open)


if __name__ == '__main__':
    TestApp().run()