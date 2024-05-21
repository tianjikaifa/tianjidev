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
import webbrowser

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button, Label
from kivy.uix.checkbox import CheckBox

from tianji.config.json_module import gua_seq_name
from tianji.config.user_db_module import UserListDialogScreen, UserItem
from tianji.config.yi_jing_tui_ming.gua_module import Gua
from tianji.config.yi_jing_tui_ming.yi_jing_liu_nian_module import get_liu_nian_gua, get_liu_yue_gua
from tianji.config.yi_jing_tui_ming.yi_jing_pai_ming import get_xian_tian_gua, get_hou_tian_gua
from tianji.config.yi_jing_tui_ming.liu_nian_gua_module import gua_dict
from tianji.config.zi_wei_dou_shu.pan_time_module import PanTime
from tianji.proj_config import ext_dir, version_code, my_dir
from tianji.ui.DialogScreenUI import OpenFileDialog, message_popup, SaveFileDialog
from tianji.config.zi_wei_dou_shu.ming_pan_module import Pan
from tianji.ui.FontSetModule import set_font  # , font_size
from tianji.ui.logModule import Logger
from tianji.ui.screen_manager_module import users_screen, screen_manager, main_win

# Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

dir_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

log = Logger(os.path.join(dir_path, "UserUI.log")).logger
# 记录最后一次修改的是农历还是日历
last_editd = "农历"


# 单选框
class RadioButton(CheckBox):
    def _do_press(self):
        if self.active:
            return
        super(RadioButton, self)._do_press()


# 文本框
class CenteredTextInput(TextInput):
    def __init__(self, **kwargs):
        self.date_type = kwargs.pop("date_type", None)
        super(CenteredTextInput, self).__init__(**kwargs)
        self.bind(size=self._update_padding,on_touch_up =self.on_activate)

        self.multiline = False  # 确保是单行输入

    def on_activate(self,*args,**kwargs):
        global last_editd
        if not self.date_type is None:
            last_editd = self.date_type
        return True  #阻止事件继续向下触发

    def _update_padding(self, instance, value):
        # 计算垂直居中的padding
        self.padding = (self.height - self.line_height) / 2


# 超链接标签
class HyperlinkLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url = 'https://tianjikaifa.github.io/-/'
        hyperlink_text = '[color=#0000FF][ref=visit_app_com]打开[/ref][/color]'

        self.text = self.url + hyperlink_text
        self.markup = True  # 允许使用文本标记
        self.bind(on_ref_press=self.on_hyperlink_press)
        set_font(self)
        self.font_size = self.font_size + 4

    def on_hyperlink_press(self, instance, ref):
        if ref == 'visit_app_com':
            webbrowser.open(self.url)


