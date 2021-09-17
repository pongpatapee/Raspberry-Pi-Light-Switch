import RPi.GPIO as GPIO
import time

pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
servo1 = GPIO.PWM(pin, 50)

servo1.start(0)

duty = 2
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.1)
    servo1.ChangeDutyCycle(0)
    time.sleep(0.1)
    duty += 1
    
time.sleep(2)
servo1.ChangeDutyCycle(2)
servo1.stop()
GPIO.cleanup()
print("Goodbye")
