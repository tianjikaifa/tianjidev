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
users_screen = Screen(name="users_screen")  #用户列表
yang_zhai_screen = Screen(name="yang_zhai_screen") # 阳宅
xiao_liu_ren_screen = Screen(name="xiao_liu_ren_screen") # 小六壬
shi_wu_screen = Screen(name="shi_wu_screen") # 失物
APP_screen = Screen(name="APP_screen") # 应用主程序

screen_manager.add_widget(APP_screen)
screen_manager.add_widget(main_screen)
screen_manager.add_widget(users_screen)
screen_manager.add_widget(yang_zhai_screen)
screen_manager.add_widget(shi_wu_screen)
screen_manager.add_widget(xiao_liu_ren_screen)



def main_win(*args,**kwargs):
    screen_manager.current="main_screen"


def users_ui(*args,**kwargs):
    screen_manager.current="users_screen"

def app_ui(*args,**kwargs):
    screen_manager.current = "APP_screen"