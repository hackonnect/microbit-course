from microbit import *

# display.scroll() allows you to display a string that is scrolled across the LED display

'''
display.scroll('I <3 Hackonnect!')
'''

# display.show() allows you to display prebuilt or custom images
# display.clear() clears the display

'''
display.show(Image.HEART)
sleep(2000)
display.show(Image.SILLY)
sleep(2000)
display.show(Image.RABBIT)
sleep(2000)
display.clear()
'''

# In Mu, when you finish typing Image., there should be a dropdown menu that displays all the
# prebuilt images you can use.

# To make custom images, simply make a grid like the one shown below. The numbers 0-9 indicate
# the brightness of the LED, with 9 being the brightest and 0 being completely dark.

'''
square = Image('99999:'
               '95559:'
               '95059:'
               '95559:'
               '99999')
               
square = Image('99999:95559:95059:95559:99999')

# Both methods work, as long as the colon separates each row

display.show(square)
sleep(2000)
display.clear()
'''

# Displays do not have to be static. You can have animations too! To do this, simply use a list
# of images as the argument for display.show(). This animation can be looped and have a delay
# set for them.

'''
large_square = Image('99999:90009:90009:90009:99999')
medium_square = Image('00000:09990:09090:09990:00000')
small_square = Image('00000:00000:00900:00000:00000')

square_list = [large_square, medium_square, small_square]

display.show(square_list, loop=False, delay=1000)
display.clear()
'''