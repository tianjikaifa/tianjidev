#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/19 18:21
# @Author  : huangfujue
# @File    : SetingUI.py
# @Date    : 2023/11/19 
"""
模块说明
"""

# ----------------------------------------------------------------------------------------------------------------------
import os
import datetime
import json
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button, Label
from kivy.uix.checkbox import CheckBox

from tianji.ui.PanTime import PanTime
from tianji.ui.Dialog import FileChooserPopup
from tianji.ui.MingPan import Pan


from tianji.ui.font_set import set_font
from kivy.config import Config

from tianji.ui.logModule import Logger

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class RadioButton(CheckBox):
    def _do_press(self):
        if self.active:
            return
        super(RadioButton, self)._do_press()


class MingPanDate(BoxLayout):
    def __init__(self, **kwargs):
        super(MingPanDate, self).__init__(**kwargs)
        self.user_info = {}
        self.gender_radio = {}
        self.gender = "男"
        self.user_info_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "user_info")
        self.pai_pan = None  # 排盘委托方法
        root = BoxLayout(orientation="vertical")
        self.add_widget(root)
        gender_select = BoxLayout(orientation="horizontal")
        root.add_widget(gender_select)
        root.spacing = 10
        root.padding = 10
        root.add_widget(self.mk_item("姓名"))
        root.add_widget(self.mk_item("日历"))
        root.add_widget(self.mk_item("农历"))

        gl = Label(text="性别", size_hint_x=0.60)
        set_font(gl)
        gender_select.add_widget(gl)
        gender_select.add_widget(self.mk_gender_item("男"))
        gender_select.add_widget(self.mk_gender_item("女"))
        user_operation = BoxLayout(orientation="horizontal")
        user_operation.spacing = 20
        pai_pan_button = Button(text='排盘', on_release=self.start)
        bao_cun_button = Button(text='保存', on_release=self.save_user_info)
        da__kai_button = Button(text='历史', on_release=self.open_from_file)

        set_font(pai_pan_button, bao_cun_button, da__kai_button)
        pai_pan_button.color = (1, 1, 1, 1)
        bao_cun_button.color = (1, 1, 1, 1)
        da__kai_button.color = (1, 1, 1, 1)
        user_operation.add_widget(da__kai_button)
        user_operation.add_widget(bao_cun_button)
        user_operation.add_widget(pai_pan_button)
        root.add_widget(user_operation)

    def update_ming_pan_time(self, old):
        self.user_info.get("农历").text = old.user_info.get("农历").text
        self.user_info.get("日历").text = old.user_info.get("日历").text
        self.pai_pan = old.pai_pan
        self.gender = old.gender
        self.gender_radio.get(old.gender).active = True
        self.user_info = old.user_info

    def mk_gender_item(self, gender="男"):
        root = BoxLayout(orientation="horizontal")
        root.spacing = 10
        root.padding = 10
        g = RadioButton(group='gender')
        if gender == "男":
            g.active = True
        gl = Label(text=gender)
        set_font(g, gl)
        root.add_widget(gl)
        root.add_widget(g)
        self.gender_radio[gender] = g

        return root

    def mk_item(self, item_type="日历"):
        root = BoxLayout(orientation="horizontal")
        label = Label(text=f"{item_type}:", size_hint_x=0.35)
        input = TextInput(hint_text="1998-01-31-06")
        if item_type == "姓名":
            input = TextInput(hint_text="姓名", text="匿名")
        set_font(label, input)
        root.add_widget(label)
        root.add_widget(input)
        self.user_info[item_type] = input
        return root

    def get_ri_li_pan_time(self):
        s = self.user_info.get("日历").text.strip()
        self.user_info.get("农历").text = ""
        try:
            ss = s.split("-")
            y = int(ss[0])
            m = int(ss[1])
            d = int(ss[2])
            shi = int(ss[3])
            y, m, d =PanTime.solar_to_lunar(y, m, d)

            # print(y, m, d, shi)
            pt = PanTime(y, m, d, shi)
            self.user_info.get("农历").text = (f"{y}-{m}-{d}-{shi}")
            return pt
        except Exception as E:
            self.date_error(str(E))
            self.user_info.get("日历").text = ""
            dir_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"log")
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            log = Logger(os.path.join(dir_path,"err.log")).logger
            log.error(E)

            return None

        # if len(s) >= 13:
        #     try:
        #         ss = s.split("-")
        #         y = int(ss[0])
        #         m = int(ss[1])
        #         d = int(ss[2])
        #         shi = int(ss[3])
        #         y, m, d = PanTime.solar_to_lunar(y, m, d)
        #         print(y, m, d, shi)
        #         pt = PanTime(y, m, d, shi)
        #         self.user_info.get("农历").text = (f"{y}-{m}-{d}-{shi}")
        #         return pt
        #     except Exception as E:
        #         self.date_error(str(E))
        #         return None
        #
        # else:
        #
        #     return None

    def get_nong_li_pan_time(self):
        s = self.user_info.get("农历").text.strip()
        self.user_info.get("日历").text = ""
        try:
            ss = s.split("-")
            y = int(ss[0])
            m = int(ss[1])
            d = int(ss[2])
            shi = int(ss[3])
            # print(y, m, d, shi)
            pt = PanTime(y, m, d, shi)
            y, m, d = pt.lunar_to_solar()
            self.user_info.get("日历").text = (f"{y}-{m}-{d}-{shi}")
            return pt
        except Exception as E:
            self.date_error(str(E))
            self.user_info.get("农历").text = ""
            dir_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"log")
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            log = Logger(os.path.join(dir_path,"err.log")).logger
            log.error(E)
            return None

        # if len(s) >= 13:
        #     try:
        #         ss = s.split("-")
        #         y = int(ss[0])
        #         m = int(ss[1])
        #         d = int(ss[2])
        #         shi = int(ss[3])
        #         print(y, m, d, shi)
        #         pt = PanTime(y, m, d, shi)
        #         y, m, d = pt.lunar_to_solar()
        #         self.user_info.get("日历").text = (f"{y}-{m}-{d}-{shi}")
        #         return pt
        #     except Exception as E:
        #         self.date_error(str(E))
        #         return None
        # else:
        #
        #     return None

    def date_error(self, error=None):
        title = '你的输入有误，请检查 ' if error is None else error
        contex = BoxLayout(orientation="vertical")
        label = Label(text=title)
        button = Button(text='确定', size_hint_y=0.2, on_release=lambda button: popup.dismiss())
        contex.add_widget(label)
        contex.add_widget(button)
        popup = Popup(title="error",
                      content=contex,
                      size_hint=(None, None),
                      size=(400, 400)

                      )

        set_font(button, label, contex, popup)
        label.color = (1, 1, 1, 1)
        button.color = (1, 1, 1, 1)
        popup.open()


    def start(self, button, *args, **kwargs):
        if self.pai_pan is None:
            self.date_error("尚未传递排盘方法")
            return

        if self.gender_radio.get("女").active:
            self.gender = "女"
        else:
            self.gender = "男"

        if not self.user_info.get("农历").text == "":
            ming_pan_time = self.get_nong_li_pan_time()
        else:
            ming_pan_time = self.get_ri_li_pan_time()

        if not ming_pan_time is None:
            p = Pan(ming_pan_time, self.gender)
            self.pai_pan(p)
        else:
            return

    def save_user_info(self, button, *args, **kwargs):

        if self.user_info.get("农历").text.strip() == "":
            self.date_error("尚未排盘或农历生日有误")
            return

        if self.user_info.get("姓名").text.strip() == "":
            self.date_error("尚未输入姓名")
            return

        if self.gender_radio.get("女").active:
            self.gender = "女"
        else:
            self.gender = "男"

        save_info = {
            "name": self.user_info.get("姓名").text,
            "gender": self.gender,
            "nong_li_time": self.user_info.get("农历").text,
        }
        now = datetime.datetime.now()

        # 生成文件名称
        filename = os.path.join(self.user_info_dir,
                                f"{save_info.get('name')}_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}.json")
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        # 保存字典对象
        with open(filename, 'w') as f:
            json.dump(save_info, f)

    def open_from_file(self, button, *args, **kwargs):

        def update_self(file):
            if not file is None:
                with open(file, 'r') as f:
                    user_info = json.load(f)
                    self.gender = user_info.get("gender")
                    self.gender_radio.get(self.gender).active = True
                    self.user_info.get("农历").text = user_info.get("nong_li_time")
                    self.user_info.get("日历").text = ""
                    self.user_info.get("姓名").text = user_info.get("name")

        FileChooserPopup("", update_self, self.user_info_dir).open()
