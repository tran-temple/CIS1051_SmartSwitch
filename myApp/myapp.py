'''
   ***** Works Cited *****
   This is the link of resource and the app that I learnt to do my Final Project (The smart light control).
   https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
   For my app, I only do one led light control.
'''

'''
	Raspberry Pi - Smart LED Light Control
'''
import RPi.GPIO as GPIO
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
# disable warnings
GPIO.setwarnings(False)

# define pin number
ledPin = 12
# initialize GPIO status variables
ledLightSts = 0

# define led pin as output
GPIO.setup(ledPin, GPIO.OUT) 
# turn led light OFF
GPIO.output(ledPin, GPIO.LOW)
	
@app.route("/")
def index():
        # read GPIO Status
	ledLightSts = GPIO.input(ledPin)
	templateData = {
                'ledLight' : ledLightSts,
        }
	return render_template('index.html', **templateData)
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):	
	if deviceName == 'ledLight':
		actuator = ledPin
   
	if action == "on":
		GPIO.output(actuator, GPIO.HIGH)
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)
		     	
	ledLightSts = GPIO.input(ledPin)
   
	templateData = {
                'ledLight' : ledLightSts,
	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
