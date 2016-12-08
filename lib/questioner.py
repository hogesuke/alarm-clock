import webiopi
import random

from liquidcrystal import LiquidCrystal

class Questioner:

    def __init__(self, q_count=5):
        self.lcd = LiquidCrystal(7, 8, 25, 24, 23, 18)
        self.lcd.clear()
        self.q_count = q_count
        self.counter = 0

        self.start()

    def start(self):
        for i in range(1, self.q_count):
            self.__question(i)
            self.counter += 1
            webiopi.sleep(3.0)

    def __question(self, q_num):
        x = random.randint(1, 9999)
        y = random.randint(1, 9999)
        operator = random.choice(['+', '-'])

        self.lcd.set_cursor(0, 0)
        self.lcd.write('Q%d %d %s %d =' % (q_num, x, operator, y))
