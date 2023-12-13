#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/19 18:21
# @Author  : huangfujue
# @File    : UserUI.py
# @Date    : 2023/11/19 
"""
用户界面，配置八字，排盘和流年卦等操作
"""

# ----------------------------------------------------------------------------------------------------------------------
import traceback
import os
import datetime
import json

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button, Label
from kivy.uix.checkbox import CheckBox

from tianji.config.gua_config import gua_dict
from tianji.config.pan_time_module import PanTime
from tianji.ui.DialogScreenUI import OpenFileDialog, message_popup, SaveFileDialog
from tianji.ui.MingPanScreenUI import Pan
from tianji.ui.FontSetModule import set_font, font_size
from tianji.ui.logModule import Logger

from kivy.config import Config

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
dir_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
log = Logger(os.path.join(dir_path, "MingPanDate.log")).logger


class RadioButton(CheckBox):
    def _do_press(self):
        if self.active:
            return
        super(RadioButton, self)._do_press()


class MingPanDate(BoxLayout):
    def __init__(self, pan_windows, **kwargs):
        kwargs["size_hint"] = (1.30, 1)
        super(MingPanDate, self).__init__(**kwargs)
        self.user_info = {}
        self.gender_radio = {}
        self.gender = "男"

        self.button_height = 40
        self.button_widht = 80
        self.label_widht = 70
        self.user_info_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "user_info")
        self.pai_pan = None  # 排盘委托方法
        self.pan_windows = pan_windows  # AppScreen 对象
        root = BoxLayout(orientation="vertical")
        self.add_widget(root)
        root.spacing = 10
        root.padding = 10
        gender_select = BoxLayout(orientation="horizontal", size_hint=(1, None), size=(200, self.button_height))
        root.add_widget(gender_select)
        root.add_widget(self.make_input_item("姓名"))
        root.add_widget(self.make_input_item("日历"))
        root.add_widget(self.make_input_item("农历"))
        root.add_widget(self.make_input_item("四柱"))
        root.add_widget(self.make_input_item("排盘八字"))


        root.add_widget(self.make_label_show("先天", ""))
        root.add_widget(self.make_label_show("后天", ""))
        root.add_widget(self.make_label_show("五行局", ""))
        root.add_widget(self.make_label_show("阴阳男女", ""))
        root.add_widget(self.make_label_show("虚岁", ""))

        gender_item = BoxLayout(orientation="horizontal")
        gender_item.add_widget(self.mkke_gender_item("男"))
        gender_item.add_widget(self.mkke_gender_item("女"))
        gl = Label(text="性别", size_hint=(None, None), size=(self.label_widht, self.button_height))
        set_font(gl)
        gl.text_align = "left"
        gender_select.add_widget(gl)
        gender_select.add_widget(gender_item)

        user_operation = GridLayout(spacing=10)
        user_operation.cols = 2

        # user_operation.spacing = 20
        pai_pan_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='排盘',
                                on_release=self.start)
        bao_cun_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='保存',
                                on_release=self.save_user_info)
        da__kai_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='历史',
                                on_release=self.open_from_file)
        zhuancunbutton = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='存图',
                                on_release=self.save_to_file)
        qing_li_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='清理',
                                on_release=self.clear_user_info)
        tui_chu_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='退出',
                                on_release=self.pan_windows.exit_fun)
        she_zhi_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='设置',
                                on_release=self.pan_windows.settings)

        set_font(pai_pan_button, bao_cun_button, da__kai_button, zhuancunbutton, qing_li_button, tui_chu_button,
                 she_zhi_button)


        user_operation.add_widget(bao_cun_button)
        user_operation.add_widget(da__kai_button)
        user_operation.add_widget(zhuancunbutton)
        user_operation.add_widget(qing_li_button)
        user_operation.add_widget(she_zhi_button)
        user_operation.add_widget(pai_pan_button)
        user_operation.add_widget(tui_chu_button)

        root.add_widget(user_operation)

        # user_operation = BoxLayout(orientation="horizontal",spacing=10)
        # operation1 = BoxLayout(orientation="vertical",spacing=10)
        # operation2 = BoxLayout(orientation="vertical",spacing=10)
        # pai_pan_button = Button(size_hint=(1,None),size=(self.button_widht,50),text='排盘', on_release=self.start)
        # bao_cun_button = Button(size_hint=(1,None),size=(self.button_widht,50),text='保存', on_release=self.save_user_info)
        # da__kai_button = Button(size_hint=(1,None),size=(self.button_widht,50),text='历史', on_release=self.open_from_file)
        # zhuancunbutton = Button(size_hint=(1,None),size=(self.button_widht,50),text='图片', on_release=self.save_to_file)
        #
        # set_font(pai_pan_button, bao_cun_button, da__kai_button, zhuancunbutton)
        # operation1.add_widget(zhuancunbutton)
        # operation1.add_widget(Label())
        # operation1.add_widget(da__kai_button)
        # operation2.add_widget(bao_cun_button)
        # operation2.add_widget(pai_pan_button)
        # user_operation.add_widget(operation1)
        # user_operation.add_widget(operation2)
        # user_operation.add_widget(da__kai_button)
        # user_operation.add_widget(zhuancunbutton)
        # user_operation.add_widget(bao_cun_button)
        # user_operation.add_widget(pai_pan_button)
        # root.add_widget(user_operation)
        # l=Label()
        # l.size_hint_y=1
        # root.add_widget(l)

    def update_ming_pan_time(self, old):

        self.user_info.get("农历").text = old.user_info.get("农历").text
        self.user_info.get("日历").text = old.user_info.get("日历").text
        self.pai_pan = old.pai_pan
        self.gender = old.gender
        self.gender_radio.get(old.gender).active = True
        # self.user_info = old.user_info

    def mkke_gender_item(self, gender="男"):
        root = BoxLayout(orientation="horizontal", spacing=20, size_hint=(1, None), size=(200, self.button_height))
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

    def make_input_item(self, item_type="日历"):
        root = BoxLayout(orientation="horizontal", spacing=20, size_hint=(1, None), size=(200, self.button_height))
        label = Label(text=f"{item_type}: ", size_hint=(None, None), size=(self.label_widht, self.button_height))
        label.text_align = "left"
        input = TextInput(multiline=False)
        root.add_widget(label)
        root.add_widget(input)
        self.user_info[item_type] = input
        set_font(label, input)
        input.font_size = font_size - 2

        if item_type == "姓名":
            input.text = "匿名"

        if item_type in ["农历", "日历"]:
            input.hint_text = "1998-01-31-06"

            if item_type == "农历":
                input.text = "1998-01-04-06"

        return root

    def make_label_show(self, gua_type, gua_name=""):

        root = BoxLayout(orientation="horizontal", spacing=20, size_hint=(1, None), size=(200, self.button_height))
        label = Label(text=f"{gua_type}: ", size_hint=(None, None), size=(self.label_widht + 20, self.button_height))
        button = Button(text=f"{gua_name} ", size_hint=(None, None), size=(self.button_widht, self.button_height))
        set_font(button, label)
        button.background_color = (0.98, 0.98, 0.98, 1)
        label.text_align = "left"
        if  gua_type in  ["先天","后天"]:
            button.on_release = lambda: message_popup(
                f'\n{button.text.strip()} \n\n{gua_dict.get(button.text.strip(), {f"{button.text.strip()}": "未定义的卦,也许是有问题需要解决"}).get(gua_type)}')

        root.add_widget(label)
        root.add_widget(button)

        self.user_info[gua_type] = button
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
            y, m, d = PanTime.solar_to_lunar(y, m, d)

            # print(y, m, d, shi)
            pt = PanTime(y, m, d, shi)
            date = datetime.datetime(y, m, d, shi).strftime("%Y-%m-%d-%H")
            self.user_info.get("农历").text = date
            return pt
        except Exception as E:
            E = traceback.format_exc()
            message_popup(E)
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
            date = datetime.datetime(y, m, d, shi).strftime("%Y-%m-%d-%H")
            self.user_info.get("日历").text = date
            return pt
        except Exception as E:
            E = traceback.format_exc()
            message_popup(E)
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

    def start(self, button, *args, **kwargs):

        if self.pai_pan is None:
            message_popup("尚未传递排盘方法")
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
            message_popup("尚未排盘或农历生日有误")
            return

        if self.user_info.get("姓名").text.strip() == "":
            message_popup("尚未输入姓名")
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
        filename = os.path.join(self.user_info_dir, f"{save_info.get('name')}.json")
        # f"{save_info.get('name')}_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}.json")

        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        # 保存字典对象
        with open(filename, 'w') as f:
            json.dump(save_info, f)
            message_popup(f"保存成功，已保存至{os.path.basename(filename)}")

    def open_from_file(self, button, *args, **kwargs):
        OpenFileDialog("", self.update_user_info, self.user_info_dir).open()

    def save_to_file(self, button, *args, **kwargs):
        def ff(file_name):
            self.pan_windows.export_to_png(file_name, size=self.pan_windows.size, dpi=300, quality=100)

        if self.pan_windows is None:
            message_popup("尚未赋值父窗体，无法导出")
        else:
            save_dir = os.path.join(os.path.dirname(self.user_info_dir), "png")
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            default_file_name = f"{self.user_info.get('姓名').text}_{datetime.datetime.now().strftime('%Y-%m-%d')}"
            SaveFileDialog("请输入保存文件名", fun=ff, default_dir=save_dir, file_name=default_file_name).open()

            # file_name = os.path.join(save_dir,
            #                          f"{self.user_info.get('姓名').text}_{datetime.datetime.now().strftime('%Y-%m-%d')}.png")
            # self.pan_windows.export_to_png(file_name, size=self.pan_windows.size, dpi=300, quality=100)

    def clear_user_info(self, button, *args, **kwargs):
        self.user_info.get("姓名").text = ""
        self.user_info.get("日历").text = ""
        self.user_info.get("农历").text = ""
        self.pai_pan()

    def update_user_info(self, file):

        if not file is None:
            with open(file, 'r') as f:
                user_info = json.load(f)
                self.gender = user_info.get("gender")
                self.gender_radio.get(self.gender).active = True
                self.user_info.get("农历").text = user_info.get("nong_li_time")
                self.user_info.get("日历").text = ""
                self.user_info.get("姓名").text = user_info.get("name")

            self.start(None)
        else:
            message_popup("未选择")
