#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/12 12:40
# @Author  : huangfujue
# @File    : 02.py
# @Date    : 2023/11/12 
"""
模块说明
"""
# ----------------------------------------------------------------------------------------------------------------------
from kivy.app import App
from kivy.uix.widget import Widget



class PongGame(Widget):
    pass


class GameApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    GameApp().run()