import os.path
import sqlite3
from datetime import datetime

import pyaudio
import wave
from kivy.app import App
from kivy.metrics import sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
import tianji.proj_config  as pro_config


class LuYin:
    def __init__(self,idid,pid,file_path):
        self.pid=pid
        self.id=id
        self.file_path=file_path




class MyAudio:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.recording = False
        self.can_be_Recording = True

    def start_record(self,*args,**kwargs):
        if not self.recording:
            self.CHUNK = 1024
            self.FORMAT = pyaudio.paInt16
            self.CHANNELS = 1
            self.RATE = 44100
            self.RECORD_SECONDS = None  # 实时录音，不设定固定时长

            self.stream = self.p.open(format=self.FORMAT,
                                      channels=self.CHANNELS,
                                      rate=self.RATE,
                                      input=True,
                                      frames_per_buffer=self.CHUNK)

            self.recording = True
            Clock.schedule_interval(self.collect_audio_data, 1.0 / (self.RATE / self.CHUNK))

    def stop_record(self,file_name,*args,**kwargs):
        if self.recording:
            self.recording = False
            Clock.unschedule(self.collect_audio_data)
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()

            wf = wave.open(file_name, 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self.frames))
            wf.close()
    def collect_audio_data(self, _):
        if self.recording:
            data = self.stream.read(self.CHUNK)
            self.frames.append(data)

    def create_bind_function(self,pid):
        def ff(*args,**kwargs):
            """
            按钮点击事件，点一次创建一个，保存一个
            :param args:
            :param kwargs:
            :return:
            """
            if self.can_be_Recording:
                button=args[0]
                if button.text == "Start Recording":
                    self.start_record()
                    button.text = "Stop Recording"
                else:
                    # pid_当前系统时间为后缀
                    file_name=os.path.join(pro_config.luyin_dir,f"{pid}_{int(datetime.now().timestamp())}.wav")
                    self.stop_record(file_name)
                    button.text = "已结束"
                    self.can_be_Recording = False
                    self.insert(pid,luyin_file_path=file_name)

        return ff
    def insert(self,pid,luyin_file_path):
        # 连接到SQLite数据库
        conn = sqlite3.connect(pro_config.users_db_path)
        cursor = conn.cursor()
        # 创建一个批注的表
        cursor.execute('''CREATE TABLE IF NOT EXISTS pizhu
                          (   id INTEGER PRIMARY KEY,
                          pid INTEGER, 
                          luyin TEXT);
                          ''')
        cursor.execute(
            f"INSERT INTO pizhu (pid, luyin) VALUES ('f{pid}','f{luyin_file_path}');")
        cursor.close()
        conn.commit()
        conn.close()

    def delete(self,id):
        pass


    def update(self,id):
        pass

    @staticmethod
    def queryAll(pid):
        """
        查询指定的排盘对象的所有录音批注
        :param pid: 排盘对象的id
        :return:
        """
        list_pizhu = []
        conn = sqlite3.connect(pro_config.users_db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS pizhu
                          (   id INTEGER PRIMARY KEY,
                          pid INTEGER, 
                          luyin TEXT);
                          ''')

        cursor.execute("SELECT id,pid,luyin FROM pizhu ORDER BY id DESC ;")

        for item in cursor:
            info = LuYin(item[0],item[1],item[2])
            list_pizhu.append(info)

        cursor.close()
        conn.close()

        # 应群友的建议，删除后的记录数量应该与当前记录数一致
        i=len(list_pizhu)
        for luyin in list_pizhu:
            luyin.label_id=i
            i-=1
        return list_pizhu


def luyin_player(file):
    Player
    player = Player(filename=file)
    player.play()

class AudioRecorderApp(App):
    def __init__(self):
        super().__init__()
        self.audio=MyAudio()


    def build(self):
        btn_start = Button(text="Start Recording",size_hint=(None,None),size=(sp(300),sp(120)))
        btn_start.bind(on_press=self.audio.create_bind_function(11))
        btn_player = Button(text="Start Recording", size_hint=(None, None), size=(sp(300), sp(120)))
        btn_player.bind(on_press=self.audio.create_bind_function(11))
        layout = BoxLayout()
        layout.add_widget(btn_start)
        layout.add_widget(btn_player)
        return layout

if __name__ == "__main__":
    AudioRecorderApp().run()
