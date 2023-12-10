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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# ----------------------------------------------------------------------------------------------------------------------


from tianji.ui.BaseUI import MyScreen
from tianji.ui.SetingUI import MingPanDate
from tianji.ui.MingPan import  Gong
from tianji.ui.GongScreenUI import GongScreen


from kivy.config import Config

from tianji.ui.font_set import set_font

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class AppScreen(MyScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.user = MingPanDate()
        self.user.pai_pan = self.pai_pan
        self.gongs = {
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
        self.clear_widgets()
        root = BoxLayout(orientation="vertical")
        root.padding = 20
        root.spacing = 0
        shui_ping_1 = BoxLayout(orientation="horizontal")
        shui_ping_1.add_widget(self.gongs.get("巳"))
        shui_ping_1.add_widget(self.gongs.get("午"))
        shui_ping_1.add_widget(self.gongs.get("未"))
        shui_ping_1.add_widget(self.gongs.get("申"))
        root.add_widget(shui_ping_1)

        shui_ping_2 = BoxLayout(orientation="horizontal")
        shui_ping_2.add_widget(self.gongs.get("辰"))
        # shui_ping_2.add_widget(Label(text=""))
        if self.init_time:
            shui_ping_2.add_widget(self.user)
            self.init_time = False
        else:
            old = self.user
            self.user = MingPanDate()
            self.user.update_ming_pan_time(old)
            shui_ping_2.add_widget(self.user)

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


