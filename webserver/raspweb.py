from flask import Flask, render_template, request, url_for
import datetime
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

#setting up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin1 = 17
pin2 = 27
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
s1 = GPIO.PWM(pin1, 50)
s2 = GPIO.PWM(pin2, 50)
s1.start(0)
s2.start(0)
    

def get_angle(state):
    state = state.lower()
    if state == 'on':
        return 0
    elif state == 'off':
        return 180
    else:
        return 90

@app.route("/", methods=['GET', 'POST'])
def home():
    now = datetime.datetime.now()
    timestr = now.strftime("%d/%m/%Y  %H:%M")
    templateData = {
        'title': 'Raspberry Pi web',
        'time' : timestr
    }

    if request.method == 'POST':
        if request.form['on_btn'] == 'ON':
            try:
                print('Turning lights on')
                angle = 0 
                s1.ChangeDutyCycle(2+(angle/18))
                s2.ChangeDutyCycle(2+(angle/18))
                time.sleep(0.5)
                angle = 90
                s1.ChangeDutyCycle(2+(angle/18))
                s2.ChangeDutyCycle(2+(angle/18))
                time.sleep(0.3)
                s1.ChangeDutyCycle(0)
                s2.ChangeDutyCycle(0)
            except:
                print("There was an error")
        else:
            try:
                print('Turning lights off')
                angle = 180
                s1.ChangeDutyCycle(2+(angle/18))
                s2.ChangeDutyCycle(2+(angle/18))
                time.sleep(0.5)
                angle = 90
                s1.ChangeDutyCycle(2+(angle/18))
                s2.ChangeDutyCycle(2+(angle/18))
                time.sleep(0.3)
                s1.ChangeDutyCycle(0)
                s2.ChangeDutyCycle(0)
            except:
                print("There was an error")
    else:
        return render_template("index.html", **templateData)

    return render_template("index.html", **templateData)


if __name__ == "__main__":
    app.run(debug=True)

    s1.ChangeDutyCycle(2+(90/180))
    s2.ChangeDutyCycle(2+(90/180))
    s1.stop()
    s2.stop()
    GPIO.cleanup()
    print("program ended")
    #192.168.0.138 window's ipv4
    #192.168.0.163 rasp