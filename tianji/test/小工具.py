#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/12 19:04
# @Author  : huangfujue
# @File    : 小工具.py
# @Date    : 2023/11/12 
"""
模块说明
"""
# ----------------------------------------------------------------------------------------------------------------------
"""

            

"""


if __name__ == '__main__':
    text="""


    """.replace(" ", "").replace("\n", "")

    for item in text:
        print(item)
    print("==="*30)
    for index in range(0,len(text),2):
        print(f"{text[index]}{text[index+1]}")

    # for i in range(1,13):
    #     print('{}:"",'.format(i))