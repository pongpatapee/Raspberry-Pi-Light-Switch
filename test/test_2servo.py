import RPi.GPIO as GPIO
import time

pin1 = 17
pin2 = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
servo1 = GPIO.PWM(pin1, 50)
servo2 = GPIO.PWM(pin2, 50)

servo1.start(0)
servo2.start(0)

duty = 2
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    servo2.ChangeDutyCycle(duty)
    time.sleep(0.1)
    servo1.ChangeDutyCycle(0)
    servo2.ChangeDutyCycle(0)
    time.sleep(0.1)
    duty += 1
    
time.sleep(2)
servo1.ChangeDutyCycle(12)
servo1.stop()
servo2.ChangeDutyCycle(12)
servo2.stop()
GPIO.cleanup()
print("Goodbye")

