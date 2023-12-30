#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/12/30 21:08
# @Author  : huangfujue
# @File    : bb.py
# @Date    : 2023/12/30 
"""
模块说明
"""
# ----------------------------------------------------------------------------------------------------------------------
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch


class SwitchWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 创建 Switch 部件
        self.switch = Switch()
        self.switch.bind(active=self.on_active)

        # 添加 Switch 部件到布局
        self.add_widget(self.switch)

    def on_active(self, instance, value):
        # 处理 Switch 部件的状态变化
        if value:
            print("开启")
        else:
            print("关闭")

class SwitchApp(App):
    def build(self):
        return SwitchWidget()

if __name__ == "__main__":
    SwitchApp().run()