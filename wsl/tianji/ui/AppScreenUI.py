#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/18 23:51
# @Author  : huangfujue
# @File    : AppScreenUI.py
# @Date    : 2023/11/18 
"""
模块说明
"""


# ----------------------------------------------------------------------------------------------------------------------
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config

from tianji.ui.BaseUI import MyScreen
from tianji.ui.SetingUI import MingPanDate
from tianji.ui.MingPan import  Gong
from tianji.ui.GongScreenUI import GongScreen


Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class AppScreen(MyScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.user = MingPanDate()
        self.user.pai_pan = self.pai_pan
        self.default_gongs = {
            "子": GongScreen(Gong("子")),
            "丑": GongScreen(Gong("丑")),
            "寅": GongScreen(Gong("寅")),
            "卯": GongScreen(Gong("卯")),
            "辰": GongScreen(Gong("辰")),
            "巳": GongScreen(Gong("巳")),
            "午": GongScreen(Gong("午")),
            "未": GongScreen(Gong("未")),
            "申": GongScreen(Gong("申")),
            "酉": GongScreen(Gong("酉")),
            "戌": GongScreen(Gong("戌")),
            "亥": GongScreen(Gong("亥")),
        }
        self.init_time = True
        self.pai_pan()


    def pai_pan(self, ming_pan=None):

        if not ming_pan is None:
            # 设置是否是身宫
            ming_pan.gongs.get(ming_pan.shen_gong_location).shen_gong=True
            gongs = {
                "子": GongScreen(ming_pan.gongs.get("子")),
                "丑": GongScreen(ming_pan.gongs.get("丑")),
                "寅": GongScreen(ming_pan.gongs.get("寅")),
                "卯": GongScreen(ming_pan.gongs.get("卯")),
                "辰": GongScreen(ming_pan.gongs.get("辰")),
                "巳": GongScreen(ming_pan.gongs.get("巳")),
                "午": GongScreen(ming_pan.gongs.get("午")),
                "未": GongScreen(ming_pan.gongs.get("未")),
                "申": GongScreen(ming_pan.gongs.get("申")),
                "酉": GongScreen(ming_pan.gongs.get("酉")),
                "戌": GongScreen(ming_pan.gongs.get("戌")),
                "亥": GongScreen(ming_pan.gongs.get("亥")),
            }
            self.gongs = gongs
        else:
            self.gongs=self.default_gongs

        self.clear_pan()

        root = BoxLayout(orientation="vertical")
        root.padding = 20
        root.spacing = 0
        shui_ping_1 = BoxLayout(orientation="horizontal",size_hint=(1, 0.25))
        shui_ping_1.add_widget(self.gongs.get("巳"))
        shui_ping_1.add_widget(self.gongs.get("午"))
        shui_ping_1.add_widget(self.gongs.get("未"))
        shui_ping_1.add_widget(self.gongs.get("申"))
        root.add_widget(shui_ping_1)


        mid_shui_ping = BoxLayout(orientation="horizontal", size_hint=(1, 0.5))
        zhong_zuo = BoxLayout(orientation="vertical")
        zhong_you = BoxLayout(orientation="vertical")

        zhong_zuo.add_widget(self.gongs.get("辰"))
        zhong_zuo.add_widget(self.gongs.get("卯"))
        zhong_you.add_widget(self.gongs.get("酉"))
        zhong_you.add_widget(self.gongs.get("戌"))
        mid_shui_ping.add_widget(zhong_zuo)
        if self.init_time:
            mid_shui_ping.add_widget(self.user)
            self.init_time = False
        else:
            old = self.user
            self.user = MingPanDate()
            self.user.update_ming_pan_time(old)
            old.clear_widgets()
            old=None
            mid_shui_ping.add_widget(self.user)

        mid_shui_ping.add_widget(Label())
        mid_shui_ping.add_widget(zhong_you)
        root.add_widget(mid_shui_ping)

        shui_ping_4 = BoxLayout(orientation="horizontal",size_hint=(1, 0.25))
        shui_ping_4.add_widget(self.gongs.get("寅"))
        shui_ping_4.add_widget(self.gongs.get("丑"))
        shui_ping_4.add_widget(self.gongs.get("子"))
        shui_ping_4.add_widget(self.gongs.get("亥"))
        root.add_widget(shui_ping_4)
        self.add_widget(root)


    def clear_pan(self):
        for child in self.children:
            if child == self.user:
                continue
            self.remove_widget(child)