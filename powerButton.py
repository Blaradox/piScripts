from gpiozero import Button
from signal import pause
import os

# Use the Broadcom SOC Pin numbers 
button = Button(21, hold_time=4.0)

# Our functions on what to do when the buttons are pressed
def shutdown():
  os.system('sudo shutdown -h now')
def reboot(): 
  os.system('sudo shutdown -r now')

# Add our functions to execute when the button pressed event happens
button.when_released = shutdown
button.when_held = reboot

# Now wait!
pause()
