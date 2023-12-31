#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/20 16:23
# @Author  : huangfujue
# @File    : DialogScreenUI.py
# @Date    : 2023/11/20 
"""
模块说明
"""

# ----------------------------------------------------------------------------------------------------------------------
import os
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.button import Button, Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from tianji.ui.FontSetModule import set_font, font_size
from tianji.ui.screen_manager_module import  screen_manager


class WhitePopup(Popup):

    def __init__(self, **kwargs):
        super(WhitePopup, self).__init__(**kwargs)
        self.auto_dismiss=False
        self.background_color = (204, 204, 204, 1)



class OpenFileDialog(WhitePopup):
    def __init__(self, title, fun=None, default_dir=None, **kwargs):

        super(OpenFileDialog, self).__init__(**kwargs)
        self.title = title
        self.fun = fun
        self.default_dir = "" if default_dir is None else default_dir
        self.size_hint = (0.98, 0.98)
        self.background_color=(0.5,0.5,0.5,0.5)
        self.init()

    def init(self):

        layout = BoxLayout(orientation='vertical')
        btn_height = 45
        btn_layout = BoxLayout(size_hint=(1, None), size=(180, btn_height), spacing=15)

        select_button = Button(text='打开', on_press=self.select_file, size_hint=(None, None), size=(180, btn_height))
        chanel_button = Button(text='取消', on_press=self.chanel, size_hint=(None, None), size=(180, btn_height))
        delete_button = Button(text='删除', on_press=self.delete_file, size_hint=(None, None), size=(180, btn_height))
        self.filechooser = FileChooserIconView(path=self.default_dir, dirselect=False, size_hint=(0.9, 0.9))

        set_font(select_button, chanel_button, delete_button, self, self.filechooser)

        btn_layout.add_widget(chanel_button)
        btn_layout.add_widget(Label(size_hint=(1, None), size=(180, btn_height)))
        btn_layout.add_widget(select_button)
        btn_layout.add_widget(delete_button)
        layout.add_widget(btn_layout)
        layout.add_widget(self.filechooser)
        # self.add_widget(layout)
        self.content = layout

    def select_file(self, instance):
        if len(self.filechooser.selection) > 0:
            file = self.filechooser.selection[0]
            if os.path.isfile(file):
                self.dismiss()
                self.fun(file)

    def chanel(self, instance):
        self.dismiss()
        self.fun(None)

    def delete_file(self, instance):

        if len(self.filechooser.selection) > 0:
            file = self.filechooser.selection[0]
        else:
            return

        def yes_no(yes):
            if yes:
                if os.path.isfile(file):
                    try:
                        os.remove(file)
                        message_popup("已删除")

                    except Exception as E:
                        message_popup("删除失败\n\n" + str(E))
                    finally:
                        self.update()
                else:
                    message_popup(f"未找到文件： {file}")
                    self.update()

        YesNoPopup(f"确定要删除此文件吗\n\n\n{file}", operate_fun=yes_no).open()

    def update(self):
        current_path = self.filechooser.path
        up_oath = os.path.dirname(current_path)
        self.filechooser.path = up_oath
        self.filechooser.path = current_path


class SaveFileDialog(OpenFileDialog):
    def __init__(self, title, fun=None, default_dir=None, file_name=None, **kwargs):
        self.file_name = "" if file_name is None else file_name
        super(SaveFileDialog, self).__init__(title, fun, default_dir, **kwargs)

        self.init()

    def init(self):
        layout = BoxLayout(orientation='vertical')
        btn_height = 45
        btn_layout = BoxLayout(size_hint=(1, None), size=(180, btn_height), spacing=15)

        submit_button = Button(text='保存', on_press=self.submit, size_hint=(None, None), size=(180, btn_height))
        chanel_button = Button(text='取消', on_press=self.dismiss, size_hint=(None, None), size=(180, btn_height))
        delete_button = Button(text='删除', on_press=self.delete_file, size_hint=(None, None), size=(180, btn_height))

        self.filechooser = FileChooserIconView(path=self.default_dir, dirselect=False, size_hint=(0.9, 0.9))
        self.saveinput = TextInput(text=self.file_name, multiline=False, size_hint_y=None, height=btn_height)
        self.saveinput.hint_text = "文件名.png       不需要添加拓展名"
        set_font(submit_button, chanel_button, delete_button, self.saveinput, self, self.filechooser)

        btn_layout.add_widget(chanel_button)
        btn_layout.add_widget(Label(size_hint=(1, None), size=(180, btn_height)))
        btn_layout.add_widget(delete_button)
        btn_layout.add_widget(submit_button)

        layout.add_widget(self.saveinput)
        layout.add_widget(btn_layout)
        layout.add_widget(self.filechooser)

        # self.add_widget(layout)
        self.content = layout

    def submit(self, *args, **kwargs):

        if self.saveinput.text.strip() == "":
            return

        file_name = os.path.join(self.filechooser.path, f"{self.saveinput.text}.png")
        if not os.path.exists(self.filechooser.path):
            os.makedirs(self.filechooser.path)

        if os.path.exists(file_name) and os.path.isfile(file_name):
            YesNoPopup("文件已存在，是否覆盖已有文件？",
                       operate_fun=lambda res: self.fun(file_name) if res else None).open()
        else:
            self.fun(file_name)
        self.dismiss()


