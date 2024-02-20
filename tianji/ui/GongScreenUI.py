#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2023/11/18 23:50
# @Author  : huangfujue
# @File    : GongScreenUI.py
# @Date    : 2023/11/18 
"""
十二个宫可视化部分组件
"""

# ----------------------------------------------------------------------------------------------------------------------


from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line
from kivy.uix.button import Button, Label

from tianji.config.zi_wei_dou_shu.xing_chen_biao_module import dou_shu_stars
from tianji.ui.DialogScreenUI import message_popup
from tianji.ui.FontSetModule import set_font


class GongScreen(BoxLayout):
    def __init__(self, gong_obj=None,screen_obj=None, **kwargs):
        kwargs["orientation"] = "vertical"
        kwargs["padding"] = 5
        super(GongScreen, self).__init__(**kwargs)

        self.screen_obj=screen_obj
        self.other_info = [
            f"{gong_obj.gong_tian_gan}{gong_obj.location}",  # 宫天干+ 宫位
            gong_obj.nei_zang,  # 内脏
            # gong_obj.qu_gan,  # 躯干

        ]

        self.gong_info = [

            gong_obj.da_xian,  # 大流年
            gong_obj.name,  # 宫所主的名称
        ]
        if gong_obj.shen_gong:
            self.gong_info.append("身宫")
        # 表示这个宫的不同等级的星耀
        self.stars = gong_obj.stars

        m = BoxLayout()
        t = BoxLayout()
        t_l = BoxLayout()
        t_r = BoxLayout()
        b = BoxLayout()

        b_l = BoxLayout()
        b_r = BoxLayout()
        b_m = BoxLayout()
        t.add_widget(t_l)
        t.add_widget(t_r)
        b.add_widget(b_l)
        b.add_widget(b_m)
        b.add_widget(b_r)
        self.add_widget(t)
        self.add_widget(m)
        self.add_widget(b)
        t.size_hint_y = 0.5
        m.size_hint_y = 0.16
        b.size_hint_y = 0.34
        dui_qi_fang_shi = "vertical"  # horizontal
        t_l.add_widget(StarListScreen(star_list=self.stars.get("甲"), orientation=dui_qi_fang_shi))
        t_r.add_widget(StarListScreen(star_list=self.stars.get("乙"), orientation=dui_qi_fang_shi))
        b_l.add_widget(StarListScreen(star_list=self.stars.get("丙"), orientation=dui_qi_fang_shi))
        b_r.add_widget(StarListScreen(star_list=self.stars.get("丁"), orientation=dui_qi_fang_shi))
        m.add_widget(StarListScreen(star_list=self.other_info, orientation=dui_qi_fang_shi,event=self.on_touch_up_envent(gong_obj.location)))
        b_m.add_widget(StarListScreen(star_list=self.gong_info, orientation=dui_qi_fang_shi,event=self.on_touch_up_envent(gong_obj.location)))

        self.bind(size=self._update_rect, pos=self._update_rect)

        with self.canvas.before:
            Color(0, 0, 0, 1)  # set the color to red
            self.rect = Line(rectangle=(self.x, self.y, self.width, self.height), width=1)



    def _update_rect(self, instance, value):
        self.rect.rectangle = (self.x, self.y, self.width, self.height)


    def on_touch_up_envent(self,location):

        def ff(*args,**kwargs):
            """
            totch envent
            :param touch:
            :return:
            """
            self.screen_obj.torch_gong=location
            self.screen_obj._update_rect(None,None)
            #print(self.screen_obj.torch_gong)
            return False

        return ff





class StarListScreen(BoxLayout):
    def __init__(self, star_list, **kwargs):

        event=kwargs.pop("event",None)
        self.align = ('left', 'top')
        super(StarListScreen, self).__init__(**kwargs)
        for star in star_list:
            res = self.find_star(star)
            if res[0]:
                button = Button(text=star)
                button.info = res[1].info
                # button.on_release =self.add_star_info(button)
                button.on_press = self.add_star_info(button)

            else:
                button = Button(text=star)
                if not event is None:
                    button.on_press=event

            set_font(button)
            button.font_blended = True
            button.background_color = (1, 1, 1, 1)

            if "顺行" in star or "逆行" in star:
                button.color = "#FF0000"

            # 四化星处理
            flag=True
            for temp in ["化权","化科","化禄","化忌"]:
                if temp in star:
                    new_star=BoxLayout(orientation="horizontal")
                    star_name=star.split(" ")[0]
                    button = Button(text=star_name,size=(30,30),size_hint=(1,None))
                    button2 = Button(text=temp,size=(40,22),size_hint=(None,None), bold=True)
                    button.info=res[1].info
                    button2.info=self.find_star(temp)[1].info
                    button.on_press = self.add_star_info(button)
                    button2.on_press = self.add_star_info(button2)
                    set_font(button,button2)


                    # button2.color =  "#3A500A"
                    # button2.background_color = (0.949,0.729,0.007, 1)
                    button2.color = (1, 1, 1, 1)
                    button2.background_color =  "#5EB125"
                    #button2.color = "#087982"
                    #button2.background_color = (1, 1, 1, 1)
                    button.background_color = (1, 1, 1, 1)

                    if temp == "化忌":
                        #button2.color = "#FF0000"
                        button2.color = (1, 1, 1, 1)
                        button2.background_color = "#EE545E"



                    new_star.add_widget(button)
                    new_star.add_widget(button2)
                    self.add_widget(new_star)
                    flag=False


            if flag :
                self.add_widget(button)




    def find_star(self, star=""):
        flag = False
        star_info = None
        for star_name in dou_shu_stars:
            if star.find(star_name) > -1:
                flag = True
                star_info = dou_shu_stars.get(star_name)
                break

        return [flag, star_info]

    def add_star_info(self, button):

        def ff(*args, **kwargs):

            message_popup(button.info)

        return ff
