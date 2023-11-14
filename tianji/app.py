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

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class AppScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(AppScreen, self).__init__(**kwargs)

        # for i in range(1,17):
        #     self.add_widget(self.creat_gong(" "+str(i)),2)




    def  creat_gong(self,name):
        b=Button(text=name)
        b.background_color =  (10, 10, 10)
        b.size=(400,350)

        return b



class PhoneApp(App):

    def build(self):
        s=AppScreen()
        s.size=(1700,1700)
        return s




if __name__ == '__main__':

    app=PhoneApp()
    app.title="天纪v1.0   --黄甫觉开发版本"
    app.title="开发版本"
    app.run()



