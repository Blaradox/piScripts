#!/bin/python
# Original script by INderpreet Singh
# Modified by Blaradox

import RPi.GPIO as GPIO
import time
import os

# Use the Broadcom SOC Pin numbers 
button = 21

# Setup the Pin with Internal pullups enabled and PIN in reading mode. 
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Our functions on what to do when the buttons are pressed
def shutdown(channel):
	os.system("sudo shutdown -h now")
def reboot(): 
	os.system("sudo shutdown -r now")

# Add our functions to execute when the button pressed event happens
GPIO.add_event_detect(button, GPIO.FALLING, callback = shutdown, bouncetime = 2000)

# Now wait!
while 1:
	time.sleep(1)
