from pyControl.utility import *

# States and events.

states = ['LED_on',
          'LED_off']

events = ['left_poke',
          'left_poke_out']

initial_state = 'LED_off'

# Variables.

v.LED_n  = 1 # Number of LED to use.

# Define behaviour.


def LED_on(event):
    if event == 'entry':
        pyb.LED(v.LED_n).on()
    elif event == 'exit':
        pyb.LED(v.LED_n).off()
    elif event == 'left_poke':
        goto('LED_off')


def LED_off(event):
    if event == 'left_poke_out':
        goto('LED_on')


def run_end():  # Turn off hardware at end of run.
    hw.LED.off()
