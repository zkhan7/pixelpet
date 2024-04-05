from gpiozero import LED

class ledini:
    def __init__(self, red_pin, yellow_pin, green_pin):
        self._red_light = LED(red_pin)
        self._yellow_light = LED(yellow_pin)
        self._green_light = LED(green_pin)
        self._state = "red"

    @property
    def red_led(self):
        return self._red_light

    @property
    def yellow_led(self):
        return self._yellow_light

    @property
    def green_led(self):
        return self._green_light

    def red(self):
        self._red_light.on()
        self._yellow_light.off()
        self._green_light.off()
        self._state = "red"

    def yellow(self):
        self._red_light.off()
        self._yellow_light.on()
        self._green_light.off()
        self._state = "yellow"

    def green(self):
        self._red_light.off()
        self._yellow_light.off()
        self._green_light.on()
        self._state = "green"

    def turn_off(self):
        self._red_light.off()
        self._yellow_light.off()
        self._green_light.off()
