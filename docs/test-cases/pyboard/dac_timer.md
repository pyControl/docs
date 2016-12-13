# PyBoard test cases - DAC timer

We want to test the response time when using the micropython timer function. This test will be performed WITH vs WITHOUT using the pycontrol framework. The timer function will trigger another function that writes 0 or 255 for the DAC port allowing us to see a squared wave on the oscilloscope. We want to see a squared wave with wavelength of 50Hz (=20ms). This means that our HIGH and LOW signals will be triggered at 100Hz (=10ms).

## Preparing test 

### Requirements
* PyBoard
* Coaxial cable
* Oscilloscope
* Serial software
* PyControlGUI software

### Setup

Connect ports:

* DAC-1 (PyBoard) to Channel 1 (Oscilloscope)

![pyboard_dac_port](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/pyboard_dac_port.jpg?rev=350fb980445ddb4e183f4f5a763d54fef21e6b8a)

### A. Run test without framework

* Upload script [timer_dac.py](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac.py) to pyboard:

```
# timer_dac.py

import pyb
from pyb import Pin
from pyb import ADC
from pyb import delay
from pyb import ExtInt
from pyb import DAC
from pyb import Timer

my_control = True
update = False


def square_wave_output(e):
    global update
    update = True

dac = DAC(Pin('X5'))

tim = Timer(4) # create a timer object using timer 4
tim.init(freq=100) # trigger at 100Hz
tim.callback(square_wave_output)

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

* Import and run dac_timer.py module

```
import timer_dac
```


### B. Run test with framework

1. Download PyControl example project from [here](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/pycontrolgui_project_time_tests.zip)
2. Install framework "board\_no\_print"

	![install_framework](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/bnc_interrupt/install_framework.png)

3. Upload and run script [timer_dac.py](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac_gui.py) to PyBoard:

```
# timer_dac_gui.py

from pyControl.utility import *

# States and events.

states = ['square_high', 'square_low']

events = ['timer_evt']

initial_state = 'square_high'

# Variables.

v.period_on = 10  # Period of blinking when on (in ms) (=100Hz)
v.period_off = 10  # Period of blinking when off (in ms) (=100Hz)

# Define behaviour.


def square_high(event):
    if event == 'entry':
	hw.dac.write(255)
        set_timer('timer_evt', v.period_on)
    elif event == 'timer_evt':
        goto('square_low')


def square_low(event):
    if event == 'entry':
        hw.dac.write(0)
        set_timer('timer_evt', v.period_off)
    elif event == 'timer_evt':
        goto('square_high')
```

* Load pyboard REPL:

```
# UNIX
screen /dev/tty.usbmodem1462
```

* Import and run dac_loop.py script

```
import timer_dac
```

### C. Results - Without framework *vs* framework (verbose) *vs* framework (silent)

#### 10us zoom @ 50 Hz


| without framework | framework (verbose) | framework (silent)
| --- | --- | --- |
| ![timer_dac_10us](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac_10us.png) | ![timer_dac_gui_10us](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac_gui_10us.png) | ![timer_dac_gui_10us_no_print](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac_gui_10us_no_print.png) |

#### 2.5ms zoom  @ 50 Hz

| without framework | framework (verbose) | framework (silent)
| --- | --- | --- |
|  ![timer_dac_2.5ms](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac_2.5ms.png) | ![timer_dac_gui_2.5ms](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac_gui_2.5ms.png) | ![timer_dac_gui_2.5ms_no_print](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac_gui_2.5ms_no_print.png) |

#### 5ms zoom @ 50 Hz

| without framework | framework (verbose) | framework (silent)
| --- | --- | --- |
| ![timer_dac_5ms](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac_5ms.png) |![timer_dac_gui_5ms](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac_gui_5ms.png) | ![timer_dac_gui_5ms_no_print](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac_gui_5ms_no_print.png) |

#### 10ms zoom @ 50 Hz

| without framework | framework (verbose) | framework (silent)
| --- | --- | --- |
| ![timer_dac_10ms](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac_10ms.png) | ![timer_dac_gui_10ms](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac_gui_10ms.png) |  ![timer_dac_gui_10ms_no_print](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/pyboard_timing/timer_dac/timer_dac_gui_10ms_no_print.png) |

