#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/12/18 14:07
# @Author  : huangfujue
# @File    : screen_manager_module.py
# @Date    : 2023/12/18 
"""
模块说明
"""


# ----------------------------------------------------------------------------------------------------------------------
from kivy.uix.screenmanager import ScreenManager, Screen

screen_manager = ScreenManager()
main_screen = Screen(name="main_screen")
users_screen = Screen(name="users_screen")
screen_manager.add_widget(main_screen)
screen_manager.add_widget(users_screen)


def main_win(*args,**kwargs):
    screen_manager.current="main_screen"


def users_ui(*args,**kwargs):
    screen_manager.current="users_screen"