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

            # 停止
            if self.is_stopped:
                break

            # 繰り返し再生
            if self.proc.poll() == 0:
                self.play()
                break

            # 再生に失敗した場合、再実行
            if self.proc.poll() == 1:
                sleep(1)
                self.play()
                break

            sleep(0.2)

    def terminate(self):
        self.is_stopped = True

        if self.proc.poll() is None:
            self.proc.terminate()

            while self.proc.poll() is None:
                sleep(0.1)

    def resume(self):
        self.is_stopped = False
        self.play()
