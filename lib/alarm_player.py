import os
from subprocess import Popen
from time import sleep

class AlarmPlayer:
    def __init__(self):
        self.proc = None
        self.is_stoped = False

    def play(self):
        cmd = 'aplay -D hw:1,0 %s' % os.path.dirname(__file__) + '/../assets/sounds/alarm.wav'
        self.proc = Popen(cmd.strip().split(' '))

        while True:
            if self.proc.poll() == 0 or self.is_stoped:
                self.play()
                break
            sleep(0.2)

    def terminate(self):
        self.is_stoped = True
        self.proc.terminate()
