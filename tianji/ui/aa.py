from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

from kivy.app import App


class MyDropDown(BoxLayout):
    def __init__(self, **kwargs):
        super(MyDropDown).__init__(**kwargs)
        l = BoxLayout()
        l.add_widget(Button(text="aa", on_release=self.fun))
        self.add_widget(l)
        # input = TextInput(multiline=False)
        # but = TextInput(multiline=False)
        # dp = DropDown()
        # dp.bind(on_select=lambda instance, x: setattr(input, 'text', x))
        # for i in range(100):
        #     item = Button(text='hello %d' % i, size_hint_y=None, height=44)
        #     item.bind(on_release=lambda btn: dp.select(btn.text))
        #     dp.add_widget(item)
        # dp.open()

    def fun(self, a, *args, **kwargs):
        a = App.root_window
        b = Button(text="bb")
        app.set


class ABCD(BoxLayout):
    def __init__(self, sm, name, **kwargs):
        super(ABCD).__init__(**kwargs)

        self.sm = sm
        self.name = name
        b = Button(text=name)
        b.on_release = self.fun
        self.add_widget(b)

    def fun(self,*args,**kwargs):
        self.sm.current = self.name


class PhoneApp(App):

    def build(self):
        self.screen_manager = ScreenManager()

        self.screen1 = Screen(name="main_screen")
        self.screen2 = Screen(name="screen2")

        self.screen_manager.add_widget(self.screen1)
        self.screen_manager.add_widget(self.screen2)
        self.screen_manager.current = "main_screen"

        self.screen1.add_widget(ABCD(self.screen_manager, "screen2"))
        self.screen2.add_widget(ABCD(self.screen_manager, "main_screen"))

        return self.screen_manager


app = PhoneApp()
app.title = "天纪 v1.0  --测试版本"
app.run()