class YesNoPopup(WhitePopup):

    def __init__(self, message="", operate_fun=None, **kwargs):
        super(YesNoPopup, self).__init__(**kwargs)
        self.operate_fun = operate_fun
        content = BoxLayout(orientation="vertical")
        content.spacing = 20
        operate = BoxLayout(orientation="horizontal", spacing=15, size_hint_y=0.15)

        label_container = BoxLayout(orientation="vertical", spacing=80, size_hint_y=None)
        label_container.bind(minimum_height=label_container.setter('height'))
        scroll_view = ScrollView()
        scroll_view.add_widget(label_container)
        message = "\n\n" + message
        lines = message.splitlines()
        for l in lines:
            label = Label(text=l, text_size=(800, None))
            set_font(label)
            #label.color = (1, 1, 1, 1)
            label.font_size = font_size+2
            label.font_halign = "left"
            label_container.add_widget(label)

        yes_button = Button(text='确定', size_hint=(1, None), size=(400, 40))
        no_button = Button(text='取消', size_hint=(1, None), size=(400, 40))
        operate.add_widget(yes_button)
        operate.add_widget(no_button)

        self.size = (400, 800)
        self.size_hint = (0.98, None)
        self.title = ""

        content.add_widget(scroll_view)
        content.add_widget(operate)
        self.content = content

        set_font(yes_button, no_button, content, self)
        no_button.on_press = self.no
        yes_button.on_press = self.yes

    def no(self):
        super().dismiss()
        if not self.operate_fun is None:
            self.operate_fun(False)
        self.res = False

    def yes(self):
        super().dismiss()
        if not self.operate_fun is None:
            self.operate_fun(True)
        self.res = True


def message_popup(msg=None,picture=None):
    title = '你的输入有误，请检查 ' if msg is None else msg
    contex = BoxLayout(orientation="vertical")
    popup = WhitePopup(title="",
                       content=None,
                       size_hint=(0.98, None), size=(400, 1000))

    button = Button(text='确定', size_hint=(1, None), size=(400, 40))
    label_container = BoxLayout(orientation="vertical", spacing= 80, size_hint_x=1,size_hint_y=None)
    label_container.bind(minimum_height=label_container.setter('height'))


    scroll_view = ScrollView(size_hint=(1, 1))

    # label = Label(text=msg, text_size=(400, None))
    # set_font(label)
    # label.color = (1, 1, 1, 1)
    # label.font_size = font_size
    # label.font_halign ="left"
    #label_container.add_widget(label)

    title = "\n" + title
    lines = title.splitlines()
    for l in lines:

        if l.strip() == "\n":
            continue

        label = Label(text=l, text_size=(800, None))
        set_font(label)
        #label.color = (1, 1, 1, 1)
        label.font_size = font_size+2
        label.font_halign = "left"
        label_container.add_widget(label)

    if not picture is None:
        im=Image(source=picture,size_hint=(1, None), size=(400, 1000))

        label_container.add_widget(im)

    scroll_view.add_widget(label_container)
    contex.add_widget(scroll_view)
    contex.add_widget(button)

    popup.content = contex
    set_font(button, contex, popup)

    button.on_press = lambda: popup.dismiss()
    popup.open()
    return popup






class MyApp(App):
    def build(self):
        button = Button(text='open file')
        button.bind(on_press=self.show_filechooser)
        return button

    def show_filechooser(self, instance):
        open_path = r"D:\pycharm\pythonProject1\wsl\tianji\data"
        WhitePopup().open()


if __name__ == '__main__':
    MyApp().run()
