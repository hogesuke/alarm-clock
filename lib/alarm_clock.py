import threading
from datetime import datetime, time, timedelta
from time import sleep
from alarm_player import AlarmPlayer
from touch_sensor import TouchSensor
from questioner import Questioner
from light_controller import LightController


class AlarmClock:
    def __init__(self, hour=5, minute=0, second=0, ws_url='ws://localhost:8080/light'):
        self.alarm_time = time(hour, minute, second, 0)
        self.is_invoked = self.alarm_time < datetime.now().time()
        self.day = datetime.today().day
        self.is_lightuped = False
        self.player = AlarmPlayer()
        self.sensor = TouchSensor()
        self.questioner = Questioner()
        self.light_controller = LightController(ws_url)

        self.run()

    def __init_status(self):
        self.is_plaing = False
        self.is_pausing = False
        self.start_datetime = None

    def run(self):
        self.__init_status()

        while True:
            sleep(0.1 if self.is_plaing else 1)

            if self.is_plaing:

                # タッチされていない間はアラーム再生
                if self.is_pausing and not self.sensor.is_touched():
                    self.is_pausing = False
                    self.__sound(True)
                    continue

                # タッチされている間はアラームの再生停止
                if not self.is_pausing and self.sensor.is_touched():
                    self.is_pausing = True
                    self.player.terminate()
                    continue

                # 一定時間以上経過で停止
                if self.__is_time_out(self.start_datetime):
                    self.__init_status()
                    self.player.terminate()
                    self.questioner.terminate()
                    continue

                # 全問正解で停止
                if self.questioner.has_completed():
                    self.__init_status()
                    self.player.terminate()
                    continue


            if not self.is_lightuped:
                if self.__is_lightup_time():
                    self.is_lightuped = True
                    self.light_controller.power_on()

            if not self.is_invoked:
                if self.__is_wakeup_time():
                    self.__sound()
                    self.__question()

            if self.__is_changed_day():
                self.is_invoked = False
                self.is_lightuped = False

    def __sound(self, resume=False):
        self.start_datetime = datetime.now()

        if resume:
            th = threading.Thread(target=self.__resume, name='sound_thread')
        else:
            th = threading.Thread(target=self.__play, name='sound_thread')

        th.setDaemon(True)
        th.start()

        self.is_invoked = True
        self.is_plaing = True

    def __play(self):
        self.player.play()

    def __resume(self):
        self.player.resume()

    def __question(self):
        th = threading.Thread(target=self.__calc, name='question_thread')
        th.setDaemon(True)
        th.start()

    def __calc(self):
        self.questioner.start()

    def __is_lightup_time(self):
        return self.alarm_time <= (datetime.now() + timedelta(minutes=5)).time()

    def __is_wakeup_time(self):
        return self.alarm_time <= datetime.now().time()

    def __is_time_out(self, start_datetime):
        return (start_datetime + timedelta(minutes=10)).time() <= datetime.now().time()

    def __is_changed_day(self):
        current_day = datetime.today().day

        if self.day != current_day:
            self.day = current_day
            return True
        else:
            return False
