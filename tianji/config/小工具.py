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
孤
高
窍
盗
灾
患
克
父
诽
谤
桃
花
克
母
耗
败
一
年
主
咎
丧
亡
狱
灾
主
讼
小
失
大
败
化
凶
诸
凶
化
凶
孝
服
疾
厄

    """.replace(" ", "").replace("\n", "")

    for item in text:
        print(item)
    print("==="*30)
    for index in range(0,len(text),2):
        print(f"{text[index]}{text[index+1]}")

    # for i in range(1,13):
    #     print('{}:"",'.format(i))