import RPi.GPIO as GPIO
import time

pin1 = 17
pin2 = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
servo1 = GPIO.PWM(pin1, 50)
servo1.start(0)
GPIO.setup(pin2, GPIO.OUT)
servo2 = GPIO.PWM(pin2, 50)
servo2.start(0)

try:
    while True:
        angle = float(input("Enter angle between 0 & 180: "))
        servo1.ChangeDutyCycle(2+(angle/18))
        servo2.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
        servo2.ChangeDutyCycle(0)


except KeyboardInterrupt: 
    servo1.ChangeDutyCycle(2)
    servo2.ChangeDutyCycle(2)
    print("bruh")
finally:
    servo1.ChangeDutyCycle(2)
    servo1.stop()
    servo2.ChangeDutyCycle(2)
    servo2.stop()
    GPIO.cleanup()
    print("Goodbye")