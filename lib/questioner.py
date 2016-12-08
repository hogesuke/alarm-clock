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

        self.start()

    def start(self):
        for i in range(1, self.q_count + 1):
            self.__question(i)
            webiopi.sleep(3.0)

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

        self.__end_input()



    def __start_input(self):
        scr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        return scr

    def __end_input(self):
        curses.nocbreak()
        curses.echo()
