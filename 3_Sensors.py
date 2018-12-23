from microbit import *

# It's very easy to get the surrounding temperature using the microbit
# in degrees Celsius using temperature()

'''
display.scroll(str(temperature()))
'''

# You can also measure the time the microbit has been running in
# milliseconds using running_time()

'''
sleep(2000)
display.scroll(str(running_time()))
'''

# As you can see, there is some delay when the microbit runs each function

# The microbit also has an accelerometer built in, allowing you to measure
# the force in milligrams between -+2000. Use accelerometer.get_x(), .get_y()
# and .get_z() (on the 3 different directions). You can also use get_values()
# to get all three values as once as a tuple. After you flash the program into
# the microbit, click on the REPL button. You will be able to see the three
# accelerometer values get printed constantly as you tilt your microbit around.

'''
while not button_a.is_pressed() and not button_b.is_pressed():
    sleep(50)
    print(accelerometer.get_values())
'''

# Microbits can also recognise different gestures using these values.

'''
while not button_a.is_pressed() and not button_b.is_pressed():
    sleep(100)
    print(accelerometer.current_gesture())
'''

# The available gestures are: up, down, left, right, face up, face down, free fall,
# 3g, 6g, 8g, shake
# You can also use accelerometer.is_gesture(gesture_name), accelerometer.was_gesture(gesture_name)
# and accelerometer.get_gestures(), similar to what we did earlier with the buttons.

# Microbits can also act as a compass. The compass measures magnetic field strength
# on the x, y and z axis. We can test it similar to how we tested the accelerometer.

'''
while not button_a.is_pressed() and not button_b.is_pressed():
    sleep(50)
    print(str(compass.get_x()) + ' ' + str(compass.get_y()) + ' ' + str(compass.get_z()))
    print(str(compass.get_field_strength())
'''

# To use these values as a compass however, we need to calibrate the compass first.
# Follow the instructions displayed on the microbit in order to calibrate the compass.
# Use compass.heading() to get the heading of the compass.

'''
compass.calibrate()
display.scroll('DONE!')
while not button_a.is_pressed() and not button_b.is_pressed():
    sleep(100)
    clock = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[clock])
display.clear()
'''

# This program gives you an example of how the compass could be used
# The screen is refreshed every 100ms, or 0.1s.
# Through converting the angle (compass.heading()) to a specific clock hour,
# we can represent the directions through different clocks. Try it out yourself
# and see how it works.