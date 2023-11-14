#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/12 12:58
# @Author  : huangfujue
# @File    : 03.py
# @Date    : 2023/11/12 
"""
模块说明
"""
# ----------------------------------------------------------------------------------------------------------------------

from kivy.app import App
from kivy.event import EventDispatcher
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 4
        self.add_widget(Label(text='用户'))
        self.add_widget(TextInput(multiline=False))
        self.add_widget(Label(text='密码'))
        self.add_widget( TextInput(password=True, multiline=False))


class MyApp(App):

    def build(self):
        return LoginScreen()

class MyEventDispatcher(EventDispatcher):

    def __init__(self, **kwargs):
        self.register_event_type('on_mytest')
        super(MyEventDispatcher, self).__init__(**kwargs)

    def do_something(self, value):
        # when do_something is called, the 'on_test' event will be
        # dispatched with the value
        #
        self.dispatch('on_mytest', value)


    def on_mytest(self, *args):
        print("在回调之后触发", args)


if __name__ == '__main__':

    #MyApp().run()
    def my_callback(value, *args):
        print("回调参数", args)


    ev = MyEventDispatcher()
    ev.bind(on_mytest= my_callback)
    ev.do_something('测试参数')