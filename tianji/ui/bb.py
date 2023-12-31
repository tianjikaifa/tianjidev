#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/12/31 11:44
# @Author  : huangfujue
# @File    : bb.py
# @Date    : 2023/12/31 
"""
模块说明
"""
# ----------------------------------------------------------------------------------------------------------------------
import os
import PIL.Image
dirname=r"D:\pycharm\pythonProject1\tianji\data\gua_picture\gu"
def list_files(path=dirname):
    for root, dirs, files in os.walk(path):
        for file in files:
            image = PIL.Image.open(os.path.join(root, file))
            image.save(os.path.join(root,f"{os.path.basename(file).split('.')[0]}.jpg" ))


list_files()