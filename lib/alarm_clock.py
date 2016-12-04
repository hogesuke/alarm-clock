import os
from datetime import datetime, time
from subprocess import Popen
from time import sleep

class AlarmClock:
    def __init__(self, hour=5, minute=0, second=0):
        self.alarm_time = time(hour, minute, second, 0)
        self.wakeuped = False
        self.day = datetime.today().day

        self.run()

    def run(self):
        while True:
            if self.__is_wakeup_time:
                self.sound()
                self.wakeuped = True

            if self.__is_changed_day:
                self.wakeuped = False

            sleep(1)

    def sound(self):
        cmd = os.path.dirname(__file__) + '/../bin/sound_alarm'
        proc = Popen(cmd.strip().split(' '))

    def __is_wakeup_time(self):
        return self.alarm_time < datetime.now().time() and not self.wakeuped

    def __is_changed_day(self):
        current_day = datetime.today().day

        if self.day != current_day:
            self.day = current_day
            return True
        else:
            return False
