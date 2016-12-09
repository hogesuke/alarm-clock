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

    def __init_status(self):
        self.is_completed = False
        self.force_completed = False

    def start(self):
        self.__init_status()

        for i in range(1, self.q_count + 1):
            if self.force_completed:
                break

            self.__question(i)

        self.is_completed = True
        self.__write_goodmorning()

    def has_completed(self):
        return self.is_completed

    def terminate(self):
        self.force_completed = True

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

            if self.force_completed:
                break

            c = chr(scr.getch())

            # 入力をクリア
            if c == 'c':
                input_str = ''
                self.__clear_ans()
                continue  # clear

            # 問題をスキップ
            if c == 's':
                break

            # 不正な入力を無視
            if self.__invalid_input(c, input_str):
                continue

            input_str += c

            # 正解
            if input_str == ans_str:
                self.__write_ans(input_str + ' GOOD!')
                sleep(0.7)
                break

            # 不正解
            if len(input_str) == len(ans_str):
                self.__write_ans(input_str + ' NG')
                sleep(0.7)
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

    def __write_goodmorning(self):
        self.lcd.clear()
        self.lcd.set_cursor(0, 0)
        self.lcd.write('Good morning!')
        sleep(2)
        self.lcd.clear()

