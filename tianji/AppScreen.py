#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/18 23:51
# @Author  : huangfujue
# @File    : AppScreen.py
# @Date    : 2023/11/18 
"""
模块说明
"""

# ----------------------------------------------------------------------------------------------------------------------

from kivy.uix.boxlayout import BoxLayout
from tianji.ui.BaseUI import MyScreen
from kivy.uix.button import Button, Label

from tianji.MingPan import PanTime, Pan
from tianji.GongScreen import GongScreen


class AppScreen(MyScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        y = 1998
        m = 1
        d = 31
        shi = 6

        y, m, d = PanTime.solar_to_lunar(y, m, d)
        print(y, m, d)

        pt = PanTime(y, m, d, shi)
        pt.get_jie_qi()
        p = Pan(pt, "男")

        self.gongs = {
            "子": GongScreen(p.gongs.get("子")),
            "丑": GongScreen(p.gongs.get("丑")),
            "寅": GongScreen(p.gongs.get("寅")),
            "卯": GongScreen(p.gongs.get("卯")),
            "辰": GongScreen(p.gongs.get("辰")),
            "巳": GongScreen(p.gongs.get("巳")),
            "午": GongScreen(p.gongs.get("午")),
            "未": GongScreen(p.gongs.get("未")),
            "申": GongScreen(p.gongs.get("申")),
            "酉": GongScreen(p.gongs.get("酉")),
            "戌": GongScreen(p.gongs.get("戌")),
            "亥": GongScreen(p.gongs.get("亥")),
        }
        root = BoxLayout(orientation="vertical")

        shui_ping_1 = BoxLayout(orientation="horizontal")
        shui_ping_1.add_widget(self.gongs.get("巳"))
        shui_ping_1.add_widget(self.gongs.get("午"))
        shui_ping_1.add_widget(self.gongs.get("未"))
        shui_ping_1.add_widget(self.gongs.get("申"))
        root.add_widget(shui_ping_1)

        shui_ping_2 = BoxLayout(orientation="horizontal")
        shui_ping_2.add_widget(self.gongs.get("辰"))
        shui_ping_2.add_widget(Label(text=""))
        shui_ping_2.add_widget(Label(text=""))
        shui_ping_2.add_widget(self.gongs.get("酉"))
        root.add_widget(shui_ping_2)

        shui_ping_3 = BoxLayout(orientation="horizontal")
        shui_ping_3.add_widget(self.gongs.get("卯"))
        shui_ping_3.add_widget(Label(text=""))
        shui_ping_3.add_widget(Label(text=""))
        shui_ping_3.add_widget(self.gongs.get("戌"))
        root.add_widget(shui_ping_3)

        shui_ping_4 = BoxLayout(orientation="horizontal")
        shui_ping_4.add_widget(self.gongs.get("寅"))
        shui_ping_4.add_widget(self.gongs.get("丑"))
        shui_ping_4.add_widget(self.gongs.get("子"))
        shui_ping_4.add_widget(self.gongs.get("亥"))
        root.add_widget(shui_ping_4)
        self.add_widget(root)
        # 第二种方式
        # self.add_widget(root)
        # zhong_jian = BoxLayout(orientation="horizontal")
        #
        #
        # shui_ping_1 = BoxLayout(orientation="horizontal")
        # shui_ping_1.add_widget(self.gongs.get("巳"))
        # shui_ping_1.add_widget(self.gongs.get("午"))
        # shui_ping_1.add_widget(self.gongs.get("未"))
        # shui_ping_1.add_widget(self.gongs.get("申"))
        # root.add_widget(shui_ping_1)
        #
        # zuo = BoxLayout(orientation="vertical")
        # zuo.add_widget(self.gongs.get("辰"))
        # zuo.add_widget(self.gongs.get("卯"))
        # zhong_jian.add_widget(zuo)
        # zhong_jian.add_widget(Label(text=""))
        # zhong_jian.add_widget(Label(text=""))
        # you = BoxLayout(orientation="vertical")
        # you.add_widget(self.gongs.get("酉"))
        # you.add_widget(self.gongs.get("戌"))
        # zhong_jian.add_widget(you)
        # root.add_widget(zhong_jian)
        # shui_ping_4 = BoxLayout(orientation="horizontal")
        # shui_ping_4.add_widget(self.gongs.get("寅"))
        # shui_ping_4.add_widget(self.gongs.get("丑"))
        # shui_ping_4.add_widget(self.gongs.get("子"))
        # shui_ping_4.add_widget(self.gongs.get("亥"))
        # root.add_widget(shui_ping_4)
