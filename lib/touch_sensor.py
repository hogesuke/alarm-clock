import wiringpi

class TouchSensor:

    def __init__(self):
        self.pin = 16

        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self.pin, 0)

    def is_touched(self):
        return wiringpi.digitalRead(self.pin) == 1
