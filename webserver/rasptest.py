import RPi.GPIO as GPIO
import time

def get_angle(state):
    state = state.lower()
    if state == 'neutral':
        return 90
    elif state == 'on':
        return 0
    elif state == 'off':
        return 180
    elif state == 'custom':
        angle = int(input("Enter an angle between 0 & 180: "))
        return angle
    else:
        return 90

pin1 = 17
pin2 = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
servo1 = GPIO.PWM(pin1, 50)
servo1.start(0)
GPIO.setup(pin2, GPIO.OUT)
servo2 = GPIO.PWM(pin2, 50)
servo2.start(0)

state = 'neutral'

try:
    while True:
        state = input("Enter state: ")
        angle = get_angle(state)
        servo1.ChangeDutyCycle(2+(angle/18))
        servo2.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        angle = 90
        servo1.ChangeDutyCycle(2+(angle/18))
        servo2.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.3)
        servo1.ChangeDutyCycle(0)
        servo2.ChangeDutyCycle(0)


except KeyboardInterrupt: 
    print("Ending operations")
finally:
    servo1.ChangeDutyCycle(2)
    servo1.stop()
    servo2.ChangeDutyCycle(2)
    servo2.stop()
    GPIO.cleanup()
    print("Goodbye")