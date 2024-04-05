import status_led
from time import sleep

# Define GPIO pins for three LEDs
red_pin = 17
green_pin = 27
yellow_pin = 22

# Create Led instance
led_lights = status_led.ledini(red_pin,yellow_pin, green_pin)

def set_led(temp):
    if temp is not None:
        if 20 <= temp <= 50:
            led_lights.green()
            sleep(60)
        elif 0 <= temp <= 10 or 50 <= temp <= 60:
            led_lights.yellow()
            sleep(60)
        else:
            led_lights.red()
            sleep(60)
    else:
        for _ in range(5):  
            led_lights.toggle()
            sleep(1)

    
