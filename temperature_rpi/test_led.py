import status_led
from time import sleep

# Define GPIO pins for three LEDs
red_pin = 17
green_pin = 27
yellow_pin = 22

# Create Led instance
led_lights = status_led.ledini(red_pin, yellow_pin, green_pin)

led_lights.red()
sleep(10)
led_lights.yellow()
sleep(10)
led_lights.green()
sleep(10)

