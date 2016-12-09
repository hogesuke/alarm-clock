import random
import curses
import re
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
        input_str = ''
        ans_str = str(ans)

        while True:
            sleep(0.1)

            c = chr(scr.getch())

            if c == 'c':
                input_str = ''
                self.__clear_ans()
                continue  # clear

            if c == 's':
                break  # skip

            if self.__invalid_input(c, input_str):
                input_str = ''
                self.__clear_ans()
                continue  # error

            input_str += c

            if input_str == ans_str:
                self.__write_ans(input_str + ' GOOD!')
                sleep(1)
                break

            if len(input_str) == len(ans_str):
                self.__write_ans(input_str + ' NG')
                sleep(1)
                input_str = ''
                self.__clear_ans()
                continue

            self.__write_ans(input_str)

    def __invalid_input(self, c, input_str):
        if len(input_str) == 0 and c == '-':
            return False

        return not c.isdigit()

    def __write_ans(self, input):
        self.lcd.set_cursor(0, 1)
        self.lcd.write(input)

    def __clear_ans(self):
        self.lcd.set_cursor(0, 1)
        self.lcd.write(' ' * 16)