class MingPanDate(BoxLayout):
    def __init__(self, pan_windows, **kwargs):

        super(MingPanDate, self).__init__(**kwargs)
        self.user_info = {"性别": {}}
        # self.gender_radio = {}

        # self.button_height = 40
        # self.button_widht = 80
        # self.label_widht = 70
        self.button_height = 1
        self.button_widht = 0.24
        self.label_widht = 0.3
        self.user_info_dir = ext_dir  #
        self.pai_pan = None  # 排盘委托方法
        self.pan_windows = pan_windows  # AppDouShuScreen 对象
        self.gennater_UI()

    def gennater_UI(self):

        root = BoxLayout(orientation="vertical", size_hint=(1, 1))
        self.add_widget(root)
        root.spacing = 10
        root.padding = 10
        input_items_hint_height = 0.5
        user_bazi_info_hint_height = 0.28
        user_operation_hint_height = 0.2
        if kivy.platform == "android" or kivy.platform == "ios":
            input_items_hint_height = 0.31
            user_operation_hint_height = 0.18
        label_hint_height = 1 - input_items_hint_height - user_bazi_info_hint_height - user_operation_hint_height
        # gender_select = BoxLayout(orientation="horizontal", size_hint=(1, None), size=(200, self.button_height))

        input_items = BoxLayout(orientation="vertical", size_hint=(1, input_items_hint_height), spacing=root.spacing)
        gender_select = BoxLayout(orientation="horizontal", size_hint=(1, self.button_height))

        input_items.add_widget(self.make_input_item("姓名"))
        input_items.add_widget(self.make_input_item("日历"))
        input_items.add_widget(self.make_input_item("农历"))
        input_items.add_widget(self.make_input_item("节气四柱"))
        input_items.add_widget(self.make_input_item("排盘四柱"))
        input_items.add_widget(gender_select)
        user_bazi_info = GridLayout(size_hint=(0.8, user_bazi_info_hint_height), spacing=root.spacing)
        if kivy.platform == "android" or kivy.platform == "ios":
            user_bazi_info.cols = 1
            user_bazi_info.add_widget(self.make_label_show("命主星", ""))
            user_bazi_info.add_widget(self.make_label_show("身主星", ""))
            user_bazi_info.add_widget(self.make_label_show("五行局", ""))
            user_bazi_info.add_widget(self.make_label_show("阴阳男女", ""))
            user_bazi_info.add_widget(self.make_label_show("先天卦", ""))
            user_bazi_info.add_widget(self.make_label_show("后天卦", ""))
            user_bazi_info.add_widget(self.make_label_show("子斗", ""))
        else:
            user_bazi_info.cols = 2
            user_bazi_info.add_widget(self.make_label_show("命主星", ""))
            user_bazi_info.add_widget(self.make_label_show("身主星", ""))
            user_bazi_info.add_widget(self.make_label_show("五行局", ""))
            user_bazi_info.add_widget(self.make_label_show("先天卦", ""))
            user_bazi_info.add_widget(self.make_label_show("阴阳男女", ""))
            user_bazi_info.add_widget(self.make_label_show("后天卦", ""))
            user_bazi_info.add_widget(self.make_label_show("子斗", ""))
            user_bazi_info.add_widget(self.make_open_item("辅助线", self.pan_windows.on_switch_change))

        gender_item = BoxLayout(orientation="horizontal", size_hint=(0.8, self.button_height))
        gender_item.add_widget(self.mkke_gender_item("男"))
        gender_item.add_widget(self.mkke_gender_item("女"))
        gender_item.add_widget(Label())
        gl = Label(text="性别", size_hint=(self.label_widht, self.button_height))
        set_font(gl)
        gl.text_align = "left"
        gender_select.add_widget(gl)
        gender_select.add_widget(gender_item)

        # user_operation = GridLayout(spacing=10, size_hint=(None, None), size=(400, 100))
        user_operation = GridLayout(spacing=10, size_hint=(0.9, user_operation_hint_height))
        user_operation.cols = 3

        # pai_pan_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='排盘',
        #                         on_press=self.start)
        # bao_cun_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='保存',
        #                         on_press=self.save_user_info)
        # da__kai_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='历史',
        #                         on_press=self.open_from_file)
        # cun_tu_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='存图',
        #                        on_press=self.save_to_file)
        # qing_li_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='清理',
        #                         on_press=self.clear_user_info)
        # tui_chu_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='退出',
        #                         on_press=self.pan_windows.exit_fun)
        # she_zhi_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='设置',
        #                         on_press=self.pan_windows.settings)
        #
        # guan_yu_button = Button(size_hint=(None, None), size=(self.button_widht, self.button_height), text='关于',
        #                         on_press=self.about)
        pai_pan_button = Button(size_hint=(self.button_widht, self.button_height), text='排盘',
                                on_press=self.start)
        bao_cun_button = Button(size_hint=(self.button_widht, self.button_height), text='保存',
                                on_press=self.save_user_info)
        da__kai_button = Button(size_hint=(self.button_widht, self.button_height), text='历史',
                                on_press=self.open_from_file)
        cun_tu_button = Button(size_hint=(self.button_widht, self.button_height), text='存图',
                               on_press=self.save_to_file)
        qing_li_button = Button(size_hint=(self.button_widht, self.button_height), text='清理',
                                on_press=self.clear_user_info)
        tui_chu_button = Button(size_hint=(self.button_widht, self.button_height), text='退出',
                                on_press=self.pan_windows.exit_fun)
        she_zhi_button = Button(size_hint=(self.button_widht, self.button_height), text='设置',
                                on_press=self.pan_windows.settings)
        # 保存到数据库
        save_button = Button(size_hint=(self.button_widht, self.button_height), text='历史',
                             on_press=self.save_user_list)
        guan_yu_button = Button(size_hint=(self.button_widht, self.button_height), text='说明',
                                on_press=self.about)
        set_font(pai_pan_button, bao_cun_button, da__kai_button, cun_tu_button, qing_li_button, tui_chu_button,
                 guan_yu_button, she_zhi_button, save_button)

        user_operation.cols = 2
        user_operation.add_widget(bao_cun_button)
        user_operation.add_widget(save_button)
        user_operation.add_widget(guan_yu_button)
        user_operation.add_widget(qing_li_button)
        user_operation.add_widget(tui_chu_button)
        user_operation.add_widget(pai_pan_button)
        # user_operation.add_widget(bao_cun_button)
        # user_operation.add_widget(da__kai_button)
        #
        # user_operation.add_widget(qing_li_button)
        # user_operation.add_widget(guan_yu_button)
        # user_operation.add_widget(tui_chu_button)
        # user_operation.add_widget(pai_pan_button)

        root.add_widget(input_items)
        root.add_widget(user_bazi_info)
        root.add_widget(Label(size_hint=(1, label_hint_height / 2)))
        root.add_widget(user_operation)

    def update_ming_pan_date(self, old):

        self.user_info.get("农历").text = old.user_info.get("农历").text
        self.user_info.get("日历").text = old.user_info.get("日历").text
        self.user_info.get("姓名").text = old.user_info.get("姓名").text
        # self.user_info.get("先天卦").text = old.user_info.get("先天卦").text
        # self.user_info.get("后天卦").text = old.user_info.get("后天卦").text

        if kivy.platform == "win":
            self.user_info.get("辅助线").active = self.pan_windows.can_be_draw_line
        self.pai_pan = old.pai_pan

        # self.user_info = old.user_info 1990-08-19-08

    def mkke_gender_item(self, gender="男"):
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
        self.user_info.get("性别")[gender] = g

        return root

    def make_input_item(self, item_type="日历"):
        # root = BoxLayout(orientation="horizontal", spacing=20, size_hint=(1, None), size=(200, self.button_height))
        # label = Label(text=f"{item_type}: ", size_hint=(None, None), size=(self.label_widht, self.button_height))
        root = BoxLayout(orientation="horizontal")
        label = Label(text=f"{item_type}: ", size_hint_x=self.label_widht)  # =(self.label_widht,self.text_height))
        label.text_align = "left"
        if item_type == "日历" or item_type == "农历":
            input = CenteredTextInput(multiline=False,
                                      size_hint_x=1 - self.label_widht,date_type=item_type)  # ,  size_hint=(1-self.label_widht,self.text_height))
        else:
            input = CenteredTextInput(multiline=False,
                                      size_hint_x=1 - self.label_widht)  # ,  size_hint=(1-self.label_widht,self.text_height))
        root.add_widget(label)
        root.add_widget(input)
        self.user_info[item_type] = input
        set_font(label, input)

        if item_type == "姓名":
            input.text = "样例"
            input.hint_text = "张三"

        if item_type in ["农历", "日历"]:

            if item_type == "农历":
                input.hint_text = "2000-01-01-01"
                input.text = "2000-01-01-01"
            else:
                input.hint_text = "农历有输入则以农历日期进行排列"
                input.text = ""
                input.foreground_color = (0, 0, 0, 1)

        return root

    def make_label_show(self, label_type, gua_name=""):

        # root = BoxLayout(orientation="horizontal", spacing=20, size_hint=(1, None), size=(200, self.button_height))
        # label = Label(text=f"{label_type}: ", size_hint=(None, None), size=(self.label_widht + 20, self.button_height))
        # button = Button(text=f"{gua_name} ", size_hint=(None, None), size=(self.button_widht, self.button_height))
        root = BoxLayout(orientation="horizontal")
        label = Label(text=f"{label_type}: ", size_hint=(0.4, self.button_height))
        # button = Button(text=f"{gua_name} ",  size_hint=(self.button_widht, self.button_height))
        button = Button(text=f"{gua_name} ", size_hint=(0.5, self.button_height))
        set_font(button, label)
        button.background_color = (0.98, 0.98, 0.98, 1)
        label.text_align = "left"
        if label_type in ["先天卦", "后天卦"]:
            button.on_press = lambda: message_popup(
                f'\n\n{label_type}\n{button.text.strip()} \n\n{gua_dict.get(button.text.strip(), {f"{button.text.strip()}": "未定义的卦,也许是有问题需要解决"}).get(label_type[:2])}',
                Image(source=os.path.join(my_dir, "data", "gua_picture", "jin",
                                          f"{gua_seq_name.get(button.text.strip())}.jpg"), size_hint=(1, None),
                      size=(400, 1000)))

        if label_type in ["命主星", "身主星"]:
            button.txt = """
命主星是命宫的守护神，主宰人的富贵贫贱祸福寿天，与精神思想有关，先天魂所居之所，是先天具有的特性。
身主星是身宫的守护神，主营养、修为、阴德、福德等，先天魄所居之所，是先天作为导致如今的行为，和身宫一样，是一生最执迷的地方，也是后天努力的因素。

命身主星入命身宫，自我意识特强﹔为龙归大海，适得其所，逢吉更吉，逢凶减凶
命身主星入兄弟宫，靠兄弟朋友，吉则兄弟朋友和睦有助，凶则不和少助。
命身主星入夫妻宫，注重夫妻生活，吉则夫唱妇随，凶则争吵不和、刑克。
命身主星入子孙宫，重视照顾子孙、员工，吉则爱护子孙员工、统御力强;凶则反之。
命身主星入财帛宫，追求财物，吉则财丰，凶则难求。
命身主星入疾厄宫，宫吉主工作环境好，少年得志﹔宫凶主疾病、想不开、不得志。
命身主星入奴仆宫，为卑贱的宫位，纵有吉星也劳碌;老板兼打工。逢贵人禄马亦吉。
命身主星入官禄宫，追求事业、工作狂，吉则事业顺遂而富贵，凶则不利。
命身主星入迁移宫，追求出人头地，想外出发展，变动较大，较宜离祖过房﹔吉则增利、得人敬重，凶则减利、不得人缘、过房或偏房庶出。
命身主星入田宅宫，重视家庭和经营，吉则增加财富、不动产;凶则少聚财。
命身主星入福德宫，追求享受，吉则享清福，凶则减福。
命身主星入父母宫，靠父母，追随名望，吉则孝顺、有名望﹔凶则缺衣少禄、不孝、官非、有恶名。
                """
            button.on_press = lambda: message_popup(button.txt)

        root.add_widget(label)
        root.add_widget(button)

        self.user_info[label_type] = button
        return root

    def make_open_item(self, label_type, on_change_call=None):
        root = BoxLayout(orientation="horizontal", size_hint=(1, self.button_height))
        switch1 = CheckBox(size_hint=(self.button_widht, self.button_height))
        label = Label(text=f"{label_type}: ", size_hint=(self.button_widht, self.button_height))

        switch1.active = self.pan_windows.can_be_draw_line
        switch1.bind(state=lambda s, v: on_change_call(v))

        set_font(switch1, label)
        root.add_widget(label)
        root.add_widget(switch1)

        self.user_info[label_type] = switch1
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

            if m < 0:  # 闰月生的
                m = abs(m)
                message_popup(f"{y}年闰{m}月出生的，按{m + 1}月算,所以显示的农历月实际是要减1")
                m += 1
                if m > 12:
                    y += 1
                    m = 1
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

    def save_user_info(self, button, *args, **kwargs):

        if self.user_info.get("农历").text.strip() == "":
            message_popup("尚未排盘或农历生日有误")
            return

        if self.user_info.get("姓名").text.strip() == "":
            message_popup("尚未输入姓名")
            return

        save_info = {
            "name": self.user_info.get("姓名").text,
            "gender": self.get_gender(),
            "nong_li_time": self.user_info.get("农历").text,
        }
        now = datetime.datetime.now()
        user_info = UserItem(
            name=self.user_info.get("姓名").text,
            birthday=self.user_info.get("农历").text,
            gender=self.get_gender(),
            save_time=str(now),
        )
        user_info.save_to_db()
        message_popup(
            f"\n\n 保存成功 \n{user_info.name} \n{user_info.birthday}\n{user_info.gender}\n{user_info.save_time}")
        # 生成文件名称
        # filename = os.path.join(self.user_info_dir, f"{save_info.get('name')}.json")
        # # f"{save_info.get('name')}_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}.json")
        #
        # if not os.path.exists(os.path.dirname(filename)):
        #     os.makedirs(os.path.dirname(filename))
        # # 保存字典对象
        # with open(filename, 'w', encoding='utf-8') as f:
        #     json.dump(save_info, f, indent=4, ensure_ascii=False)
        #     message_popup(f"保存成功，已保存至{os.path.basename(filename)}")

    def update_user_info(self, file):

        if not file is None:
            with open(file, 'r', encoding='utf-8') as f:
                user_info = json.load(f)
                self.user_info.get("性别").get(user_info.get("gender")).active = True
                self.user_info.get("农历").text = user_info.get("nong_li_time")
                self.user_info.get("日历").text = ""
                self.user_info.get("姓名").text = user_info.get("name")

            self.start(None)
        else:
            message_popup("未选择")

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
        self.user_info.get("姓名").text = "张三"
        self.user_info.get("日历").text = ""
        self.user_info.get("农历").text = ""
        self.pai_pan()

    def get_gender(self):
        gender = "女" if self.user_info.get("性别").get("女").active else "男"
        return gender

    def about(self, *args, **kwargs):
        from kivy.metrics import Metrics

        dpi = Metrics.dpi
        txt = f"""
此软件是一个游戏软件，不涉及任何封建迷信内容。
软件版本号 {version_code}  屏幕dpi ：{dpi}

使用方法
    在农历栏输入自己的出生年月日时，用-进行分隔，然后点击排盘即可。
    例如如2000年1月1日2点55分，需要输入的是2000-1-1-2,不需要输入分钟数
    如果不知道自己的农历生日，可以输入公历生日进行排盘，日历农历有一个就行。
每一个星耀都可以点击查看它的属性信息,后续看看情况，如果需要的话可以添加每个星耀的详情信息
年龄使用的是虚岁，以正月初一为岁与岁的分界线
三方四正线可以点击每个宫和对应的内脏行切换，如亥或者三焦，将切换为亥宫的三方四正，排盘之后默认显示命宫的三方四正
关于先天卦和后天卦可以点击进行查看倪师在视频里对这个卦的先天后天批注，以及对应的卦图，但是请注意，一切均来自卦图，
倪师在视频里进行讲解的时候并未完全整理完成，所以供使用者参考，实际使用应当自己读图取象效果会更好。

软件不需要任何无关使用的手机权限，也不会接收任何更新，如果您想使用更新的版本，请登录app网址进行下载使用
此软件为完全遵照倪师在网上的资料进行设计之所以有四柱和排盘八字两个八字，
是因为紫薇斗数和易经推命使用的八字对一年的开始的定义不一样。
在这个软件上易经推命用的是八字，斗数用的是排盘八字（与倪师在往上的资料一致）
目前添加了紫薇斗数部分和关于易经推命的部分，易经推命的部分批注是倪师重新批过的，不是吴修名版本的内容
我测试的样例中和其他易经推命的排盘结果是一样的，但是如果您使用发现易经推命有什么不对的，请联系我进行改正
有任何建议或使用遇到问题请联系我的邮箱 103b6051@mail.nkut.edu.tw
或者直接扫码加群进行沟通，另外感谢使用此软件，也感谢帮助完善此软件的玩家

        
-                                                       2024年2月2日 
        
## 版权声明
本软件使用了Noto Sans Simplified Chinese字体。
版权所有 © 2015-2023 Adobe Systems Incorporated, Google LLC and other contributors.
此字体软件根据 SIL 开放字体许可证 (SIL Open Font License) 1.1 版授权。
此许可证可在 https://fonts.google.com/noto/specimen/Noto+Sans+SC 上获得。
        """
        picture = os.path.join(my_dir, "data", "picture", "qun.jpg")
        im = Image(source=picture, size_hint=(1, None), size=(400, 800))
        link = HyperlinkLabel()

        message_popup(txt, im, link=link)

    def start(self, button, *args, **kwargs):
        global last_editd

        if self.pai_pan is None:
            message_popup("尚未传递排盘方法")
            return

        if last_editd == "农历":
            ming_pan_time = self.get_nong_li_pan_time()
            # print("农历")
        else:
            ming_pan_time = self.get_ri_li_pan_time()

        # if not self.user_info.get("农历").text == "":
        #     ming_pan_time = self.get_nong_li_pan_time()
        #     # print("农历")
        # else:
        #     ming_pan_time = self.get_ri_li_pan_time()

        if not ming_pan_time is None:
            gender = self.get_gender()
            p = Pan(ming_pan_time, gender)
            # 计算流年卦
            dong_zhi_hou_xia_zhi_qian = ming_pan_time.is_xia_zhi_qian()
            res = get_liu_nian_gua(p.ba_zi, ming_pan_time.nian, gender, dong_zhi_hou_xia_zhi_qian)
            user_liu_nian_guas = {}
            count = 0
            for gua in res:
                count += 1
                liu_yues = get_liu_yue_gua(gua)
                gua.liu_yues = liu_yues
                user_liu_nian_guas[count] = gua
            p.liu_nian_guas = user_liu_nian_guas  # 将流年卦增加到排盘上
            self.pai_pan(p)
            bazi = "".join(ming_pan_time.get_ba_zi())
            res = get_xian_tian_gua(bazi, gender, ming_pan_time.nian)
            xian_tian_gua = Gua.find_gua(res[0])
            xian_tian_gua.yuan_tang_yao = xian_tian_gua.get_yuan_tang(bazi[-1])
            hou_tian_gua = get_hou_tian_gua(res[1], res[2], ming_pan_time.sdz, dong_zhi_hou_xia_zhi_qian)
            self.pan_windows.user.user_info.get("性别").get(gender).active = True
            self.pan_windows.user.user_info.get("先天卦").text = xian_tian_gua.name
            self.pan_windows.user.user_info.get("后天卦").text = hou_tian_gua.name
            self.pan_windows._update_rect(None, None)
        else:
            return

    def save_user_list(self, *args, **kwargs):
        users_ui = UserListDialogScreen(event=self.open_db_item)
        users_screen.clear_widgets()
        users_screen.add_widget(users_ui)
        screen_manager.current = "users_screen"

    def open_db_item(self, info):
        def ff(*args, **kwargs):
            self.user_info.get("性别").get(info.gender).active = True
            self.user_info.get("农历").text = info.birthday
            self.user_info.get("日历").text = ""
            self.user_info.get("姓名").text = info.name
            screen_manager.current = "main_screen"
            self.start(None)

        return ff

    def test(self, *args, **kwargs):
        for year in range(1840, 3000):
            for m in range(1, 12):
                self.user_info.get("农历").text = f"{year}-{m}-01-05"
                self.start(None)
            print(year)
