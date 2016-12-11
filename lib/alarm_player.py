import os
from subprocess import Popen
from time import sleep

class AlarmPlayer:
    def __init__(self):
        self.proc = None
        self.is_stopped = False

    def play(self):
        cmd = 'aplay -D hw:1,0 %s' % os.path.dirname(__file__) + '/../assets/sounds/alarm.wav'
        self.proc = Popen(cmd.strip().split(' '))

        while True:
            if self.proc.poll() == 0 and not self.is_stopped:
                self.play()
                break
            sleep(0.2)

    def terminate(self):
        self.is_stopped = True
        if self.proc.poll() is None:
            self.proc.terminate()
