import webiopi

from liquidcrystal import LiquidCrystal

lcd = LiquidCrystal(7, 8, 25, 24, 23, 18)

lcd.clear()
lcd.set_cursor(0, 0)
lcd.write("Hello World!")

counter = 1
while 1:
    lcd.set_cursor(0, 1)
    lcd.write(str(counter))
    counter += 1
    webiopi.sleep(1.0)
