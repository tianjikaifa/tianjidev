#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/12 15:39
# @Author  : huangfujue
# @File    : main.py
# @Date    : 2023/11/12 
"""
模块说明
"""
import os
import traceback
import kivy
from kivy.lang import Builder
from kivy.app import App

import tianji.proj_config   as myapp_config
from tianji.ui.AppScreenUI import AppDouShuScreen
from tianji.ui.DialogScreenUI import YesNoPopup
from tianji.ui.logModule import Logger
from tianji.ui.screen_manager_module import main_screen, screen_manager





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

        myapp_config.users_db_path=os.path.join(self.user_data_dir,"user_info.db")
        self.screen_manager=screen_manager
        main_screen.add_widget(AppDouShuScreen(self))
        #main_screen.add_widget(AppYiJingScreen(self))
        # if kivy.platform == "android"  :
        #     request_permissions([Permission.READ_EXTERNAL_STORAGE,Permission.WRITE_EXTERNAL_STORAGE])
        return self.screen_manager


    def on_start(self):
        #kivy.platform="android"
        if kivy.platform == "win":
            self.root_window.size = (900, 900)



"""

# 调整了一下，发现和天纪软件有部分对不上，不知道为什么，暂时先不做了，考上公务员之后也许就有时间继续完成这个软件了，那时我一定继续完成它
# 上次起课问该不该继续完成这个软件得到的结果是地雷复，我看到的是君子之道始复，我一个人难以完成，需要合众人齐心协力，但是我又没办法，所以只能先放下后面有时间了再搞。
这下是天水讼了，先给自己用吧
 pyinstaller .\main.py 

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
