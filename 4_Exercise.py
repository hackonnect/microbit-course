from microbit import *

# Using the knowledge we have learnt so far, try to create a device that can
# show the current temperature or act as a compass depending on which button
# you press on the microbit.

compass.calibrate()
while True:
    sleep(50)
    # Add your code here
display.clear()

# EXTENSION
# Instead of using buttons, allow the user to use gestures to determine whether
# they want to see the current temperature or use the microbit as a compass.

