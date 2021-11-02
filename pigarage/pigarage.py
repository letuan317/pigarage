import time
from datetime import datetime
from flask import Flask, render_template, request
from termcolor import cprint

import RPi.GPIO as GPIO

# the pin numbers refer to the board connector not the chip
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.HIGH)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Garage', methods=['GET', 'POST'])
def Garage():
    name = request.form['garagecode']
    # 12345678 is the Password that Opens Garage Door (Code if Password is Correct)
    if name == '1011':
        GPIO.output(7, GPIO.LOW)
        time.sleep(1)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(2)
        cprint("[INFO] GarageCode is correct", "green")
        return app.send_static_file('Open.html')
    else:
        cprint("[!] GarageCode is incorrect", "red")
        return app.send_static_file('Question.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
