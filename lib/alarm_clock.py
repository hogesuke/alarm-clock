import os
from datetime import time
from subprocess import Popen
from time import sleep

class AlarmClock:
    def __init__(self):
        self.alarm_time = time(5, 0, 0, 0)

    def alarm(self):
        cmd = 'aplay -D hw:1,0 %s' % os.path.dirname(__file__) + '/../assets/sounds/alarm.wav'
        proc = Popen(cmd.strip().split(' '))

        while True:
            if proc.poll() == 0:
                self.alarm()
                break
            sleep(0.5)
