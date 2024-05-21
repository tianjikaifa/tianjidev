import kivy

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.core.audio import SoundLoader
from kivy.uix.progressbar import ProgressBar


class MyAudio(App):
    def build(self):
        # 创建一个布局控件
        layout = BoxLayout(orientation='vertical')

        # 创建标签控件
        label = Label(text="play")
        layout.add_widget(label)

        # 创建进度条控件
        progress_bar = ProgressBar(max=100)
        layout.add_widget(progress_bar)

        # 加载 WAV 文件
        sound = SoundLoader.load(r"D:\pycharm\pythonProject1\tianji\data\luyin_files\11_1713850768.wav")

        # 将播放声音的功能绑定到标签控件的 on_touch_down 事件
        label.bind(on_touch_down=lambda widget, touch: self.play_audio(sound, progress_bar))

        return layout

    def play_audio(self, sound, progress_bar):
        # 播放声音
        sound.play()

        # 更新进度条
        def update_progress_bar(dt):
            progress = sound.get_progress() * 100
            progress_bar.value = progress

            if progress == 100:
                # 播放完成
                sound.stop()

        # # 每 10 毫秒更新进度条一次
        Clock.schedule_interval(update_progress_bar, 0.01)




if __name__ == "__main__":
    MyAudio().run()
