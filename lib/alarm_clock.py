from datetime import time
from subprocess import Popen
from time import sleep

class AlarmClock:
    def __init__(self):
        self.alarm_time = time(5, 0, 0, 0)

    def alarm(self):
        cmd = '../bin/play'
        proc = Popen(cmd.strip().split(' '))
        sleep(5)
        proc.terminate()
