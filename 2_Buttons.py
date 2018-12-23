from microbit import *

# There are two buttons on the microbit, button_a and button_b
# You can use is_pressed() to see if a button is being pressed.
# Remember, when you want to see if both buttons are preseed,
# that has to be the first if statement.

'''
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        break
    elif button_a.is_pressed():
        display.show('A')
    elif button_b.is_pressed():
        display.show('B')
    else:
        display.show(Image.HAPPY)
display.show(Image.SAD)
sleep(2000)
display.clear()
'''

# You can also use get_presses() to see how many times a button is pressed
# while the microbit is asleep

'''
display.scroll('START!')
sleep(5000)
presses = button_a.get_presses() + button_b.get_presses()
display.scroll(str(presses))
'''

# You can also see if the button was pressed while the microbit is asleep using
# was_pressed().

'''
display.show('?')
sleep(1000)
if button_a.was_pressed():
    display.show(Image.HAPPY)
else:
    display.show(Image.SAD)
sleep(1000)
display.clear()
'''