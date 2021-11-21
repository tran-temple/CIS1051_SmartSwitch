# Status Report

#### Your name

My name is Cindy H. Tran.

#### Your section leader's name

Cindy H. Tran

#### Project title

The title of my project is Smart Light Switch.

***

Short answers for the below questions suffice. If you want to alter your plan for your project (and obtain approval for the same), be sure to email your section leader directly!

#### What have you done for your project so far?

I have done the following tasks:
  - Set up Raspberry Pi device
  - Researched on the internet and wrote code to turn on/off the light:

		import RPi.GPIO as GPIO
		GPIO.setmode(GPIO.BCM)
		heat_pin = 12
		GPIO.setup(heat_pin, GPIO.OUT)
		GPIO.output(heat_pin, GPIO.HIGH)
		
  - Created a simple WebServer with Flask and deployed it on the Raspberry Pi device. This is my reference resource: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d

#### What have you not done for your project yet?

Currently, my web page only displays "Hello World" to test the system. I will design it with buttons and images to make it more attractive.

#### What problems, if any, have you encountered?

I met one problem with connecting Raspberry via SSH; however, I researched on the internet and found out how to fix it. This is my reference resource: https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html
