# The speech module is not in the microbit library.
# We have to import it separately
import speech
from microbit import *

# Use say in order to make your micro:bit say things.
'''
speech.say('Hackonnect is the best.')
sleep(1000)
speech.say('I agree.')
sleep(1000)
'''

# Of course, in order to make sounds that cannot be described by words, we need another method.
# For this, we can use phenomes with the pronounce() function.
'''
speech.pronounce('/HEH5EH4EH3EH2EH2EH3EH4EH5EHLP')

# You can also use translate in order to translate English into Phenomes
speech.pronounce(translate('Aww, I\'m so sorry!'))
sleep(1000)

# We can also use different pitches with sing.
sing('#115DOWWWW')
'''

# Of course, this is a really hard way to play music.
# We can use the music module to play music.
from music import *

# Here is how musical notes work with the microbit:
# NOTE + OCTAVE : DURATION
# a4:2 means A played on the octave for 2 ticks.

speech.say('Hi!')
music.play('g')
sleep(1000)

# You can set the tempo using this:

music.set_tempo(ticks = 4, bpm = 120)

# To play music, you can play a list of notes:

music.play(['e3:2', 'd3:2', 'c3:2', 'd3:2', 'e3:2', 'e3:2', 'e3:4', 'd3:2', 'd3:2', 'd3:4', 'e3:2', 'e3:2', 'e3:4', 'e3:2', 'd3:2', 'c3:2', 'd3:2', 'e3:2', 'e3:2', 'e3:2', 'e3:2', 'd3:2', 'd3:2', 'e3:2', 'd3:2', 'c3:4'])
sleep(1000)
# Stop all music that is playing
stop()

# Feel free to play around with the audio for a while.