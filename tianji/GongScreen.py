#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/18 23:50
# @Author  : huangfujue
# @File    : GongScreen.py
# @Date    : 2023/11/18 
"""
十二个宫可视化部分组件
"""
import os

# ----------------------------------------------------------------------------------------------------------------------


from kivy.uix.button import Button, Label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class GongScreen(BoxLayout):
    def __init__(self, gong_obj=None, **kwargs):
        kwargs["orientation"] = "vertical"
        super(GongScreen, self).__init__(**kwargs)

        self.info = [
            f"{gong_obj.gong_tian_gan}{gong_obj.location}",  # 宫天干+ 宫位
            gong_obj.da_xian,  # 大流年
            gong_obj.name,  # 宫所主的名称

        ]

        # 表示这个宫的不同等级的星耀
        self.stars = gong_obj.stars

        m = BoxLayout()
        t = BoxLayout()
        t_l = BoxLayout()
        t_r = BoxLayout()
        b = BoxLayout()
        b_l = BoxLayout()
        b_r = BoxLayout()
        t.add_widget(t_l)
        t.add_widget(t_r)
        b.add_widget(b_l)
        b.add_widget(b_r)
        self.add_widget(t)
        self.add_widget(m)
        self.add_widget(b)
        font_size=15
        t_l.add_widget(StarListScreen(star_list=self.stars.get("甲"), f_size=font_size, orientation='vertical'))
        t_r.add_widget(StarListScreen(star_list=self.stars.get("乙"), f_size=font_size, orientation='vertical'))
        b_l.add_widget(StarListScreen(star_list=self.stars.get("丙"), f_size=font_size, orientation='vertical'))
        b_r.add_widget(StarListScreen(star_list=self.stars.get("丁"), f_size=font_size, orientation='vertical'))
        m.add_widget(StarListScreen(star_list=self.info,f_size=font_size, orientation='vertical'))


class StarListScreen(BoxLayout):
    def __init__(self, star_list, **kwargs):
        #kwargs["spacing"] = 10
        f_size = kwargs.pop("f_size")

        super(StarListScreen, self).__init__(**kwargs)
        for star in star_list:
            button = Label(text=star)
            button.font_size = f_size

            button.font_name = os.path.join(os.path.dirname(__file__), "config", "font", "simsun.ttc")

            button.font_blended = True
            button.color = (0, 0, 0, 1)
            self.add_widget(button)


class PApp(App):

    def build(self):
        app = GongScreen("123")
        return app


if __name__ == '__main__':
    app = PApp()
    app.run()
