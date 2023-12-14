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

from kivy.config import Config

from tianji.config.gua_config import gua_dict, LiuNianGua
from tianji.ui.BaseUI import MyScreen
from tianji.ui.UserUI import MingPanDate
from tianji.ui.MingPanScreenUI import Gong
from tianji.ui.GongScreenUI import GongScreen
from tianji.ui.GuaScreenUI import GuaUI

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class AppScreen(MyScreen):

    def __init__(self,app, **kwargs):
        super().__init__(**kwargs)
        self.exit_fun=app.stop
        self.settings=app.open_settings
        self.user = MingPanDate(self)
        self.user.pai_pan = self.pai_pan

        self.gongs = self.default_gongs()
        self.init_time = True
        self.pai_pan()

    def pai_pan(self, ming_pan=None):

        if not ming_pan is None:
            # 设置是否是身宫
            ming_pan.gongs.get(ming_pan.shen_gong_location).shen_gong = True
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
            self.gongs = self.default_gongs()

        liu_nian_gua = LiuNianGua(ming_pan)
        self.guas = liu_nian_gua.guas
        self.age = liu_nian_gua.age
        self.clear_pan()

        root = BoxLayout(orientation="vertical")
        root.padding = 20
        root.spacing = 0
        shui_ping_1 = BoxLayout(orientation="horizontal", size_hint=(1, 0.25))
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
            self.user = MingPanDate(self)
            self.user.update_ming_pan_time(old)
            old.clear_widgets()
            old = None
            mid_shui_ping.add_widget(self.user)

        mid_shui_ping.add_widget(GuaUI(self.guas, size_hint=(0.7, 1)))
        mid_shui_ping.add_widget(zhong_you)
        root.add_widget(mid_shui_ping)

        shui_ping_4 = BoxLayout(orientation="horizontal", size_hint=(1, 0.25))
        shui_ping_4.add_widget(self.gongs.get("寅"))
        shui_ping_4.add_widget(self.gongs.get("丑"))
        shui_ping_4.add_widget(self.gongs.get("子"))
        shui_ping_4.add_widget(self.gongs.get("亥"))
        root.add_widget(shui_ping_4)
        self.add_widget(root)

        self.update_gua(ming_pan)

    def update_gua(self, ming_pan=None):
        if ming_pan is None:
            self.user.user_info.get("先天").text = "未排盘"
            self.user.user_info.get("后天").text = "未排盘"
        else:
            pai_pan_bazi=[]
            for item in ming_pan.ba_zi:
                pai_pan_bazi.append(item)
            pai_pan_bazi[0]=ming_pan.pan_time.current_year_ntg
            pai_pan_bazi[1]=ming_pan.pan_time.current_year_ndz
            self.user.user_info.get("排盘八字").text = "".join(pai_pan_bazi)
            self.user.user_info.get("四柱").text = "".join(ming_pan.ba_zi)
            self.user.user_info.get("五行局").text = ming_pan.wu_xing_jv_name
            self.user.user_info.get("阴阳男女").text = f"{ming_pan.yin_yang}{ming_pan.gender}"
            self.user.user_info.get("虚岁").text = f"{self.age} 岁"

            # TODO 需要在这写下更新先天卦和后天卦
            self.user.user_info.get("先天").text = "坤为地"
            self.user.user_info.get("后天").text = "地山谦"

    def default_gongs(self):
        gong = {
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
        return gong

    def clear_pan(self):
        for child in self.children:
            if child == self.user:
                continue
            self.remove_widget(child)

        self.user.user_info.get("先天").text = "未排盘"
        self.user.user_info.get("后天").text = "未排盘"
