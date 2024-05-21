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
import datetime
import json
# ----------------------------------------------------------------------------------------------------------------------

import os.path
from kivy.graphics import Line, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from tianji.config.json_module import gua_dict, gua_zu_he_biao, gua_seq_name
from tianji.config.xiao_liu_ren.pai_liu_ren import pai_liu_ren
from tianji.config.zi_wei_dou_shu.pan_time_module import cal_jianchu
from tianji.proj_config import version_code, my_dir
from tianji.ui.BaseUI import MyScreen
from tianji.ui.DialogScreenUI import message_popup
from tianji.ui.FontSetModule import set_font
from tianji.ui.UserUI import MingPanDate, CenteredTextInput
from tianji.config.zi_wei_dou_shu.ming_pan_module import Gong
from tianji.ui.GongScreenUI import GongScreen
from tianji.ui.GuaScreenUI import GuaUI
from tianji.ui.screen_manager_module import screen_manager
from lunar_python import Lunar, Solar


# 主屏幕
class APPScreen(MyScreen):

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation="vertical")
        root.spacing = 20
        root.padding = 20
        d = datetime.datetime.now()
        lu = Lunar.fromSolar(Solar(d.year, d.month, d.day, d.hour, d.minute, d.second))
        sizhu = "".join(lu.getBaZi())
        # txt=f"日历{d}\n农历{lu}  {cal_jianchu(lu)}日\n\n{'  '.join(sizhu[::2])}\n{'  '.join(sizhu[1::2])}"
        txt = f"日历{d}\n农历{lu}  \n\n{'  '.join(sizhu[::2])}\n{'  '.join(sizhu[1::2])}"
        l1 = Label(text=txt)
        l1.color = (0, 0, 0, 1)
        set_font(l1)

        root.add_widget(l1)
        # root.add_widget(l2)
        root.add_widget(self.make_item("紫薇斗数", "main_screen"))
        root.add_widget(self.make_item("阳宅64卦", "yang_zhai_screen"))
        # root.add_widget(self.make_item("失物寻找", "shi_wu_screen"))
        root.add_widget(self.make_item("小六壬", "xiao_liu_ren_screen"))
        root.add_widget(Label())

        self.add_widget(root)

    def make_item(self, name, to_window_name):
        btn = Button(text=name, size_hint=(1, 0.168))
        set_font(btn)
        btn.color = (0, 0, 0, 1)
        btn.on_press = self.to_screen_envt(to_window_name)

        return btn

    def to_screen_envt(self, screen_name):
        def ff(*args, **kwargs):
            screen_manager.current = screen_name

        return ff


