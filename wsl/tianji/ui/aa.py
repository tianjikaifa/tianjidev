from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.app import App
class MyDropDown(BoxLayout):
    def __init__(self,**kwargs):
        super(MyDropDown).__init__(**kwargs)
        l=BoxLayout("")
        input = TextInput(multiline=False)
        but = TextInput(multiline=False)
        dp = DropDown()
        dp.bind(on_select=lambda instance, x: setattr(input, 'text', x))
        for i in range(100):
            item = Button(text='hello %d' % i, size_hint_y=None, height=44)
            item.bind(on_release=lambda btn: dp.select(btn.text))
            dp.add_widget(item)
        dp.open()

class PhoneApp(App):

    def build(self):
        app = MyDropDown()

        return app



app = MyDropDown()
app.title = "天纪 v1.0  --测试版本"
app.run()
