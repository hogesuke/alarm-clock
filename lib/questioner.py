import webiopi
import random
import curses
from time import sleep

from liquidcrystal import LiquidCrystal

class Questioner:

    def __init__(self, q_count=5):
        self.lcd = LiquidCrystal(7, 8, 25, 24, 23, 18)
        self.lcd.clear()
        self.q_count = q_count

    def start(self):
        for i in range(1, self.q_count + 1):
            self.__question(i)

    def __question(self, q_num):
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        ope = random.choice(['+', '-'])
        ans = None

        if ope == '+':
            ans = x + y
        elif ope == '-':
            ans = x - y

        self.lcd.clear()
        self.lcd.set_cursor(0, 0)
        self.lcd.write('Q%d %d %s %d =' % (q_num, x, ope, y))

        curses.wrapper(self.__read_input, ans)

    def __read_input(self, scr, ans):
        print(ans)
        while True:
            sleep(0.1)

            c = scr.getch()

            if c == ord('q'):
                break
