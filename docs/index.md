# pyControl

Open source, Python based, behavioural experiment control.

---

## Overview

**pyControl** is a system of open source hardware and software for controlling behavioural experiments, built around the [Micropython](https://micropython.org/) microcontroller.

pyControl makes it easy to program complex behavioural tasks using a clean, intuitive, and flexible syntax for specifying tasks as state machines. User created task definition files, written in Python, run directly on the microcontroller, supported by pyControl framework code.  This gives users the power and simplicity of Python for specifying task behaviour, while allowing advanced users low-level access to the microcontroller hardware.  For more information see [programming tasks](user-guide/programming-tasks.md).

pyControl [hardware](user-guide/hardware.md) consists of a breakout board that interfaces the microcontroller with a set of connectors, and a family of devices such as nose pokes, audio boards, LED drivers, rotary encoders and stepper motor controllers that can be used to create a wide variety of different behavioural setups.  Assembled pyControl hardware is available from the [OpenEphys store](http://www.open-ephys.org/store).

pyControl has a [Graphical User Interface](user-guide/graphical-user-interface.md) (GUI) and a [Command Line Interface](user-guide/command-line-interface.md) (CLI).   The GUI is the recommended way to get started with pyControl.  The command line interface provides tools for running tasks on many setups in parallel.

Tools for importing pyControl data into Python for analysis are provided in the [data_import](user-guide/importing-data.md) module.

The pyControl [google group](https://groups.google.com/forum/#!forum/pycontrol) is a email list for pyControl users.

**GUI**
![run_task_GUI.jpg](media/run_task_GUI.jpg)
**Breakout board**
![Breakout 1.2 back](media/hardware/breakout-1-2-back.jpg)

---

## Getting started


### Installation

Download the latest version of pyControl as a zip file from the repository's [downloads](https://bitbucket.org/takam/pycontrol/downloads/) page. Unzip the folder on your computer and you will have the following folder structure:

```
- pyControl
	- gui          # Graphical user interface
    - cli          # Command line interface
    - com          # Serial communication and data logging
    - config       # Configuration files edited by user
    - data         # Default folder for pyControl data
    - devices      # pyControl hardware classes (uploaded to pyboard).
    - pyControl    # pyControl framework        (uploaded to pyboard).
    - tasks        # Task definition files
    - tools        # Tools for importing pycontrol data
```

### Dependencies

pyControl has the following dependencies:

- Python 3 
- pyserial
- numpy     (GUI only)
- pyqtgraph (GUI only)
- pyperclip (optional, used to copy summary data to clipboard)

The simplest way to install the required dependencies is to download and install the [Anaconda](https://www.anaconda.com/download/) Python distribution, then use the *conda* package management utility to install the other packages using the following commands in the *Anaconda Prompt*:

```
conda update conda
conda install -c anaconda pyserial
conda install -c anaconda numpy
conda install -c anaconda pyqtgraph
conda install -c conda-forge pyperclip
```

pyControl has been tested primarily on Windows 7 and 10 but in principle should be cross platform and has been used on Mac and Linux.  You may need to install the micropython USB drivers to ensure your operating system recognizes the board and can open a serial connection to it, see [micropython windows setup](http://micropython.org/resources/Micro-Python-Windows-setup.pdf) and the micropython [docs](http://docs.micropython.org/en/latest/pyboard/pyboard/tutorial/repl.html).

Micropython boards (pyboards) need to be running a fairly recent version of the Micropython firmware to work with pyControl (version >= 1.9).  When you connect to a pyboard with the GUI, the micropython version running on the board is displayed.  Instructions for updating the micropython firmware can be found for windows [here](http://micropython.org/download) and for Linux/Mac [here](https://github.com/micropython/micropython/wiki/Pyboard-Firmware-Update). You can use the GUI's board config menu to put the pyboard into device firmware upgrade (DFU) mode rather than physically connecting the DFU pin to 3.3V.

### Updating

To update pyControl, download the latest version from the download page, unzip it, and copy across the *config* and *tasks* directories from your old installation to keep you configuration settings and tasks.  After updating pyControl you should reload the pyControl framework onto your pyboards using the GUI board config menu.

Alternatively you can use version control software to clone the repository rather than downloading it as a zip.  You can then pull the latest version from the repository to update, but be careful not to overwrite your configuration files.

### Running a task

1. Run the file *run_task_gui.py* in the folder *pyControl/gui*, you will see a GUI window like that shown above.

2. Plug in a pyboard and it will appear in the *Serial port* drop down menu.  Select the board and press the *Connect* button.  The GUI will connect to the board and upload the pyControl framework.

3. From the *Tasks* drop down menu, select the task [*blinker*](https://bitbucket.org/takam/pycontrol/src/default/tasks/blinker.py).  Press the *Upload* button to upload the task to the pyboard.

4. Press the *Start* button.  The task will run causing the blue LED on the pyboard to start blinking.

5.  While the task is running, press the *Variables* button to open the dialog for setting and getting task variables.  Set the variable *LED_n* to 1,2,3 or 4 to change the color of LED that is flashing.

6.  Stop the task with the *Stop* button.

7.  To save data generated by the task to disk, enter a subject ID in the *Subject ID* text box.  The *Start* button will change to *Record* indicating that data from the run will be saved.  Run the task with the *Record* button, a data file will be created in the *pyControl/data* folder.

## Developer's guide

Do you want to contribute for the pyControl project? You can find more information [here](/contributing).