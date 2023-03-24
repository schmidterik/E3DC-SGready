import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
chan_list = (22,23,24,27)
GPIO.output(chan_list, True)
try:
    while(True):
        sleep(1)
        GPIO.output(23, False)
        sleep(1)
        GPIO.output(22, False)
        sleep(1)
        GPIO.output(27, False)
        sleep(1)
        GPIO.output(24, False)
        sleep(1)
        GPIO.output(chan_list, True)
except KeyboardInterrupt:
    GPIO.cleanup()
