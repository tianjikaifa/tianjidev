#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/20 16:23
# @Author  : huangfujue
# @File    : Dialog.py
# @Date    : 2023/11/20 
"""
模块说明
"""

# ----------------------------------------------------------------------------------------------------------------------
import os
from kivy.app import App
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button, Label

from tianji.ui.font_set import set_font


class FileChooserPopup(Popup):
    def __init__(self, title, fun=None, default_dir=None, **kwargs):

        super(FileChooserPopup, self).__init__(**kwargs)
        self.title = title
        self.fun = fun


        default_dir = "" if default_dir is None else default_dir
        layout = BoxLayout(orientation='vertical')
        btn_layout = BoxLayout()
        bth_height = 0.2
        btn_width = 0.18

        select_button = Button(text='打开', on_release=self.select_file, size_hint_x=btn_width, size_hint_y=bth_height)
        chanel_button = Button(text='取消', on_release=self.chanel, size_hint_x=btn_width, size_hint_y=bth_height)
        delete_button = Button(text='删除', on_release=self.delete_file, size_hint_x=btn_width, size_hint_y=bth_height)
        self.filechooser = FileChooserIconView(path=default_dir, dirselect=True, size_hint_y=0.9)

        set_font(select_button, chanel_button, delete_button, self.filechooser)
        chanel_button.color = (1, 1, 1, 1)
        select_button.color = (1, 1, 1, 1)
        delete_button.color = (1, 1, 1, 1)

        btn_layout.add_widget(chanel_button)
        btn_layout.add_widget(Label(size_hint_x=0.8, size_hint_y=bth_height))
        btn_layout.add_widget(select_button)
        btn_layout.add_widget(delete_button)
        btn_layout.size_hint_y = bth_height
        layout.add_widget(btn_layout)
        layout.add_widget(self.filechooser)
        self.add_widget(layout)

    def updae_tile(self, filechooser, file):
        if os.path.isfile(file):
            self.title = file

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
            if os.path.isfile(file):
                try:
                    os.remove(file)
                except Exception as E:
                    error_popup("删除失败\n\n"+str(E))


def error_popup( error=None):
        title = '你的输入有误，请检查 ' if error is None else error
        contex = BoxLayout(orientation="vertical")
        label = Label(text=title)
        button = Button(text='确定', size_hint=(1, None), size=(400, 40))

        contex.add_widget(label)
        contex.add_widget(button)
        popup = Popup(title="",
                      content=contex,
                      size_hint=(0.9, None),
                      size=(400, 400))

        set_font(button, label, contex, popup)
        label.color = (1, 1, 1, 1)
        button.color = (1, 1, 1, 1)
        button.on_release = lambda : popup.dismiss()
        popup.open()


class MyApp(App):
    def build(self):
        button = Button(text='open file')
        button.bind(on_release=self.show_filechooser)
        return button

    def show_filechooser(self, instance):
        open_path = r"D:\pycharm\pythonProject1\tianji"
        FileChooserPopup("choose you file to open ", print, default_dir=open_path).open()


if __name__ == '__main__':
    MyApp().run()
