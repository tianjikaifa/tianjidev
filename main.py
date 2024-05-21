#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/12 15:39
# @Author  : huangfujue
# @File    : main.py
# @Date    : 2023/11/12 
"""
程序启动入口
"""
import os
import traceback
import kivy
from kivy.lang import Builder
from kivy.app import App

import tianji.proj_config   as myapp_config
from tianji.ui.AppScreenUI import AppDouShuScreen, APPScreen, YnagZhaiScreen, ShiWuScreen, LiuRenScreen
from tianji.ui.DialogScreenUI import YesNoPopup
from tianji.ui.logModule import Logger
from tianji.ui.screen_manager_module import main_screen, screen_manager, APP_screen, yang_zhai_screen, shi_wu_screen, \
    app_ui, xiao_liu_ren_screen

Builder.load_string('''
<MyScreen>
    canvas.before:
        Color
            #rgba: 0, 0, 0, 1
            #rgba: 0.8, 0.8, 0.8, 1
            rgba: 1, 1, 1, 1

        Rectangle:
            # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size

<Button>:
    background_color: 
        0.95, 0.95, 0.95, 1
    background_normal: 
        ''
    canvas.before:
        Color:
            rgba: self.background_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20]


''')


class ErrorExitPopUp(App):
    def __init__(self, msg, **kwargs):
        super().__init__(**kwargs)
        YesNoPopup(msg, operate_fun=exit).open()


class PhoneApp(App):

    def build(self):
        #app = AppDouShuScreen(self.stop)
        # app = AppDouShuScreen(self)
        #
        # return app
        # 配置程序的数据库存储位置
        myapp_config.users_db_path=os.path.join(self.user_data_dir,"user_info.db")
        self.screen_manager=screen_manager
        self.app_ui=app_ui
        APP_screen.add_widget(APPScreen(self))
        main_screen.add_widget(AppDouShuScreen(self))
        yang_zhai_screen.add_widget(YnagZhaiScreen(self))
        shi_wu_screen.add_widget(ShiWuScreen(self))
        xiao_liu_ren_screen.add_widget(LiuRenScreen(self))
        return self.screen_manager


    def on_start(self):
        #kivy.platform="android"
        if kivy.platform == "win":
            self.root_window.size = (900, 900)



"""
源码只有一套，理论上可以编译出任何平台需要的软件，只要该平台支持python 
打包exe安装包，然后再用Inno Setup Compiler 制作安装包
 pyinstaller .\main.py 
linux下 打包apk安装包，relase 版本需要app签名认证，弄这个又需要有个公司执照，太麻烦所以算了
 buildozer -v  android debug



加一个现有批注笔记的功能
同时增加一套现有体系的星辰亮度表 ，支持设置旧版本和新版本的亮度 
需要做一个失物寻找的功能   



"""

try:
    app = PhoneApp()
    #app.title = f"天纪 {version_code} "
    app.title = ""
    app.run()
except Exception as E:
    E = traceback.format_exc()
    log = Logger('tianji/log/error.log', level='debug').logger
    log.error(E)
    app = ErrorExitPopUp(E)
    app.run()
