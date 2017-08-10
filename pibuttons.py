#!/bin/python
# Original script by INderpreet Singh
# Modified by Blaradox

import RPi.GPIO as GPIO
import time
import os

# Use the Broadcom SOC Pin numbers 
shtdwn = 21
bltth = 26


# Setup the Pin with Internal pullups enabled and PIN in reading mode. 
GPIO.setmode(GPIO.BCM)
GPIO.setup(shtdwn, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(bltth, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Our functions on what to do when the buttons are pressed
def Shutdown(channel):
	os.system("sudo shutdown -h now")

def Bluetooth(channel):
	os.system("/home/pi/Scripts/bluetooth.sh")

# Add our functions to execute when the button pressed event happens
GPIO.add_event_detect(shtdwn, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)
GPIO.add_event_detect(bltth, GPIO.FALLING, callback = Bluetooth, bouncetime = 2000)

# Now wait!
while 1:
	time.sleep(1)
