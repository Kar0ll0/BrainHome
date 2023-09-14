from phue import Bridge
import time
import os
import random
import pystray
import PIL.Image
#checking system for clear cmd
if os.name in ('nt', 'dos'):
    command = 'cls'
else:
    command = 'clear'
#===
def clearcmd():
    os.system(command)

image = PIL.Image.open('ananas_logo_temp.jpg') #error with opening add whole dict

def turn_on_all_back(icon, item):
    for l in lights:
        l.on = True
def turn_off_all_back(icon, item):
    for l in lights:
        l.on = False
def party_mode_back(icon, item):
    print('PARTY MODEE!')
    i=0
    for light in lights_list:
        while i != 15:
            light.hue = random.randint(0, 20000)
            time.sleep(0.5)
            i = i + 1
def blink_mode(icon, item):
    for l in lights:
        l.on = True
        l.brightness = 20
        time.sleep(0.5)
        l.brightness = 254

    
def exit_background(icon, item):
    icon.stop()

def on_clicked(icon, item):
    print('button works')

icon = pystray.Icon('BrainHomeHue', image, menu=pystray.Menu(
    pystray.MenuItem('Turn on ALL', turn_on_all_back),
    pystray.MenuItem('Turn off ALL', turn_off_all_back),
    pystray.MenuItem('Party mode!', party_mode_back),
    pystray.MenuItem('Blink', blink_mode),
    pystray.MenuItem('Exit', exit_background)
))


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


def turn_on_all():
    for l in lights:
        l.on = True
def turn_off_all():
    for l in lights:
        l.on = False
def party_mode():
    print('PARTY MODEE!')
    i=0
    for light in lights_list:
        while i != 15:
            light.hue = random.randint(0, 20000)
            time.sleep(0.5)
            i = i + 1

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
    print('7-Create group')
    print('8-List of groups')
    print('9-Party mode')
    print('0-Turn off program(and add it to taskbar)')
    #koniec menu
    menu_dec = int(input('Write number from menu here:'))
    if menu_dec == 1:
        turn_off_all()
        clearcmd()
    elif menu_dec == 2:
        turn_on_all()
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
        namegroup = input('Input name of the group:')
        print(light_names)
        idlights = input('Input id of lights:')
        b.create_group(namegroup, [idlights])
    elif menu_dec == 8:
        b.get_group(1, 'name')
        time.sleep(5)
    elif menu_dec == 9:
        party_mode()
        clearcmd()
    elif menu_dec == 0:
        break
    elif menu_dec == 99: #testing colors
        colorhuenum = int(input(':'))
        light_names['Led'].hue = colorhuenum
        time.sleep(10)
clearcmd()
icon.run()
startup()
clearcmd()