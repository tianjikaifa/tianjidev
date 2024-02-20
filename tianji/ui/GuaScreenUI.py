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
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from tianji.config.json_module import gua_seq_name
from tianji.config.yi_jing_tui_ming.liu_nian_gua_module import gua_dict
from tianji.proj_config import my_dir
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
        kwargs["orientation"] = "vertical"
        super().__init__(**kwargs)

        gua_items = BoxLayout(orientation="vertical", spacing=20, size_hint_y=None)
        gua_items.bind(minimum_height=gua_items.setter('height'))

        for age, gua in guas.items():
            if isinstance(gua, str):
                btn = Button(text=f"{age}岁: {gua}", size_hint_y=None, height=40)
                btn.gua_name = gua
                btn.liu_yue = []

            else:
                btn = Button(text=f"{age}岁: {gua.name}", size_hint_y=None, height=40)
                btn.gua_name = gua.name
                btn.liu_yue = gua.liu_yues
            btn.age = age
            btn.on_press = self.liu_nian(btn)
            set_font(btn)
            btn.background_color = (0.98, 0.98, 0.98, 1)
            gua_items.add_widget(btn)

        view = ScrollView()
        view.add_widget(gua_items)
        l = Label(text="岁   流年卦", size_hint=(1, None), size=(100, 40))
        set_font(l)
        self.add_widget(l)
        self.add_widget(view)
        # self.add_widget(Label(size_hint_y=0.3))

    def yue_gua_enent(self,btn):
        def ff(*args, **kwargs):
            res = f"\n\n{btn.month} 月卦\n{btn.gua_name}"
            tu_name = os.path.join(my_dir, "data", "gua_picture", "jin", f"{gua_seq_name.get(btn.gua_name)}.jpg")
            im2 = Image(source=tu_name, size_hint=(1, None), size=(500, 600))
            message_popup(res, im2)
        return ff
    def liu_nian(self, btn):
        def ff(*args, **kwargs):
            gua_msg = gua_dict.get(btn.gua_name, {"流年": "未定义的卦,也许是有问题需要解决"}).get("流年")
            res = f"\n\n流年 {btn.age}岁\n{btn.gua_name}\n\n{gua_msg}"
            tu_name = os.path.join(my_dir, "data", "gua_picture", "gu", f"{gua_seq_name.get(btn.gua_name)}.jpg")
            im = Image(source=tu_name, size_hint=(1, None), size=(400, 1000))
            tu_name = os.path.join(my_dir, "data", "gua_picture", "jin", f"{gua_seq_name.get(btn.gua_name)}.jpg")
            im2 = Image(source=tu_name, size_hint=(1, None), size=(400, 600))

            gua_items = BoxLayout(orientation="horizontal", spacing=20, padding=20)
            box = BoxLayout(orientation="vertical", size_hint=(1, None), size=(500, 800))
            gua_items.add_widget(Label())
            i=0
            for gua in btn.liu_yue:
                name='\n'.join(gua.name)
                b = Button(text=f"{i + 1}月\n{name}",size_hint=(None, 1), size=(42, 200))
                b.gua_name = gua.name
                b.month = i + 1
                b.on_press = self.yue_gua_enent(b)
                set_font(b)
                b.background_color = (0.98, 0.98, 0.98, 1)
                gua_items.add_widget(b)
                i+=1
            gua_items.add_widget(Label())
            box.add_widget(im2)
            box.add_widget(gua_items)
            message_popup(res, box, im)

        return ff
