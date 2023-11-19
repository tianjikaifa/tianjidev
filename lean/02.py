#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/18 20:40
# @Author  : huangfujue
# @File    : 02.py
# @Date    : 2023/11/18 
"""
模块说明
"""
# ----------------------------------------------------------------------------------------------------------------------
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return LoginScreen()




def my_callback(dt):
    """
    更优雅的非阻塞窗体执行的任务
    :param dt: 时间间隔
    :return:
    """

    print('My callback is called', dt)
# 将任务打包成为一个定时时间事件，并让调度器安排每秒执行两次的时间的间隔进行调用

event = Clock.schedule_interval(my_callback, 1 / 2.)

event.cancel()  # 取消调度该任务
Clock.unschedule(event)   # 从调度任务中移除这个任务


# 使用全局变量的狗屎代码
count = 0
def my_callback(dt):
    global count
    count += 1
    if count == 10:
        print('Last call of my callback, bye bye !')
        return False  #返回这个，相当于 event.cancel()
    print('My callback is called')
Clock.schedule_interval(my_callback, 1 / 30.)



# 一次性任务 的两种方式，下面这种开销大，
# 因为调度器实际上会在每次调度时先创建出来事件，再判断要不要去调度，而且任务事件长的化可能会发生重复调度的情况
print("一次性定时任务")
jiange=1 # 大于0 表示多少秒后调用，等于0表示 下一个重绘制画面后立马调用，-1 表示下次绘制画面之前就调用
def my_callback(dt):
    print('My callback is called !')

Clock.schedule_once(my_callback, jiange)


# First, schedule once.
event = Clock.schedule_once(my_callback, 0)

# Then, in another place you will have to unschedule first
# to avoid duplicate call. Then you can schedule again.
Clock.unschedule(event)
event = Clock.schedule_once(my_callback, 0)
# 一次性任务 的两种方式，推荐下面这种，这个方式表示任务是唯一的，不会被重复安排调度
trigger = Clock.create_trigger(my_callback)
# later
trigger()

if __name__ == '__main__':
    MyApp().run()