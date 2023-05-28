from phue import Bridge
import time
import os
import random
#checking system for clear cmd
from turtle import *
if os.name in ('nt', 'dos'):
    command = 'cls'
else:
    command = 'clear'
#===
def clearcmd():
    os.system(command)




b = Bridge('192.168.0.103')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()


# Prints if light 1 is on or not

# Get a dictionary with the light id as the key

lights_list = b.get_light_objects('list')
light_names = b.get_light_objects('name')
lights = b.lights

light_names['Led'].on = True
time.sleep(1)
for l in lights:
    print(l.name)
#startup seq
def startup():
    for l in lights:
        l.brightness = 20
        time.sleep(0.5)
        l.brightness = 254



startup()


while True:
    clearcmd()
    print('MENU')
    print('1-Turn off all lights')
    print('2-Turn on all lights')
    print('3-Turn off chosen light')
    print('4-Turn on chosen light')
    print('5-Set brightness to chosen light')
    print('6-Set brightness of all lights')
    print('7-Party mode')
    print('0-Turn off program')
    #koniec menu
    menu_dec = int(input('Write number from menu here:'))
    if menu_dec == 1:
        for l in lights:
            l.on = False
        clearcmd()
    elif menu_dec == 2:
        for l in lights:
            l.on = True
        clearcmd()
    elif menu_dec == 3:
        print(light_names)
        namebulb_off = input('Name of the bulb/led:')
        for l in lights:
            light_names[namebulb_off].on = False
        clearcmd()
    elif menu_dec == 4:
        print(light_names)
        namebulb_on = input('Name of the bulb/led:')
        for l in lights:
            light_names[namebulb_on].on = True
        clearcmd()
    elif menu_dec == 5:
        print(light_names)
        namebulb_brightness = input('Name of the bulb/led:')
        valuebrightness = int(input('Brightness(0-254):'))
        for l in lights:
            light_names[namebulb_brightness].brightness = valuebrightness
    elif menu_dec == 6:
        valuebrightness = int(input('Brightness(0-254):'))
        for l in lights:
            l.brightness = valuebrightness
    elif menu_dec == 7:
        print('PARTY MODEE!')
        i=0
        for light in lights_list:
            while i != 15:
                light.hue = random.randint(0, 20000)
                time.sleep(1)
                i = i + 1
        clearcmd()
    elif menu_dec == 0:
        break
    elif menu_dec == 99: #testing colors
        colorhuenum = int(input(':'))
        light_names['Led'].hue = colorhuenum
        time.sleep(10)
startup()
clearcmd()