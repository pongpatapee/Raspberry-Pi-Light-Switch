import RPi.GPIO as GPIO
import time

pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
servo1 = GPIO.PWM(pin, 50)

servo1.start(0)
state = 'off'
try:
    while True:
        state = input("Enter on, off, or mid: ")
        if state.lower() == 'on':
            angle = 180
        elif state.lower() == 'mid':
            angle = 90
        else:
            angle = 0
        servo1.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
finally:
    servo1.stop()
    GPIO.cleanup()
    print("Goodbye")