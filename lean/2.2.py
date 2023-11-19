#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/18 21:48
# @Author  : huangfujue
# @File    : 2.2.py
# @Date    : 2023/11/18 
"""
一种更加灵活的方式进行调度前后的安排，
下边的例子表示在任务调度结束之后立刻就要额外做的事情
比如要做事情B

"""
from kivy.event import EventDispatcher


# ----------------------------------------------------------------------------------------------------------------------
class MyEventDispatcher(EventDispatcher):
    def __init__(self, **kwargs):
        self.register_event_type('on_test') # 在分发器中注册一个名叫on_test的方法，这个事件参数通常它用来表示这个分发器绑定的外部事件
        self.register_event_type('on_befo_test')
        self.register_event_type('on_after_test')
        super(MyEventDispatcher, self).__init__(**kwargs)

    def do_something(self, value):
        # when do_something is called, the 'on_test' event will be
        # dispatched with the value

        self.dispatch('on_befo_test', value )  # 再分发给 on_befo_test 方法
        self.dispatch('on_test', value+"156")  # 分发给外部回调,同时分发给自己的 on_test 方法
        self.dispatch('on_after_test', value+"156")  # 分发给外部回调

    def on_test(self, *args):
        print("I am  on call_back in call", args)


    def on_befo_test(self, *args):
        print("I am  on_befo_test call_back", args)

if __name__ == '__main__':
    def my_callback(value, *args):

        print("外部回调哦", args)


    ev = MyEventDispatcher() #
    ev.bind(on_test=my_callback)
    ev.do_something('test') #被别的地方触发了
