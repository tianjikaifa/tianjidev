#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/12/10 19:31
# @Author  : huangfujue
# @File    : GuaScreenUI.py
# @Date    : 2023/12/10 
"""
表示64卦的窗体
用来存放易经推命的流年卦部分内容
"""
# ----------------------------------------------------------------------------------------------------------------------
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from tianji.config.zi_wei_dou_shu.gua_config import gua_dict
from tianji.ui.DialogScreenUI import message_popup
from tianji.ui.FontSetModule import set_font


class GuaUI(BoxLayout):
    def __init__(self, guas=None, **kwargs):
        """
        应该需要补充一下流年卦的列表
        """
        self.padding = 10
        if guas is None:
            raise Exception("需要提供流年卦内容")

        if not isinstance(guas, dict):
            raise Exception("需要的是字典对象，年龄为键值")
        kwargs["orientation"]="vertical"
        super().__init__(**kwargs)

        gua_items = BoxLayout(orientation="vertical", spacing=20, size_hint_y=None)
        gua_items.bind(minimum_height=gua_items.setter('height'))

        for age, gua in guas.items():
            btn = Button(text=f"{age}岁: {gua}", size_hint_y=None, height=40)
            btn.gua_name = gua
            btn.age = age
            btn.on_press = self.liu_nian(btn)
            set_font(btn)
            btn.background_color = (0.98, 0.98, 0.98, 1)
            gua_items.add_widget(btn)

        view = ScrollView()
        view.add_widget(gua_items)
        l=Label(text="岁   流年",size_hint=(1,None),size=(100,40))
        set_font(l)
        self.add_widget(l)
        self.add_widget(view)
        self.add_widget(Label(size_hint_y=0.3))

    def liu_nian(self, btn):
        def ff(*args, **kwargs):
            # print(btn.gua_name)
            # print(btn.age)
            gua_msg = gua_dict.get(btn.gua_name, {"流年": "未定义的卦,也许是有问题需要解决"}).get("流年")
            res = f"{btn.gua_name}\n\n{gua_msg}"
            message_popup(res)

        return ff
