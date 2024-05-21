#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# @Time    : 2024-02-04 23:57
# @Author  : huangfujue
# @File    : user_db_module.py
# @Date    : 2024-02-04 
"""
模块说明
"""
# ----------------------------------------------------------------------------------------------------------------------
import sqlite3

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

import tianji.proj_config  as pro_config
from tianji.ui.BaseUI import MyScreen
from tianji.ui.DialogScreenUI import YesNoPopup
from tianji.ui.FontSetModule import set_font
from tianji.ui.screen_manager_module import main_win


class UserItem:
    def __init__(self, name, birthday, gender, save_time="", id=None):
        self.id = id
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.save_time = save_time

    def save_to_db(self):
        # 连接到SQLite数据库
        conn = sqlite3.connect(pro_config.users_db_path)
        cursor = conn.cursor()
        # 创建一个表格
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (   id INTEGER PRIMARY KEY,
                          name TEXT, 
                          birthday TEXT, 
                          gender TEXT, 
                          save_time TEXT);
                          ''')
        cursor.execute(
            f"INSERT INTO users (name, birthday, gender, save_time) VALUES ('{self.name}','{self.birthday}','{self.gender}','{self.save_time}');")
        cursor.close()
        conn.commit()
        conn.close()

    @staticmethod
    def delete_by_id(id):
        conn = sqlite3.connect(pro_config.users_db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (   id INTEGER PRIMARY KEY,
                          name TEXT, 
                          birthday TEXT, 
                          gender TEXT, 
                          save_time TEXT);
                          ''')
        count = cursor.execute(f"DELETE FROM users WHERE id={id};")
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def queryAll():
        user_infos = []
        conn = sqlite3.connect(pro_config.users_db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (   id INTEGER PRIMARY KEY,
                          name TEXT, 
                          birthday TEXT, 
                          gender TEXT, 
                          save_time TEXT);
                          ''')
        # cursor.execute("SELECT id,name, birthday, gender, save_time FROM users;")
        cursor.execute("SELECT id,name, birthday, gender, save_time FROM users ORDER BY id DESC ;")

        for item in cursor:
            # print(item)
            info = UserItem(
                id=item[0],
                name=item[1],
                birthday=item[2],
                gender=item[3],
                save_time=item[4])
            user_infos.append(info)

        cursor.close()
        conn.close()
        # 应群友的建议，删除后的记录数量应该与当前记录数一致
        i=len(user_infos)
        for user in user_infos:
            user.label_id=i
            i-=1
        return user_infos


class UserListDialogScreen(MyScreen):
    def __init__(self, **kwargs):
        self.bunton_event = kwargs.pop("event", None)
        super().__init__(**kwargs)
        box = BoxLayout(orientation="vertical", spacing=20, padding=10, )
        self.label_container = BoxLayout(orientation="vertical",
                                         spacing=80,
                                         padding=(0,80,0,0),
                                         size_hint_y=None)

        self.label_container.bind(minimum_height=self.label_container.setter('height'))
        # self.label_container.bind(minimum_height=self.label_container.setter('width'))
        self.item_height = 0.05
        users = UserItem.queryAll()

        for info in users:
            self.label_container.add_widget(self.create_user_info_item(info))

        scroll_view = ScrollView(size_hint=(0.95, 0.9))
        scroll_view.add_widget(self.label_container)
        box.add_widget(self.create_Label())
        box.add_widget(scroll_view)
        b = Button(text="返回", size_hint=(1, self.item_height))
        b.on_press = main_win
        set_font(b)
        box.add_widget(b)
        self.add_widget(box)

    def delete_user(self, id):
        def f(res):
            if res:
                UserItem.delete_by_id(id)
                for item in self.label_container.children:
                    if item.box_id == id:
                        self.label_container.remove_widget(item)
                        break
        def ff():
            y = YesNoPopup("是否删除这条记录", f)
            y.open()

        return ff

    def create_user_info_item(self, info):
        box = BoxLayout(orientation="horizontal", spacing=0, size_hint=(0.95, self.item_height))
        box.box_id = info.id

        # id = Button(text=f"{info.id}", size_hint=(self.item_height * 2, self.item_height))
        # name = Button(text=f"{info.name}", size_hint=(None,None))
        # gender = Button(text=f"{info.gender}", size_hint=(None,None))
        # birthday = Button(text=f"{info.birthday}", size_hint=(self.item_height * 4, self.item_height))
        # save_day = Button(text=f"{info.save_time}", size_hint=(self.item_height * 5, self.item_height))
        # delete = Button(text="删除", size_hint=(self.item_height * 2, self.item_height))

        id = Button(text=f"{info.label_id}", size_hint=(None, None), size=(100, 50))
        name = Button(text=f"{info.name}", size_hint=(None, None), size=(200, 50))
        gender = Button(text=f"{info.gender}", size_hint=(None, None), size=(100, 50))
        birthday = Button(text=f"{info.birthday}", size_hint=(None, None), size=(200, 50))
        save_day = Button(text=f"{info.save_time}", size_hint=(None, None), size=(250, 50))
        delete = Button(text="删除", size_hint=(None, None), size=(100, 50))
        delete.on_press = self.delete_user(info.id)

        set_font(id, name, gender, birthday, save_day, delete)

        id.on_press = self.bunton_event(info)
        name.on_press = self.bunton_event(info)
        gender.on_press = self.bunton_event(info)
        birthday.on_press = self.bunton_event(info)
        save_day.on_press = self.bunton_event(info)

        id.background_color = (0.95, 0.95, 0.95, 1)
        name.background_color = (0.95, 0.95, 0.95, 1)
        gender.background_color = (0.95, 0.95, 0.95, 1)
        birthday.background_color = (0.95, 0.95, 0.95, 1)
        save_day.background_color = (0.95, 0.95, 0.95, 1)
        delete.background_color = (0.95, 0.95, 0.95, 1)
        box.add_widget(id)
        box.add_widget(name)
        box.add_widget(gender)
        box.add_widget(birthday)
        box.add_widget(save_day)
        box.add_widget(delete)
        return box

    def create_Label(self):
        box = BoxLayout(orientation="horizontal", size_hint=(0.95, self.item_height))
        box.box_id = -1
        id = Label(text="编号", size_hint=(None, None), size=(100, 50))
        name = Label(text="姓名", size_hint=(None, None), size=(200, 50))
        gender = Label(text="性别", size_hint=(None, None), size=(100, 50))
        birthday = Label(text="农历日期", size_hint=(None, None), size=(200, 50))
        save_day = Label(text="保存日期", size_hint=(None, None), size=(250, 50))
        delete = Label(text="操作", size_hint=(None, None), size=(100, 50))
        # id = Label(text="编号", size_hint=(self.item_height * 2, self.item_height))
        # name = Label(text="姓名", size_hint=(self.item_height * 4, self.item_height))
        # gender = Label(text="性别", size_hint=(self.item_height * 2, self.item_height))
        # birthday = Label(text="农历日期", size_hint=(self.item_height * 4, self.item_height))
        # save_day = Label(text="保存日期", size_hint=(self.item_height * 5, self.item_height))
        # delete = Label(text="操作", size_hint=(self.item_height * 2, self.item_height))

        set_font(id,
                 name,
                 gender,
                 birthday,
                 save_day,
                 delete)

        box.add_widget(id)
        box.add_widget(name)
        box.add_widget(gender)
        box.add_widget(birthday)
        box.add_widget(save_day)
        box.add_widget(delete)
        return box
