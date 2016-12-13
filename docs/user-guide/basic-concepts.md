# PyControlGUI

**PyControlGUI** is a *Graphical User Interface (GUI)* for the [PyControl framework](https://bitbucket.org/takam/pycontrol/wiki/Home). It is written in Python3 and built on top of [PyForms](https://github.com/UmSenhorQualquer/pyforms) and [PyControlAPI](https://bitbucket.org/fchampalimaud/pycontrolapi) libraries.

## Interface organization

The GUI is roughly divided in 3 main sections:

* **Project tree**: tree view like to organize project contents
* **Details view**: get detailed info about each component
* **Workspace**: open plugins and consoles to manage and monitorize experiment running


![pyControlGUI frontpage](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/media/showall.png?token=63140b9493bc8d14657b24f55ab6973414e8e99f&rev=d3eb8d19de2ef5755249671d50496cdbfa89b59b)


## GUI entities

PyControlGUI is designed around the following entities relationships: 

* **Project**: top level element that aggregates a set of **Experiments**, **Tasks** and **Experimental setups**
* **Experiment**: aggregates a set of **Subjects** with certain settings
* **Task**: programmed state machine based a set of **States**, **Events** and **Variables**
* **Experimental setup**: hardware configuration of a board, its serial port and a specific **Framework**
* **Subject**: represents the living subject that is being studied, but it is also a confluence of relationships between an **Experiment**, a **Task** and an **Experimental setup (board)**
* **Session**: report generated every time a subject configuration is run on a board

![entities](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/media/pycontrolgui_entities_v1.png?token=dad5c7a07c5d5a1c564a8fd6c0cd4bcb494a05e4&rev=383eaade3b50f3a197aec336da710851887cb913)

### Operations on entities

Operations on entities can be acomplished in one of two ways:

* Selecting option on the top bar menu
* Selecting option when right-clicking entity on the tree

## Basic workflow

PyControlGUI aims at simplicity. The **Subject** entity is the main character on the workflow. Only upon correct subject configuration, a new session can be run. The basic workflow can be described like this:

1. Create **Project**
2. Add **Experiment** and give it a name
3. Add **Task**, give it a name and write code for it
4. Add **Experimental setup**, set serial port, configure and install framework
5. Add **Subject** to **Experiment**, give it a name, assign an **Experimental setup** and a **Task**
6. For each **Subject** configuration, sync **Task** variables and run it

## Board operations

There are several cases where interaction with board (aka experimental setup) takes place. This interaction is always run in parallel, which means that several boards can be configured and monitorized at the same time, without graphical interface gets frozen.

Below, we describe the buttons for the available operations:

* **Install framework**: removes and installs new framework on the board 

![entities](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/media/button_install.png?token=464920fa16883b770b91a6454f5071f9e2e93b5b&rev=7de6977f4443644996949e2c3ca1d40fbd8b4259)

* **Sync task**: uploads task to board and then syncs GUI with board events and states IDs and variables contents

![sync task](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/media/button_sync.png?token=c55a28fc330745c35d35b9b861a5de49a63c64df&rev=7de6977f4443644996949e2c3ca1d40fbd8b4259)


* **Upload and Run task**: uploads task to board and then starts state machine

![run task](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/media/buttons_upload_run.png?token=ba3d1f4c90292c0a9660a33efa27c6c7f76d87a5&rev=7de6977f4443644996949e2c3ca1d40fbd8b4259)

## Menu options

There are 3 sub-menus available on the top bar menu:

* **File**: allows user to create or open project 

![entities](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/media/menu_file.png?token=87f4e5bfa4c2ff936b0cf980907adafe7ece1854&rev=6ffaccfccb197013a0e674e0c543e288f1061efc)

* **Actions**: provides actions that perform operations on entities (ex: add experiment, add setup, import task, etc)

![sync task](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/media/menu_actions.png?token=0b9d4481faccc17ec0b23d976136577cf8f92861&rev=3095dc84a626a27596e04003992070276dfd1906)


* **Window**: operations related to windows opened in the workspace (ex: align windows, close all, etc)

![window](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/media/menu_window_options.png?token=9bd0cf71ddd1cf85391b8c5b8c70c3b2cff782f2&rev=3095dc84a626a27596e04003992070276dfd1906)

## Task programming

Tasks are written in Python3 and follow a state machine design.

Consider a simple example where pyBoard has one poke connected (left poke) and we want to react for poke activation. If poke IR light is interrupted, turn on poke LED, otherwise poke LED is turned off.


The full example is described below:


```
from pyControl.utility import *

# Define states, events and variables.

states = ['mouse_poke_in', 'mouse_poke_out']

events = ['left_poke', 'left_poke_out']

initial_state = 'mouse_poke_out'

v.my_var = 5000

# Define behaviour.

def mouse_poke_out(event):
    if event == 'entry':
        hw.left_poke.LED.off()
    elif event == 'left_poke':
        goto('mouse_poke_in')


def mouse_poke_in(event):
    if event == 'entry':
        hw.left_poke.LED.on()
    if event == 'left_poke_out':
        goto('mouse_poke_out')


def run_end():  # Turn off hardware at end of run.
    hw.left_poke.LED.off()

```

### Task elements

Every task is composed of:

* List of states

`states = ['mouse_poke_in', 'mouse_poke_out']`

* List of events

`events = ['left_poke', 'left_poke_out']`

* Variable to indicate initial state

`initial_state = 'mouse_poke_out'`

* Zero or more auxiliar variables

` v.my_var = 5000 `

* A function for each declared state (this function always receive an event)

```
def mouse_poke_out(event):
    if event == 'entry':
        hw.left_poke.LED.off()
    elif event == 'left_poke':
        goto('mouse_poke_in')


def mouse_poke_in(event):
    if event == 'entry':
        hw.left_poke.LED.on()
    if event == 'left_poke_out':
        goto('mouse_poke_out')
```

* A set of auxiliar functions (optional)

### Framework under the hood

The task is uploaded to board only if a framework is installed. This framework is composed of several modules that support task interpretation. Some of this modules are exposed as an API and are intended to abstract low-level hardware details. This is the case of the **pyControl.utility** and the **pyControl.hardware_description** modules. For a better understanding of the framework please refer to the ***Framework programming*** section below.


## Framework programming

The framework is the piece of code that is installed on the pyBoard before a task is uploaded. It is composed of several modules that support task execution.

There are 4 modules that support core functionality:

* **framework.py**: states, events and variables definition and exposed api
* **state_machine.py**: low-level core functions that define state machine excution
* **hardware.py**: low-level functions that abstract micropython hardware
* **utility.py**: utility functions availble to user when programming tasks


There is 1 module that supports hardware abstraction and exposes high-level components to the task:

* **hardware_description.py**: describes board pin mapping and exposes several concepts to task programming, like Poke, Box, etc.

```
import pyb
from . import framework as fw
from . import hardware as hw
from .hardware import Digital_input
from .hardware import Digital_output
from .hardware import Speaker

# ----------------------------------------------------------------------------------------
# Board pin mapping dictionaries.
# ----------------------------------------------------------------------------------------

# These dictionaries provide pin mappings for specific boards whose schematics are
# provided in the pyControl/schematics folder.

breakout_1_0 = {'ports': {1: {'DIO_A': 'X1',   # RJ45 connector port pin mappings.
                              'DIO_B': 'X2',
                              'POW_A': 'Y4',
                              'POW_B': 'Y8'},

                          2: {'DIO_A': 'X3',
                              'DIO_B': 'X4',
                              'POW_A': 'Y3',
                              'POW_B': 'Y7'},

                          3: {'DIO_A': 'X7',
                              'DIO_B': 'X8',
                              'POW_A': 'Y2',
                              'POW_B': 'Y6'},

                          4: {'DIO_A': 'X12',
                              'DIO_B': 'X11',
                              'POW_A': 'Y1',
                              'POW_B': 'Y5'}},
                'BNC_1': 'Y11',      # BNC connector pins.
                'BNC_2': 'Y12',
                'DAC_1': 'X5',
                'DAC_2': 'X6',
                'button_1': 'X9',    # User pushbuttons.
                'button_2': 'X10'}

# ----------------------------------------------------------------------------------------
# Hardware collections.
# ----------------------------------------------------------------------------------------


class Poke(hw.Hardware_group):

    def __init__(self, port, rising=None, falling=None, rising_B=None,
                 falling_B=None, debounce=5, pull=pyb.Pin.PULL_NONE):

        self.SOL = Digital_output(port['POW_A'])
        self.LED = Digital_output(port['POW_B'])
        self.input_A = Digital_input(port['DIO_A'], rising, falling, debounce, pull)
        self.input_B = Digital_input(port['DIO_B'], rising_B, falling_B, debounce, pull)

        self.all_inputs = [self.input_A, self.input_B]
        self.all_outputs = [self.SOL, self.LED]

    def value(self):
        # Return the state of input A.
        return self.input_A.value()


class Box(hw.Hardware_group):

    def __init__(self):

        # Settings for breakout board 1_0
        ports = breakout_1_0['ports']
        pull = pyb.Pin.PULL_NONE

        # Instantiate components.

        self.debug_led = pyb.LED(1)

        self.left_poke = Poke(ports[1], rising='left_poke', falling='left_poke_out',
                              rising_B='session_startstop', pull=pull)
        self.center_poke = Poke(ports[2], rising='high_poke', falling='high_poke_out',
                                rising_B='low_poke', falling_B='low_poke_out', pull=pull)
        self.right_poke = Poke(ports[3], rising='right_poke', falling='right_poke_out', pull=pull)

        self.houselight = self.center_poke.SOL

        self.opto_stim = Digital_output('X12')

        self.house_red = Digital_output('Y1')

        self.speaker = Speaker(breakout_1_0['DAC_1'])

        self.all_inputs = [self.left_poke, self.center_poke, self.right_poke]
        self.all_outputs = [self.left_poke, self.center_poke, self.right_poke, self.opto_stim,
                            self.house_red]

```