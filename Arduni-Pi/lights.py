# There are pre requirements to be followed before getting into it
from gpiozero import LED
from time import sleep
from .cars import count_cars

red = LED(22)
yellow = LED(17)
green = LED(20)

while True:
    red.on()
    sleep(5)
    yellow.on()
    sleep(5)
    green.on()
    sleep(5)
    red.off()
    sleep(5)
    yellow.off()
    sleep(5)
    green.off()
    sleep(5)