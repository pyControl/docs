# Hardware

## Overview

A typical pyControl hardware setup consists of one or more breakout boards connected to a computer by USB each of which runs a single behavioural setup.  The breakout board connects a set of devices such as nosepokes, audio boards or LED drivers which make up behavioural setup.

![Hardware overview](../media/hardware/hardware-overview.jpg)

## Specifying hardware

Although it is possible to instantiate hardware objects directly in a state machine definition file (as in the [button](https://bitbucket.org/takam/pycontrol/src/default/tasks/button.py) example), the recomended way of specifying hardware is to create a *hardware definition* file which is imported by the state machine.  The rationale for this is twofold: Firstly, the same hardware setup is  typically used for many different tasks so seperating out the hardware definition and task definition into seperate files avoids repeating hardware definition code in each task file.  Secondly, the same task may be used on different setups without modifying the task code as long as the required hardware devices are 
specified in the setups hardware definitions.

The hardware definition tells the pyControl system what inputs and outputs are available for use by state machines.  A simple hardware definition file might read:


```python
from devices import *   

button = Digital_input(pin='X1', rising_event='button_press')
LED    = Digital_output(pin='X2')
```

This specifies that there is a digital input called `button` connected to pin X1 on the pyboard, and a digital output called `LED` connected to pin X2.  Each time a rising edge occurs on pin X1, a framework event named `'button_press'` will be generated, you can also specify events to be generated when falling edges occur on digital inputs:


```python
button = Digital_input(pin='X1', rising_event='button_press', falling_event='button_release')
```

By convention the hardware definition file is imported into state machine definitions with:

```python
import hardware_definition as hw
```

such that hardware objects are accessed as in the examples below:


```python
hw.button.value() # Read the state of the button.

hw.LED.on()      # Turn the LED on

hw.LED.off()     # Turn the LED off
```

You can turn off all outputs (for example at the end of a session) using the command:


```python
hw.off()  # Turn off all outputs.
```

### Boards, ports and devices

Typically when pyControl is used to run a behavioural experiment, the micropython board is mounted on a breakout board which provides a set of ports which behavioural hardware like nose pokes or levers are connected to.  

Each port provides power (GND, 5V and 12V), two general purpose digital input/output (DIO) lines, and two driver lines which can be used for switching higher power loads such as solenoids or LEDs.  pyControl hardware uses RJ45 network cables for connecting hardware devices to the breakout board as they are cheap, readily available and easy to use. 

Rather than having to specify each input and output on a hardware device seperately; for example the IR beam, stimulus LED and solenoid on a nose poke, each device has its own Python class which defines its the inputs and outputs, allowing it to be instantiated and connected with a single command.  For example the hardware definition below specifies that 3 nose pokes are plugged into ports 1-3 of pyControl Breakout board 1.0.

```python
from devices import *

board = Breakout_1_0()  # Instantiate the breakout board object.

# Instantiate the poke objects.
left_poke   = Poke(port=board.port_1, rising_event='left_poke'  , falling_event='left_poke_out' )
centre_poke = Poke(port=board.port_2, rising_event='centre_poke', falling_event='centre_poke_out')
right_poke  = Poke(port=board.port_3, rising_event='right_poke' , falling_event='right_poke_out')
```

The `Breakout_1_0` class knows which pin on the micropython maps to which line on which port of the breakout board.  The `Poke` class recieves one of the breakout boards ports as an argument when it is instantiated so it knows which pins correspond to the IR beam, LED and solenoid.  When a Poke object is instantiated, it creates a digital input which will generate the specified rising and falling events when the pokes IR beam is broken, and two digital outpus corresponding to the LED and solenoid.  These can be controlled from within a state machine definition as:


```python
hw.left_poke.LED.on() # Turn on the LED on the left poke.

hw.right_poke.SOL.off() # Turn off the solenoid on the right poke.
```

## Hardware class reference

### Hardware primatives

These classes control the behaviour of a single pin on the micropython.  See also the micropython [pyb](https://docs.micropython.org/en/latest/pyboard/library/pyb.html) module.

---

**Digital input**

The digital input class generates pyControl framework events when a specified pin on the Micropython board changes state. Seperate events can be specified for rising and falling edges. 

By defalt debouncing is used to prevent multiple events being triggered very close together in time if the edges are not clean.  The debouncing method used ensures that transient inputs shorter than the debounce duration still generate rising and faling edges.  Debouncing incurs some overheads so should be turned off for inputs with clean edges and high event rates.

Setting the decimate argument to an integer N causes only every N'th input pulse to generate an event.  Input pulses that are ignored due to decimation incur minimal overheads.  Decimation is designed for inputs like camera sync pulses where the input occurs at a high rate and recording 1 out of every N pulses is sufficent. Decimate can be used only with debouncing off and an event specified for a single edge.  

```python
class Digital_input(pin, rising_event=None, falling_event=None, debounce=5, decimate=False, pull=None)
```

*Arguments:*

`pin` Micropython pin to use

`rising_event` Name of event triggered on rising edges.

`falling_event` Name of event triggered on falling edges.

`debounce` Minimum time interval between events (ms), set to False to deactive debouncing.

`decimate` Set to N to only generate 1 event for every N input pulses.

`pull` Set to `'up'` or `'down'` to enable internal pullup or pulldown resistor.

*Methods:*

`Digital_input.value()`  Get the current state of the input, returns True if pin is high, False if low.

---

**Digital output**

The digital output class is used to control a pyboard pin used as a digital output.

```python
class Digital_output(pin, inverted=False, pulse_enabled=False)
```

*Arguments:*

`pin` Micropython pin to use.

`inverted` If `True`, the pin voltage is set high when the input is turned off and low when turned on.

`pulse_enabled` Set to `True` to enable squarewave pulsed output using the `pulse` method.  Pulsed output uses one of the pyboard hardware timers and as there are a limited number of these pulsed output is by default disabled.

*Methods:*

`Digital_output.on()` Turn on output.

`Digital_output.off()` Turn off output.

`Digital_output.toggle()` Toggle output.

`Digital_output.pulse(freq)` Turn on squarewave output with specified frequency.

`Digital_output.enable_pulse()` Setup output to support pulsed output.

---

### Breakout boards

Breakout boards interface the micropython board with RJ45 behaviour ports, BNC connectors, indicator LEDs and user pushbuttons.  The breakout board classes specify the pin mappings for the boards.

---

**Breakout 1.2** 

Breakout board with 6 RJ45 behaviour ports, 4 BNC connectors, indicator LEDs and user pushbutton. 

[Schematic (pdf)](../media/hardware/breakout-1-2-sch.pdf) 

**Front:**
![Breakout 1.2 front](../media/hardware/breakout-1-2-front.jpg)
**Back:**
![Breakout 1.2 back](../media/hardware/breakout-1-2-back.jpg)

```python
class Breakout_1_2()
```

*Atributes:*

`Breakout_1_2.port_1`, ... , `Breakout_1_2.port_6`  

`Breakout_1_2.BNC_1`, `Breakout_1_2.BNC_2`

`Breakout_1_2.DAC_1`, `Breakout_1_2.DAC_2`

`Breakout_1_2.button`

*Example usage:*

```python
# Instantiate breakout board object.
board = Breakout_1_2()

# Instantiate poke connected to port 1.
left_poke = Poke(port=board.port_1, rising_event='left_poke') 

# Instantiate digital output connected to BNC_1.
BNC_output = Digital_output(pin=board.BNC_1) 

# Instantiate digital input connected to BNC_2.
BNC_input  = Digital_input(pin=board.BNC_2, rising_event='BNC_input') 

# Instantiate pushbutton input, need to enable pullup resistor to use pushbutton.
pushbutton = Digital_input(pin=board.button, falling_event='button', pull='up') 
``` 

---

**Breakout 1.0**

Breakout board with 4 RJ45 behaviour ports, 4 BNC connectors, indicator LEDs and two user pushbuttons.

[Schematic (pdf)](../media/hardware/breakout-1-0-sch.pdf) 

```python
class Breakout_1_0()
```

*Atributes:*

`Breakout_1_2.port_1`, ... , `Breakout_1_2.port_4`  

`Breakout_1_2.BNC_1`, `Breakout_1_2.BNC_2`

`Breakout_1_2.DAC_1`, `Breakout_1_2.DAC_2`

`Breakout_1_2.button_1` , `Breakout_1_2.button_1`

---

### Devices

Devices connect to RJ45 behaviour ports and are used in behavioural setups.

---


**Poke**

Nosepoke port with infra-red beam, stimulus LED and socket to connect solenoid valve.

[Schematic (pdf)](../media/hardware/poke-2-3-sch.pdf) 

|**Front**|**Side**|
|---|---|
|![Poke front](../media/hardware/poke-front.jpg)|![Poke side](../media/hardware/poke-side.jpg)

```python
class Poke(port, rising_event=None, falling_event=None, debounce=5)
```

*Arguments:*

`rising_event` Name of event triggered on IR beam break.

`falling_event` Name of event triggered on IR beam make.

`debounce` Minimum time interval between events (ms), set to False to deactive debouncing.

*Attributes:*

`Poke.LED` Stimulus LED

`POKE.SOL` Solenoid output.

*Methods:*

`Poke.value()` Returns `True` is beam is broken, `False` otherwise.

*Example usage:*

```python

# Instantiate poke object and specify event names.
left_poke = Poke(port=board.port_1, rising_event='left_poke', 'left_poke_out') 

left_poke.LED.on() # Turn on the stimulus LED.

left_poke.SOL.off() # Turn off the solenoid.
```

---

**Audio board**

Audio amplifier board for driving speaker using micropython [DAC](https://docs.micropython.org/en/latest/pyboard/library/pyb.DAC.html) for stimulus generation.  The audio board must be plugged into a port which supports DAC output and I2C serial communication (used to set the volume) - ports 3 and 4 on breakout board 1.2 support the audio board.

[Schematic (pdf)](../media/hardware/audio-board-1-0-sch.pdf) 

![Audio board](../media/hardware/audio-board.jpg)

```python 
class Audio_board(port)
```

*Methods:*

`Audio_board.set_volume(V)` Set volume of audio output, range 0 - 127.

`Audio_board.off()` Turn off audio output.

`Audio_board.sine(freq)` Play a sine wave at the specified frequency.

`Audio_board.square(freq)` Play a square wave at the specified frequency.

`Audio_board.noise(freq=10000)` Play white(ish) noise with specified maximum frequency.

`Audio_board.click()` Play a single click.

`Audio_board.clicks(rate)` Play clicks at specified rate.

`Audio_board.pulsed_sine(freq, pulse_rate)` 

Play a sine wave of the specified frequency pulsed with a 50% duty cycle at the specified rate.

`Audio_board.pulsed_square(freq, pulse_rate)`

Play a square wave of the specified frequency pulsed with a 50% duty cycle at the specified rate.

`Audio_board.pulsed_noise(freq, pulse_rate)` 

Play white(ish) noise with specified maximum frequency pulsed with a 50% duty cycle at the specified rate.

`Audio_board.stepped_sine(start_freq, end_freq, n_steps, step_rate)`

Play a series of sine waves whose frequency is stepped from `start_freq` to `end_freq` in `n_steps` steps at the specifed step rate.

`Audio_board.stepped_square(start_freq, end_freq, n_steps, step_rate)`

Play a series of square waves whose frequency is stepped from `start_freq` to `end_freq` in `n_steps` steps at the specifed step rate.

`Audio_board.play_wav(self, file_name, gc_collect=True)`

Play audio from specified .wav file.  File must be a mono 8 bit wav.  RAM limitations mean that only short .wav files can be played.
By default a garbage collection is performed after playing the file to free up the memory used to load it, this can be disabled by setting the 
gc_collect argument to False. 

*Example usage:*

```python
speaker = Audio_board(board.port_3) # Instantiate audio board.

speaker.sine(5000) # Play a 5KHz sine wave.

speaker.noise() # Turn on white noise.

speaker.off() # Turn off sound output.
```

---

**LED driver**

A constant current LED driver for optogenetic stimulation.

[Schematic (pdf)](../media/hardware/LED-driver-1-1-sch.pdf) 

![LED driver](../media/hardware/LED-driver.jpg)

```python 
class LED_driver(port)
```

*Methods:*

`LED_driver.on()` Turn on LED

`LED_driver.off()` Turn off LED