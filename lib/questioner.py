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
        operator = random.choice(['+', '-'])

        self.lcd.clear()
        self.lcd.set_cursor(0, 0)
        self.lcd.write('Q%d %d %s %d =' % (q_num, x, operator, y))

        scr = self.__start_input()

        while True:
            sleep(0.1)

            c = scr.getch()
            print(c)

            if c == ord('q'):
                break

        self.__end_input(scr)

    def __start_input(self):
        scr = curses.initscr()
        scr.nodelay(1)
        scr.keypad(1)
        curses.noecho()
        curses.cbreak()
        return scr

    def __end_input(self, scr):
        scr.nodelay(0)
        scr.keypad(0)
        curses.nocbreak()
        curses.echo()
