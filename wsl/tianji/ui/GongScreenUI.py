#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/18 23:50
# @Author  : huangfujue
# @File    : GongScreenUI.py
# @Date    : 2023/11/18 
"""
十二个宫可视化部分组件
"""

# ----------------------------------------------------------------------------------------------------------------------


import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color, Line
from kivy.uix.button import Button, Label

from tianji.ui.font_set import set_font


class GongScreen(BoxLayout):
    def __init__(self, gong_obj=None, **kwargs):
        kwargs["orientation"] = "vertical"
        kwargs["padding"] = 10

        super(GongScreen, self).__init__(**kwargs)

        self.other_info = [
            f"{gong_obj.gong_tian_gan}{gong_obj.location}",  # 宫天干+ 宫位
            gong_obj.nei_zang,  # 内脏
            # gong_obj.qu_gan,  # 躯干

        ]

        self.gong_info = [

            gong_obj.da_xian,  # 大流年
            gong_obj.name,  # 宫所主的名称
        ]
        if gong_obj.shen_gong:
            self.gong_info.append("身宫")
        # 表示这个宫的不同等级的星耀
        self.stars = gong_obj.stars

        m = BoxLayout()
        t = BoxLayout()
        t_l = BoxLayout()
        t_r = BoxLayout()
        b = BoxLayout()

        b_l = BoxLayout()
        b_r = BoxLayout()
        b_m = BoxLayout()
        t.add_widget(t_l)
        t.add_widget(t_r)
        b.add_widget(b_l)
        b.add_widget(b_m)
        b.add_widget(b_r)
        self.add_widget(t)
        self.add_widget(m)
        self.add_widget(b)
        t.size_hint_y=0.5
        m.size_hint_y=0.15
        b.size_hint_y=0.35
        dui_qi_fang_shi = "vertical"  # horizontal
        t_l.add_widget(StarListScreen(star_list=self.stars.get("甲"), orientation=dui_qi_fang_shi))
        t_r.add_widget(StarListScreen(star_list=self.stars.get("乙"), orientation=dui_qi_fang_shi))
        b_l.add_widget(StarListScreen(star_list=self.stars.get("丙"), orientation=dui_qi_fang_shi))
        b_r.add_widget(StarListScreen(star_list=self.stars.get("丁"), orientation=dui_qi_fang_shi))
        m.add_widget(StarListScreen(star_list=self.other_info, orientation=dui_qi_fang_shi))
        b_m.add_widget(StarListScreen(star_list=self.gong_info, orientation=dui_qi_fang_shi))

        self.bind(size=self._update_rect, pos=self._update_rect)

        with self.canvas.before:
            Color(0, 0, 0, 1)  # set the color to red
            self.rect = Line(rectangle=(self.x, self.y, self.width, self.height), width=1.5)

    def _update_rect(self, instance, value):
        self.rect.rectangle = (self.x, self.y, self.width, self.height)


class StarListScreen(BoxLayout):
    def __init__(self, star_list, **kwargs):
        kwargs["spacing"] = 10

        self.align = ('left', 'top')
        super(StarListScreen, self).__init__(**kwargs)
        for star in star_list:
            button = Label(text=star)
            set_font(button)
            button.font_blended = True
            button.color = (0, 0, 0, 1)
            self.add_widget(button)
