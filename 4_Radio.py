from microbit import *
import radio

# First of all, the radio must be turned on in order for the microbit
# to send and receive any messages.

radio.on()

# You can also turn the radio off

radio.off()

# There are ways you can configure the radio. Here are the default settings.

radio.config(length=32, queue=3, channel=7, power=6, address=0x75626974, group=0, data_rate=radio.RATE_M1MBIT)

# The one you will be using the most is setting the channel, this can be any
# number between 0 and 83.

radio.config(channel=68)

# For more information about what each of these settings mean, visit
# https://microbit-micropython.readthedocs.io/en/latest/radio.html
# If you somehow mess up the settings, you can always reseet it:

radio.reset()

# Radios are actually very easy to use. But remember, each message is broadcasted
# to every other microbit out there using the same channel. It's a good idea to use a unique
# channel for you microbits.

# To send messages, simply use radio.send().
# To receive messages, simply use radio.receive().
# Test this program out with a parner, changing the channel your radio is using. 
# Can you figure out what this program does?

radio.config(channel=7)

while True:
    sleep(50)

    if button_a.was_pressed():
        display.show(Image.HAPPY)
        radio.send('A')
    elif button_b.was_pressed():
        display.show(Image.SAD)
        radio.send('B')

    message = radio.receive()

    if message == 'A':
        display.show(Image.HAPPY)

    if message == 'B':
        display.show(Image.SAD)

