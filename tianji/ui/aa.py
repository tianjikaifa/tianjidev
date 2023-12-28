from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        l=BoxLayout()
        image = Image(source=r'D:\pycharm\pythonProject1\tianji\data\picture\qun.jpg')
        image.scale = 0.5
        l.add_widget(image)
        return l

if __name__ == '__main__':
    MyApp().run()