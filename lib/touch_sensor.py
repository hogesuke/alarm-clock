import wiringpi

class TouchSensor:

    def __init__(self):
        self.pin = 36  # GPIO16

        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self.pin, 2)

    def is_touched(self):
        return wiringpi.digitalRead(self.pin) == 1


