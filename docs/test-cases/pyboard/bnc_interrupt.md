# PyBoard test cases - BNC Interrupt

We want to test the response time in reacting to an external trigger. The external triiger will be connected to a BNC port which will call another function that writes 0 or 255 for the DAC port allowing us to see a squared wave on the oscilloscope. Connected to the BNC port is an arbitrary function generator, which also generates a squared wave on a certain frequency we can control. This test will be performed WITH vs WITHOUT using the pycontrol framework. 


## Preparing test

### Requirements
* PyBoard
* 3 Coaxial cables + 1 T connection
* Oscilloscope
* Arbitrary function generator
* Serial software
* PyControlGUI software

### Setup

Connect ports:

* DAC-1 (PyBoard) to Channel 2 (Oscilloscope)
* T Connector (function generator) to Channel 1 (Oscilloscope)
* BNC-1 (PyBoard) to T Connector (function generator)

![pyboard_bnc_dac_ports](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_setup.png)


### A. Run test without framework

* Upload [bnc\_interrupt.py](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt.py) to PyBoard:


```
# bnc_interrupt.py

import pyb
from pyb import Pin
from pyb import ADC
from pyb import delay
from pyb import ExtInt
from pyb import DAC

my_control = True
update = False

def square_wave_output(e):
    global update
    update = True

dac = DAC(Pin('X5'))

ext = ExtInt(Pin('Y11'), ExtInt.IRQ_RISING_FALLING, Pin.PULL_NONE, square_wave_output)  # BNC1

while(True):
    if update:
        update = False
        if my_control:
            dac.write(255)
            my_control = False
        else:
            dac.write(0)
            my_control = True
```


* Load pyboard REPL:

```
# UNIX
screen /dev/tty.usbmodem1462
```

* Import and run bnc_interrupt module

```
import bnc_interrupt
```

### B. Run test with framework

1. Download PyControl example project from [here](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/pycontrolgui_project_time_tests.zip)
2. Install framework "board\_no\_print"

	![install_framework](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/install_framework.png)

3. Upload and run script [bnc\_interrupt\_gui.py](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_gui.py) to PyBoard:

```
# bnc_interrupt_gui.py

from pyControl.utility import *

# States and events.

states = ['WAVE_HIGH', 'WAVE_LOW']

events = ['wave_high', 'wave_low']

initial_state = 'WAVE_HIGH'

# Variables.
        
# Define behaviour.

def WAVE_HIGH(event):
    if event == 'wave_high':
        hw.dac.write(255)
        goto('WAVE_LOW')

def WAVE_LOW(event):
    if event == 'wave_low':
        hw.dac.write(0)
        goto('WAVE_HIGH')

def run_end():  # Turn off hardware at end of run.
    hw.off()
```



### C. Results

#### Frequency @ 1Hz

| zoom in (5us) | zoom in framework (100us) | zoom out (500us) | zoom out framework (500ms) |
| --- | --- | --- | --- | 
| ![bnc_interrupt_1Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_1Hz_zoom_in.png) | ![bnc_interrupt_gui_1Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_gui_1Hz_zoom_in.png) |  ![bnc_interrupt_1Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_1Hz_zoom_out.png) | ![bnc_interrupt_gui_1Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_gui_1Hz_zoom_out.png) |

#### Frequency @ 10Hz

| zoom in (5us) | zoom in framework (100us) | zoom out (50ms) | zoom out framework (50ms) |
| --- | --- | --- | --- | 
| ![bnc_interrupt_1Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_10Hz_zoom_in.png) | ![bnc_interrupt_gui_1Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_gui_10Hz_zoom_in.png) |  ![bnc_interrupt_1Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_10Hz_zoom_out.png) | ![bnc_interrupt_gui_1Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_gui_10Hz_zoom_out.png) |

#### Frequency @ 100Hz

| zoom in (5us) | zoom in framework (100us) | zoom out (5ms) | zoom out framework (5ms) |
| --- | --- | --- | --- | 
| ![bnc_interrupt_1Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_100Hz_zoom_in.png) | ![bnc_interrupt_gui_1Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_gui_100Hz_zoom_in.png) |  ![bnc_interrupt_1Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_100Hz_zoom_out.png) | ![bnc_interrupt_gui_1Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_gui_100Hz_zoom_out.png) |


#### Frequency @ 1KHz

| zoom in (5us) | zoom out (500us) |
| --- | --- | 
| ![bnc_interrupt_1Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_1KHz_zoom_in.png) | ![bnc_interrupt_1KHz_zoom_out](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_1KHz_zoom_out.png) |

#### Frequency @ 10KHz

| zoom in (5us) | zoom out (500us) |
| --- | --- | 
| ![bnc_interrupt_10Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_10KHz_zoom_in.png) | ![bnc_interrupt_1KHz_zoom_out](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_1KHz_zoom_out.png) |


#### Frequency @ 20KHz

| zoom in (5us) | zoom out (25us) |
| --- | --- | 
| ![bnc_interrupt_20Hz_zoom_in](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_20KHz_zoom_in.png) | ![bnc_interrupt_20KHz_zoom_out](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/bnc_interrupt_20KHz_zoom_out.png) |
