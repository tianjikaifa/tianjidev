#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/12/31 11:19
# @Author  : huangfujue
# @File    : proj_config.py
# @Date    : 2023/12/31 
"""
模块说明
"""

# ----------------------------------------------------------------------------------------------------------------------
import os.path

import kivy

my_dir = os.path.dirname(__file__)

# ext_dir = os.path.join(os.environ['EXTERNAL_STORAGE'], "tianji","data", "user_info") if kivy.platform == "android" else os.path.join(os.path.dirname(__file__), "data", "user_info")
ext_dir = os.path.join(os.path.dirname(__file__), "data", "user_info")

version_code = "1.2.2"
users_db_path = os.path.join(os.path.dirname(__file__), "data", "user_info", "user_info.db")

if __name__ == '__main__':
    print(my_dir)
