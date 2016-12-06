import threading
from datetime import datetime, time, timedelta
from time import sleep
from alarm_player import AlarmPlayer
from touch_sensor import TouchSensor

class AlarmClock:
    def __init__(self, hour=5, minute=0, second=0):
        self.alarm_time = time(hour, minute, second, 0)
        self.is_invoked = self.alarm_time < datetime.now().time()
        self.is_plaing = False
        self.is_pausing = False
        self.day = datetime.today().day
        self.start_datetime = None
        self.player = AlarmPlayer()
        self.sensor = TouchSensor()

        self.run()

    def run(self):
        while True:
            sleep(1)

            if self.is_plaing:
                sleep(0.2)

                if self.is_pausing and not self.sensor.is_touched():
                    self.is_pausing = False
                    self.__sound()
                    continue

                if not self.is_pausing and self.sensor.is_touched():
                    self.is_pausing = True
                    self.player.terminate()
                    continue

                if self.__is_time_out(self.start_datetime):
                    self.is_plaing = False
                    self.player.terminate()
                    continue

            if self.__is_wakeup_time():
                self.__sound()

            if self.__is_changed_day():
                self.is_invoked = False

    def __sound(self):
        self.start_datetime = datetime.now()

        th = threading.Thread(target=self.__play, name='sound_thread')
        th.setDaemon(True)
        th.start()

        self.is_invoked = True
        self.is_plaing = True

    def __play(self):
        self.player.play()

    def __is_wakeup_time(self):
        return self.alarm_time <= datetime.now().time() and not self.is_invoked

    def __is_time_out(self, start_datetime):
        return (start_datetime + timedelta(minutes=10)).time() <= datetime.now().time()

    def __is_changed_day(self):
        current_day = datetime.today().day

        if self.day != current_day:
            self.day = current_day
            return True
        else:
            return False
