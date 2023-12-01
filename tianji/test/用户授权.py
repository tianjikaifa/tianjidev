#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/23 11:50
# @Author  : huangfujue
# @File    : 用户授权.py
# @Date    : 2023/11/23 
"""
模块说明
"""
# ----------------------------------------------------------------------------------------------------------------------
from kivy.app import App
from plyer import storagepath, filechooser
from kivy.storage.jsonstore import dump
from kivy.storage.jsonstore import loads

class MyApp(App):
    def build(self):
        # 请求读写权限
        #permission.request_permissions([permission.READ_EXTERNAL_STORAGE, permission.WRITE_EXTERNAL_STORAGE])

        # 之后你可以使用存储路径和文件选择器
        path = storagepath
        filechooser.open_file(path=path)

if __name__ == '__main__':

    MyApp().run()