# 紫薇斗数部分
class AppDouShuScreen(MyScreen):

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.exit_fun = app.app_ui
        self.app = app
        self.settings = app.open_settings
        self.__size_hint = (1.30, 1)
        self.can_be_draw_line = True
        self.torch_gong = "子"
        self.zi_dou_location = "子"
        self.draw_lines = []
        self.ming_zhu_xing = ""
        self.shen_zhu_xing = ""
        self.gongs = None
        self.init_time = True
        self.pad = 20

        self.user = MingPanDate(self, size_hint=self.__size_hint)
        self.user.pai_pan = self.pai_pan

        self.pai_pan()
        self.lines = []
        self.bind(size=self._update_rect, pos=self._update_rect)
        with self.canvas.after:
            # Color(0.941, 0.368, 0, 0.5)  # set the color to red
            Color(0.50, 0.5, 0.5, 0.2)  # set the color to red
            self.draw_lines.append(Line(points=[(0, 0), (0, 0)], width=1.1))
            self.draw_lines.append(Line(points=[(0, 0), (0, 0)], width=1.3))
            self.draw_lines.append(Line(points=[(0, 0), (0, 0)], width=1.1))
            self.draw_lines.append(Line(points=[(0, 0), (0, 0)], width=1.1))

    def pai_pan(self, ming_pan=None):

        # if kivy.platform == "android" or kivy.platform == "ios":
        #     # self.top_padding_height = 0.075
        #     # self.boder_padding_height = 0.175
        #     self.top_padding_height = 0.075
        #     self.boder_padding_height = 0.001
        # else:
        #     self.top_padding_height = 0.001
        #     self.boder_padding_height = 0.001
        self.top_padding_height = 0.001
        self.boder_padding_height = 0.001
        tl = Label(size_hint=(1, self.top_padding_height))
        bl = Label(size_hint=(1, self.boder_padding_height))
        self.tl = tl
        self.bl = bl
        if not ming_pan is None:
            # 设置是否是身宫
            ming_pan.gongs.get(ming_pan.shen_gong_location).shen_gong = True
            self.torch_gong = ming_pan.ming_gong_location
            self.ming_zhu_xing = ming_pan.ming_zhu_xing
            self.shen_zhu_xing = ming_pan.shen_zhu_xing
            self.torch_gong = ming_pan.ming_gong_location
            self.zi_dou_location = ming_pan.liu_nian_dou_jun

            gongs = {
                "子": GongScreen(ming_pan.gongs.get("子"), self),
                "丑": GongScreen(ming_pan.gongs.get("丑"), self),
                "寅": GongScreen(ming_pan.gongs.get("寅"), self),
                "卯": GongScreen(ming_pan.gongs.get("卯"), self),
                "辰": GongScreen(ming_pan.gongs.get("辰"), self),
                "巳": GongScreen(ming_pan.gongs.get("巳"), self),
                "午": GongScreen(ming_pan.gongs.get("午"), self),
                "未": GongScreen(ming_pan.gongs.get("未"), self),
                "申": GongScreen(ming_pan.gongs.get("申"), self),
                "酉": GongScreen(ming_pan.gongs.get("酉"), self),
                "戌": GongScreen(ming_pan.gongs.get("戌"), self),
                "亥": GongScreen(ming_pan.gongs.get("亥"), self),
            }
            self.gongs = gongs
            self.guas = ming_pan.liu_nian_guas

        else:
            self.gongs = self.default_gongs()
            guas = {}
            count = 0
            for name in gua_dict:
                count += 1
                guas[count] = name
            self.guas = guas

        self.age = 0 if ming_pan is None else ming_pan.age
        self.clear_pan()

        root = BoxLayout(orientation="vertical")
        root.padding = self.pad
        root.spacing = 0
        root.add_widget(tl)
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
            self.remove_widget(old)
            self.user = MingPanDate(self, size_hint=self.__size_hint)
            self.user.update_ming_pan_date(old)
            old.clear_widgets()
            old = None
            mid_shui_ping.add_widget(self.user)
        # 添加流年卦显示组件
        tt = BoxLayout(orientation="vertical", size_hint=(2 - 0.05 - self.__size_hint[0], 1))
        l = Label(size_hint=(1, 0.1), text=f"紫易哲学\n   V{version_code}")
        gua_ui = GuaUI(self.guas, size_hint=(1, 1))
        set_font(l)
        tt.add_widget(gua_ui)
        tt.add_widget(l)
        mid_shui_ping.add_widget(tt)
        mid_shui_ping.add_widget(Label(size_hint=(0.05, 1)))
        mid_shui_ping.add_widget(zhong_you)
        root.add_widget(mid_shui_ping)

        shui_ping_4 = BoxLayout(orientation="horizontal", size_hint=(1, 0.25))
        shui_ping_4.add_widget(self.gongs.get("寅"))
        shui_ping_4.add_widget(self.gongs.get("丑"))
        shui_ping_4.add_widget(self.gongs.get("子"))
        shui_ping_4.add_widget(self.gongs.get("亥"))
        root.add_widget(shui_ping_4)

        root.add_widget(bl)
        self.add_widget(root)
        self.update_user_config(ming_pan)

    def _update_rect(self, instance, value):

        if not self.can_be_draw_line:
            self.draw_lines[0].points = [[0, 0], [0, 0]]
            self.draw_lines[1].points = [[0, 0], [0, 0]]
            self.draw_lines[2].points = [[0, 0], [0, 0]]
            self.draw_lines[3].points = [[0, 0], [0, 0]]
            return

        w = (self.width - 2 * self.pad) // 8
        scale = self.width / self.tl.width

        h = (self.height - 2 * self.pad) // 8

        self.gong_line = {
            "子": [
                [[5 * w, 2 * h], [2 * w, 5 * h]],
                [[5 * w, 2 * h], [3 * w, 6 * h]],
                [[5 * w, 2 * h], [6 * w, 6 * h]],
                [[2 * w, 5 * h], [6 * w, 6 * h]],
            ],
            "丑": [
                [[3 * w, 2 * h], [2 * w, 6 * h]],
                [[3 * w, 2 * h], [5 * w, 6 * h]],
                [[3 * w, 2 * h], [6 * w, 5 * h]],
                [[2 * w, 6 * h], [6 * w, 5 * h]]
            ],
            "寅": [
                [[2 * w, 2 * h], [3 * w, 6 * h]],
                [[2 * w, 2 * h], [6 * w, 6 * h]],
                [[2 * w, 2 * h], [6 * w, 3 * h]],
                [[3 * w, 6 * h], [6 * w, 3 * h]]
            ],
            "卯": [
                [[2 * w, 3 * h], [5 * w, 6 * h]],
                [[2 * w, 3 * h], [6 * w, 5 * h]],
                [[2 * w, 3 * h], [6 * w, 2 * h]],
                [[5 * w, 6 * h], [6 * w, 2 * h]]
            ],
            "辰": [
                [[2 * w, 5 * h], [6 * w, 6 * h]],
                [[2 * w, 5 * h], [6 * w, 3 * h]],
                [[2 * w, 5 * h], [5 * w, 2 * h]],
                [[6 * w, 6 * h], [5 * w, 2 * h]]
            ],
            "巳": [
                [[2 * w, 6 * h], [6 * w, 5 * h]],
                [[2 * w, 6 * h], [6 * w, 2 * h]],
                [[2 * w, 6 * h], [3 * w, 2 * h]],
                [[6 * w, 5 * h], [3 * w, 2 * h]]
            ],
            "午": [
                [[3 * w, 6 * h], [6 * w, 3 * h]],
                [[3 * w, 6 * h], [5 * w, 2 * h]],
                [[3 * w, 6 * h], [2 * w, 2 * h]],
                [[6 * w, 3 * h], [2 * w, 2 * h]]
            ],
            "未": [
                [[5 * w, 6 * h], [2 * w, 3 * h]],
                [[5 * w, 6 * h], [3 * w, 2 * h]],
                [[5 * w, 6 * h], [6 * w, 2 * h]],
                [[2 * w, 3 * h], [6 * w, 2 * h]]
            ],
            "申": [
                [[6 * w, 6 * h], [2 * w, 5 * h]],
                [[6 * w, 6 * h], [2 * w, 2 * h]],
                [[6 * w, 6 * h], [5 * w, 2 * h]],
                [[2 * w, 5 * h], [5 * w, 2 * h]]
            ],
            "酉": [
                [[6 * w, 5 * h], [3 * w, 2 * h]],
                [[6 * w, 5 * h], [2 * w, 3 * h]],
                [[6 * w, 5 * h], [2 * w, 6 * h]],
                [[3 * w, 2 * h], [2 * w, 6 * h]]
            ],
            "戌": [
                [[6 * w, 3 * h], [2 * w, 2 * h]],
                [[6 * w, 3 * h], [2 * w, 5 * h]],
                [[6 * w, 3 * h], [3 * w, 6 * h]],
                [[2 * w, 2 * h], [3 * w, 6 * h]]
            ],
            "亥": [
                [[6 * w, 2 * h], [2 * w, 3 * h]],
                [[6 * w, 2 * h], [2 * w, 6 * h]],
                [[6 * w, 2 * h], [5 * w, 6 * h]],
                [[2 * w, 3 * h], [5 * w, 6 * h]]
            ],
        }

        self.lines = self.gong_line.get(self.torch_gong)

        def get_points(line_point):
            p1, p2 = line_point
            p1[0] += self.pad
            p2[0] += self.pad

            p1[1] += self.pad
            p2[1] += self.pad

            # p1[1] += off_height2
            # p2[1] += off_height2

            return p1, p2

        if len(self.lines) == 4 and len(self.draw_lines) == 4:
            self.draw_lines[0].points = get_points(self.lines[0])
            self.draw_lines[1].points = get_points(self.lines[1])
            self.draw_lines[2].points = get_points(self.lines[2])
            self.draw_lines[3].points = get_points(self.lines[3])

    def update_user_config(self, ming_pan=None):
        if ming_pan is None:
            self.user.user_info.get("先天卦").text = "未排盘"
            self.user.user_info.get("后天卦").text = "未排盘"

            self.user.user_info.get("命主星").text = ""
            self.user.user_info.get("身主星").text = ""
        else:
            pai_pan_bazi = []
            for item in ming_pan.ba_zi:
                pai_pan_bazi.append(item)
            pai_pan_bazi[0] = ming_pan.pan_time.current_year_ntg
            pai_pan_bazi[1] = ming_pan.pan_time.current_year_ndz
            self.user.user_info.get("排盘四柱").text = "".join(pai_pan_bazi)
            self.user.user_info.get("节气四柱").text = "".join(ming_pan.ba_zi)
            self.user.user_info.get("五行局").text = ming_pan.wu_xing_jv_name
            self.user.user_info.get("阴阳男女").text = f"{ming_pan.yin_yang}{ming_pan.gender}"
            self.user.user_info.get("命主星").text = self.ming_zhu_xing
            self.user.user_info.get("身主星").text = self.shen_zhu_xing
            self.user.user_info.get("子斗").text = self.zi_dou_location

    def on_switch_change(self, value):

        self.can_be_draw_line = True if value == "down" else False
        self._update_rect(None, None)

    def default_gongs(self):
        gong = {
            "子": GongScreen(Gong("子"), self),
            "丑": GongScreen(Gong("丑"), self),
            "寅": GongScreen(Gong("寅"), self),
            "卯": GongScreen(Gong("卯"), self),
            "辰": GongScreen(Gong("辰"), self),
            "巳": GongScreen(Gong("巳"), self),
            "午": GongScreen(Gong("午"), self),
            "未": GongScreen(Gong("未"), self),
            "申": GongScreen(Gong("申"), self),
            "酉": GongScreen(Gong("酉"), self),
            "戌": GongScreen(Gong("戌"), self),
            "亥": GongScreen(Gong("亥"), self),
        }
        return gong

    def clear_pan(self):
        for child in self.children:
            if child == self.user:
                continue
            self.remove_widget(child)
            child = None


