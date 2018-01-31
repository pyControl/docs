# Hardware

## Overview

A typical pyControl hardware setup consists of one or more breakout boards connected to a computer by USB, each of which runs a single behavioural setup.  The breakout board connects to a set of devices such as nosepokes, audio boards and LED drivers which make up the setup.  

All pyControl hardware is open source and design files for the hardware detailed below are available in the [pyControl hardware repository](https://bitbucket.org/takam/pycontrol_hardware).

![Hardware overview](../media/hardware/hardware-overview.jpg)

## Hardware definitions

Hardware objects can be instantiated directly in a state machine definition file (as in the [button](https://bitbucket.org/takam/pycontrol/src/default/tasks/button.py) example), however the recomended way of specifying hardware is to create a *hardware definition* file which is imported by the state machine.  The rationale for this is twofold: Firstly, the same hardware setup is  typically used for many different tasks so seperating out the hardware and task definition code into seperate files avoids repeating the hardware definition in each task file.  Secondly, the same task may be used on different setups without modifying the task code as long as the required hardware devices are specified in the setups hardware definitions.

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

such that hardware objects are accessed in the state machine definition as in the examples below:


```python
hw.button.value() # Read the state of the button.

hw.LED.on()      # Turn the LED on

hw.LED.off()     # Turn the LED off
```

You can turn off all outputs (for example at the end of a session) using the command:


```python
hw.off()  # Turn off all outputs.
```

### Behaviour ports

Typically when pyControl is used to run a behavioural experiment, the micropython board is mounted on a [breakout board](#breakout-boards) which provides a set of *behaviour ports* which hardware like nose pokes or levers are connected to.  

Each port is an 8 pin RJ45 connector which provides power (GND, 5V and 12V), two general purpose digital input/output (DIO) lines, and two driver lines which can be used for switching higher power loads such as solenoids or LEDs. pyControl hardware uses standard network cables for connecting hardware devices to the breakout board as they are cheap, readily available and reliable.

The DIO lines connect directly to pins on the micropython microcontroller. The microcontroller uses 3.3V logic so when these pins are used as outputs they switch from 0 to 3.3V in the off and on states respectively. The DIO lines are 5V tolerant and can recieve 5V logic signals as inputs.  

The driver lines are low side drivers ([datasheet](https://toshiba.semicon-storage.com/info/docget.jsp?did=29893)) which connect the negative side of the load to ground when turned on:

![Driver diagram](../media/hardware/driver-diagram.jpg)

The positive side of the load can be connected to any voltage up to 12V.  Each driver line can sink up to 150mA of current. Putting more current through the driver lines can damage the driver IC, and in extreme cases could pose a fire risk.  The driver ICs are mounted in sockets and can be easily replaced if damaged.

Some ports have additional functionality such as an extra driver line, digital to analog (DAC), analog to digital (ADC) or serial communication (I2C/UART).

Typically devices which plug into a behaviour port have several inputs and outputs, for example the [poke](#poke) device comprises an IR beam, stimulus LED and solenoid output. Rather than having to specify each input and output on a hardware device seperately, each device has its own Python class, allowing it to be instantiated with a single command.  For example the hardware definition below specifies that 3 nose pokes are plugged into ports 1-3 of pyControl Breakout board 1.2.

```python
from devices import *

board = Breakout_1_2()  # Instantiate the breakout board object.

# Instantiate the poke objects.
left_poke   = Poke(port=board.port_1, rising_event='left_poke'  , falling_event='left_poke_out' )
centre_poke = Poke(port=board.port_2, rising_event='centre_poke', falling_event='centre_poke_out')
right_poke  = Poke(port=board.port_3, rising_event='right_poke' , falling_event='right_poke_out')
```

When a Poke object is instantiated, it creates a digital input which will generate the specified rising and falling events when the pokes IR beam is broken, and two digital outpts corresponding to the LED and solenoid.  These can be controlled from within a state machine definition as:


```python
hw.left_poke.LED.on() # Turn on the LED on the left poke.

hw.right_poke.SOL.off() # Turn off the solenoid on the right poke.
```

# Hardware classes

The following sections detail the Python classes used to specify and control pyControl hardware.

## Inputs and outputs

These classes control the behaviour of a single pin on the micropython.

---

### Digital input

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

### Analog input

The analog input class measures the voltage on a pin at a specified sampling rate, can stream these measurements to the host computer to be saved to disk, and can generate pyControl framework events when the voltage rises above or falls below a specified threshold.  

The input voltage is measured with 12 bit resolution giving a number between 0 and 4095, corresponding to the voltage range 0 to 3.3V relative to the pyboard ground.

Note; acquiring analog data and streaming it to the host computer uses pyboard processor and communication resources so attempting to acquire at too high sampling rates or from too many inputs simultaneously will overload the board. The maximum achievable sample rates have not been extensively tested, though two analog inputs aquiring at 1KHz each appears to work OK.


```python
class Analog_input(pin, name, sampling_rate, threshold=None, rising_event=None, falling_event=None)
```

*Arguments:*

`pin` Micropython pin to use. Only a subset of micropython pins support analog to digital conversion (ADC) (see pyboard [quickref](https://docs.micropython.org/en/latest/pyboard/pyboard/quickref.html)).

`name` Name of the analog input, used to identify data files generated when input is recorded.

`sampling_rate` The rate at which the pin voltage is sampled (Hz). 

`threshold` Threshold against which voltage samples are compared for generating rising and falling events, must be an integer between 0 and 4095.

`rising_event` Name of event triggered when voltage crosses threshold in rising direction.

`falling_event` Name of event triggered when voltage crosses threshold in falling direction.

*Methods:*

`Analog_input.record()`  Start streaming analog input measurements to computer.  If the computer is logging pyControl data the analog data will be saved to disk.  Analog data is saved in seperate files from the main pyControl data log, with a seperate data file for each analog input.  Analog data is saved in binary files with a *.pca* file extension, for information on how to read these files see [Importing data](importing-data.md#analog-data).

`Analog_input.stop()`  Stop streaming analog data to computer.  You can start and stop streaming analog data multples times in a framework run.  If rising or falling events are specified for the analog input these will be generated regardless of whether or not the input is streaming data to the computer.

---

### Digital output

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

`Digital_output.pulse(freq, duty_cycle=50, n_pulses=False)` Turn on a pulse train with specified frequency (Hz). The duty cycle (percentage of the period for which the signal is high) can be specified as 10, 25, 50 or 75.  If the n_pulses argument is set to an integer the pulse train will stop after this number of pulses has been delivered.

`Digital_output.enable_pulse()` Setup output to support pulsed output.

---

## Breakout boards

Breakout boards interface the micropython board with RJ45 behaviour ports, BNC connectors, indicator LEDs and user pushbuttons.  The breakout board classes specify the pin mappings for the boards.

---

**Breakout 1.2**

Current version of the pyControl Breakout board with 6 RJ45 behaviour ports, 4 BNC connectors, indicator LEDs and user pushbutton. Ports 1 & 2 have an additional driver line.  Ports 3 and 4 have an additional DIO line which also supports analog output (DAC).  Ports 3 and 4 support I2C or UART serial communication over two of their DIO lines.

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

Older version of the Breakout board with 4 RJ45 behaviour ports, 4 BNC connectors, indicator LEDs and two user pushbuttons.

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

## Devices

### Poke

Nosepoke port with infra-red beam, stimulus LED and socket to connect solenoid valve.

[Schematic (pdf)](../media/hardware/poke-2-3-sch.pdf) 

|**Front**|**Side - solenoid attached**|
|---|---|
|![Poke front](../media/hardware/poke-front.jpg)|![Poke side](../media/hardware/poke-side.jpg)

Mounted Front
![Poke front mounted](../media/hardware/poke-front-mounted.jpg)

Mounted Back
![Poke back mounted](../media/hardware/poke-back-mounted.jpg)

```python
class Poke(port, rising_event=None, falling_event=None, debounce=5)
```

*Arguments:*

`rising_event` Name of event triggered on IR beam break.

`falling_event` Name of event triggered on IR beam make.

`debounce` Minimum time interval between events (ms), set to False to deactive debouncing.

*Attributes:*

`Poke.LED` Stimulus LED

`Poke.SOL` Solenoid output.

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

### Audio board

Audio amplifier board for driving a speaker to produce auditory stimuli.  The board uses the micropython [DAC](https://docs.micropython.org/en/latest/pyboard/library/pyb.DAC.html) for stimulus generation.  The audio board must be plugged into a port on the breakout board which supports DAC output and I2C serial communication (used to set the volume) - ports 3 and 4 on breakout board 1.2 are suitable.  Up to two audio boards can be used with a single breakout board allowing two speakers to be driven independently.

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

*Example usage:*

```python
speaker = Audio_board(board.port_3) # Instantiate audio board.

speaker.sine(5000) # Play a 5KHz sine wave.

speaker.noise() # Turn on white noise.

speaker.off() # Turn off sound output.
```

---

### LED driver

A constant current LED driver for optogenetic stimulation.

[Schematic (pdf)](../media/hardware/LED-driver-1-1-sch.pdf) 

![LED driver](../media/hardware/LED-driver.jpg)

```python 
class LED_driver(port)
```

*Methods:*

`LED_driver.on()` Turn on LED

`LED_driver.off()` Turn off LED

`LED_driver.pulse(freq, duty_cycle=50, n_pulses=False)` Turn on a pulse train with specified frequency (Hz). The duty cycle (percentage of the period for which the signal is high) can be specified as 10, 25, 50 or 75.  If the n_pulses argument is set to an integer the pulse train will stop after this number of pulses has been delivered.

---

### Stepper motor

Class for controlling a stepper motor.  Requires a stepper motor driver that is controlled using a *direction* and a *step* pin, for example the [EasyDriver](http://www.schmalzhaus.com/EasyDriver/).

```python 
class Stepper_motor(direction_pin, step_pin)
```

*Arguments:* 

`direction_pin` The micropython pin connected to the direction control pin of the stepper motor driver.

`step_pin` The micropython pin connected to the step pin of the stepper motor driver.

*Methods:*

`Stepper_motor.forward(step_rate, n_pulses=False)` Turn the motor forward at the specified step rate (Hz).  If the n_pulses argument is set to an integer the motor will move that many steps at the specified rate and then stop.

`Stepper_motor.backwards(step_rate, n_pulses=False)` Turn the motor backwards.

`Stepper_motor.stop()` Stop the stepper motor.

---

### Rotary encoder

Class for acquiring data from a rotary encoder, used e.g. to measure the speed of a running wheel.  The encoder must be an incremental rotary encoder that outputs a quadrature signal. The rotary encoder class can stream the position or velocity of the encoder to the computer at a specified sampling rate, and generate framework events when the position/velocity goes above/below a specified threshold.  Currently the rotary encoder class expects the two lines carrying the quadrature signal to be connected to micropython pins 'X1' and 'X2' (Port 1 DIO_A and DIO_B on breakout board 1.2).

```python 
class Rotary_encoder(name, sampling_rate, output='velocity', threshold=None,
                     rising_event=None, falling_event=None, bytes_per_sample=2,
                     reverse=False)
```

*Arguments:*

`name` Name of the rotatory encoder, used to identify data files generated when input is recorded.

`sampling_rate` The rate at which encoder position/velocity is sampled.

`output` Whether to stream encoder position or velocity to computer.  Valid values are *'position'* or *'velocity'*.  Also determines whether a position or velocity threshold is used for event generation.  Velocity signals are in units of encoder counts per second, so an encoder with a resolution of 100 counts per revolution turning at 2 revolution per second would output a velocity of 200. Position signals are in units of encoder counts.

`threshold` Threshold against which the position or velocity (as specified by the `output` argument) is compared for generating rising and falling events, must be an integer.

`rising_event` Name of event triggered when position/velocity crosses threshold in rising direction.

`falling_event` Name of event triggered when position/velocity crosses threshold in falling direction.

`bytes_per_sample` Number of bytes used per sample when data is sent to the computer.  Valid values are 2 or 4.  Only set to 4 if your signals are likely to go outside the range covered by 2 byte signed integers (-32748 to 32748).

`reverse` Set to *True* to reverse the direction of rotation which is considered a positive velocity.

*Methods:*

`Rotary_encoder.record()`  Start streaming position/velocity measurements to computer. Data is saved in the same file format as data generated by [analog inputs](#analog-input).

`Rotary_encoder.stop()`  Stop streaming data to computer. If rising or falling events are specified for the rotary encoder these will be generated regardless of whether or not the encoder is streaming data to the computer.

*Attributes:*

`Rotary_encoder.velocity` The current velocity of the encoder.

`Rotary_encoder.position` The current position of the encoder.