# 阳宅部分
class YnagZhaiScreen(MyScreen):

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        items = ["乾", "兑", "离", "震", "巽", "坎", "艮", "坤"]
        root = BoxLayout(orientation="vertical")
        title = BoxLayout(orientation="horizontal")
        root.add_widget(title)
        title.add_widget(Label())
        for name in items:
            l = Label(text=name)
            set_font(l)
            title.add_widget(l)

        for shang_gua in items:
            root.add_widget(self.make_item(shang_gua))
        r_button = Button(text="返回", size_hint=(1, 0.5))
        set_font(r_button)
        r_button.on_press = app.app_ui

        root.add_widget(r_button)
        self.add_widget(root)

    def make_item(self, shang_gua_ming):
        items = ["乾", "兑", "离", "震", "巽", "坎", "艮", "坤"]
        root = BoxLayout(orientation="horizontal")
        l = Label(text=shang_gua_ming)
        set_font(l)
        root.add_widget(l)
        for xia_gua in items:
            root.add_widget(self.make_gua_button(shang_gua_ming, xia_gua))

        return root

    def make_gua_button(self, shang_gua, xia_gua):
        name = gua_zu_he_biao.get(xia_gua).get(shang_gua)
        button = Button(text=name)
        set_font(button)
        button.color = (0, 0, 0, 1)
        button.background_color = (1, 1, 1, 1)

        button.on_press = self.make_button_event(name)
        return button

    def make_button_event(self, name):
        def event(*args, **kwargs):
            picture1 = os.path.join(my_dir, "data", "gua_picture", "jin", f"{gua_seq_name.get(name)}.jpg")
            picture2 = os.path.join(my_dir, "data", "gua_picture", "gu", f"{gua_seq_name.get(name)}.jpg")

            im1 = Image(source=picture1, size_hint=(1, None), size=(400, 800))
            im2 = Image(source=picture2, size_hint=(1, None), size=(400, 1200))
            message_popup(f"\n{name}\n{gua_dict.get(name).get('阳宅')}", im1, im2)

        return event


# 找东西
class ShiWuScreen(MyScreen):

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)


class LiuRenScreen(MyScreen):

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.label_widht = 0.12
        root = BoxLayout(orientation="vertical")
        root.spacing = 20
        root.padding = 20
        # d = datetime.datetime.now()
        # lu = Lunar.fromSolar(Solar(d.year, d.month, d.day, d.hour, d.minute, d.second))
        # sizhu = "".join(lu.getBaZi())
        # txt = f"日历{d}\n农历{lu}  \n{'  '.join(sizhu[::2])}\n{'  '.join(sizhu[1::2])}"
        # l1 = Label(text=txt, size_hint=(1, 0.1), padding=20)
        # l1.color = (0, 0, 0, 1)
        # set_font(l1)
        #
        # root.add_widget(l1)
        root.add_widget(self.create_content())
        r_button = Button(text="返回", size_hint=(1, 0.05))
        set_font(r_button)
        r_button.on_press = app.app_ui

        root.add_widget(r_button)

        self.add_widget(root)

    def create_content(self):
        root = BoxLayout(orientation="vertical")
        root.spacing = 20
        root.padding = 20
        d = datetime.datetime.now()
        day_info = f"{d.year}-{d.month}-{d.day}-{d.hour}"

        root.add_widget(self.make_input_item("时间(新历)", day_info, "年-月-日-小时如 2024-01-01-19"))

        self.result_label = Label(text="\n\n\n\n", size_hint=(1, 0.5))
        set_font(self.result_label)
        root.add_widget(self.result_label)
        root.add_widget(Label( ))

        return root

    def make_input_item(self, item_type, default_value=None, hint_text=None):

        label = Label(text=f"{item_type}: ", size_hint=(0.2, 0.1))
        input = CenteredTextInput(multiline=False, size_hint=(0.8, 0.5))
        if not hint_text is None:
            input.hint_text = hint_text
        if not default_value is None:
            input.text = default_value

        button = Button(text="计算", size_hint=(0.2, 0.5))
        button.on_press=self.press_enevt(input)

        set_font(label, input,button)

        root = BoxLayout(orientation="vertical",size_hint=(1, 0.13))
        sub = BoxLayout(orientation="horizontal")
        sub.add_widget(input)
        sub.add_widget(button)

        root.add_widget(label)
        root.add_widget(sub)
        return root

    def press_enevt(self,input):
        def ff(*args,**kwargs):
            items=input.text.split("-")
            y=int(items[0])
            m=int(items[1])
            d=int(items[2])
            h=int(items[3])
            d=datetime.datetime(y,m,d,h)
            res=pai_liu_ren(date=d)
            self.result_label.text=f"""
            结果             {res.get("时令")}             闰X月按X月算）
            
            {res.get("月令")}    ==>    {res.get("日令")}     ==>     {res.get("时令")} 
            
            
            
            农历 {res.get("时间")}
            {'  '.join(res.get("八字")[::2])}
            {'  '.join(res.get("八字")[1::2])}
            """



        return ff
