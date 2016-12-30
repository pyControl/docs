# Command line interface

The pyControl command line interface (CLI) is a python module which provides tools for controlling micropython boards (pyboards) running pyControl from a Python interpreter running on the host computer.  The two principal tools are the `Pycboard` class and the `run_experiment` function/script.  The Pycboard class provides an interface for controlling a single pyboard at a time and is typically used when prototyping tasks or testing a hardware setup.  The run_experiment function runs a task on a set of pyboards and stores the data generated to disk, as the name suggests it is normally used for running experiments.

## Installation

The recomended way of installing the pyControl CLI is to download the file `pyControl-cli.zip` from the repository's [downloads](https://bitbucket.org/takam/pycontrol/downloads) page. Unzip the folder on your computers filesystem, in the following documentation we will assume that the root directory of the repository is located at `C:\pyControl-cli`.

When you unpack the repository you will have the following folder structure:

```
- pyControl-cli
    - cli          # The command line interface module
    - config       # Configuration files edited by user.
    - data         # Data output by the CLI.
    - devices      # pyControl hardware classes (uploaded to pyboard).
    - pyControl    # pyControl framework        (uploaded to pyboard).
    - tasks        # Task definition files.
```

### Dependencies

The pyControl CLI has the following dependcies:

- Python 3 
- pyserial
- pyperclip (optional, used to copy summary data to clipboard)

The CLI has only been tested on Windows 7 and 10 but in principle should be cross platform. You may need to install the micropython USB drivers to ensure your operating system recognises the board and can open a serial connection to it, see [micropython windows setup](http://micropython.org/resources/Micro-Python-Windows-setup.pdf) or the micropython [docs](http://docs.micropython.org/en/latest/pyboard/).

Crashes have been observed when using pyControl with pyboards that are running old versions of the Micropython firmware (version < 1.6).  When you connect to a board with the CLI the micropython version running on the board is displayed.  Information and downloads for updating the micropython firmware can be found [here](http://micropython.org/download).  Note, you can put a pyboard into device firmware update mode using the Pycboards `DFU_mode` method (see below), this is often easier than using a hardware jumper as suggested in the instructions.

### Updating 

To update the pyControl CLI, download the latest version from the download page, unzip it, and copy across the *config* and *tasks* directories from your old installation to keep you configuration setttings and tasks.

Alternatively if you are familar with version control software you can clone the repository rather than downloading it as a zip.  You can then pull the latest version from the repository to update, but be careful not to overwrite your configuration files when you do so.

## Configuration

The *config* folder contains configuration files which you will need to edit to match your experimental setup.

The file *config.py* specifies various configuration variables but the only one you need to edit is `board_serials` which specifies what serial ports your behavioural setups are plugged into. For example if you have 4 setups (numbered 1 - 4) plugged into COM ports 1 - 4 you would set:

```python
board_serials={1:'COM1',    # Board numbers with respective serial port addresses.
               2:'COM2',
               3:'COM3',
               4:'COM4'}
```

The file *hardware_definition.py* specifies the hardware connected to your pyboards, see [hardware](hardware.md) for more information.

The file *experiments.py* specifies the experiments available to be run using `run_experiment`, see below for more information.

## Usage

You can use the pyControl CLI from a regular python interpreter but it is recomended to use the [ipython](http://ipython.readthedocs.io/en/stable/) shell as it provides an input history, tab completion and other useful features.  You can try the following commands to start using the CLI:

```python
# Change directory to the the CLI root directory using ipython..
%cd C:\pyControl-cli

# ..or regular python.
import os
os.chdir('C:\\pyControl-cli')

from cli import Pycboard # Import the Pycboard class.

board = Pycboard('COM1') # Instantiate board, set serial port as appropriate.

board.load_framework()   # Transfer pyControl framework to pyboard.

board.setup_state_machine('blinker') # Setup blinker state machine.

board.run_framework(verbose=True) # Run the framework (press ctrl+c to stop run)

from cli import run_experiment # Import run_experiment function.

run_experiment() # Run an experiment, alternatively just double click
                 # run_experiment.py
```

If you are having trouble opening a serial connection to a board, check that you have specified the serial port correctly (on windows look in the device manager under *Ports (COM and LTP)*).  If you still cannot open a connection try closing the python interpreter, resetting the pyboard with the reset button and trying again.

## Pycboard class

The Pycboard class provides an interface to control a micropython board running pyControl from a Python interpreter running on a computer.  It provides methods to load the framework and hardware definition, setup state machines, start and stop the framework running, and various other useful things.

```python
class Pycboard(serial_port)
```

*Methods:*

`Pycboard.load_framework()`

Load the pyControl framework onto the pyboard, this will take some time.  The framework stays on the pyboard filesystem so you only need to load it the first time you use the board, to update the framework to a new version, or if the board filesystem gets corrupted and you have to reset it.

`Pycboard.load_hardware_definition(hwd_path=None)`

Transfer a hardware definition file to the pyboard.  If no path is specified the file *hardware_definition.py* from the *config* folder is used by default.  Irespective of the name of the transferred file, it is renamed *hardware_definition.py* on the pyboard filesystem.  The hardware definition file stays on the pyboard filesystem until a new hardward definition is loaded so you do not have to reload it each time you use the board.

`Pycboard.setup_state_machine(sm_name, sm_dir=None)`

Transfer state machine definition file *sm_name.py* from folder *sm_dir* to pyboard and instantiate state machine on board.  If directory *sm_dir* is not provided it defaults to the *tasks* directory.

`Pycboard.run_framework(dur=None, verbose=False)`

Run the framework for the specified duration (seconds) printing the output to the screen.  If duration is not supplied the framework will run until stopped with *ctrl+c*.  If `verbose` is set to `True` state and event names rather than IDs will be printed.

`Pycboard.set_variable(v_name, v_value)`

Set variable with name `v_name` to value `v_value`.  Note; variables are defined in state machine definitions with the syntax `v.` e.g. `v.my_variable = 5` (see [programming tasks](programming-tasks.md)).  When getting or setting the value of variables using the pycboard class you do not include the `v.` in the variable name. You can set variables to numbers, strings, booleans, lists, dicts and tuples, but not with more complex python objects.

`Pycboard.get_variable(v_name)`

Get value of variable named `v_name`.

`Pycboard.reset_filesystem()`

Delete all files on the pyboard filesystem except boot.py.

`Pycboard.DFU_mode()`

Put the pyboard into device firmware update mode.  This can be used to [update](http://micropython.org/download) the version of Micropython running on the board.  


*Example usage:*

```python
board = Pycboard('COM1') # Instantiate board, set serial port as appropriate.

board.load_framework() # Transfer framework to pyboard.

board.load_hardware_definition() # Transfer hardware definition to pyboard.

board.setup_state_machine('random_ratio') # Setup state machine random_ratio.

board.set_variable('ratio', 10)  # Set variable v.ratio to 10.

board.get_variable('session_duration') # Get value of variable v.session_duration

board.run_framework(verbose=True) # Run framework with verbose data output.
```

## Running experiments

The function `run_experiment` is used for running an experiment on a set of pyControl setups.  It also has a config menu which allows you to perform various operations on a set of boards.

### Specifying experiments

The file *config\experiments.py* is used to specify the experiments that are available to be run.  The file must start by importing the Experiment class which is used to define experiments:

```python
from cli.experiment  import *
```

An experiment is a set of subjects run on a given task at the same time.  An experiment is specified as in the example below:


```python
simple_exp = Experiment(
          name = 'simple_experiment',    
          start_date = '2016-12-01',
          subjects = {1: 'm001',
                      2: 'm002'},
          task = 'random_ratio')
```

`name` specifies the name the experiment will appear as in the menu of experiments in run_experiment. The name will also be used along with the `start_date` to name the experiments data folder.

`subjects` must be a dictionary of setup numbers and their coresponding subject IDs.

`task` must correspond to the name of a task description file in the *tasks* folder.  

Various optional arguments can be provided as in the example below:

```python
example_exp = Experiment(
          name = 'example_experiment',    
          start_date = '2016-12-01',
          subjects = {1: 'm003',
                      2: 'm004'},
          task = 'reversal_learning',
          set_variables = {'session_duration':  2*hour,
                           'reward_durations': {1:[80,90],   
                                                2:[75,85]}
                           },
          persistent_variables = ['state'], 
          summary_variables = ['n_rewards', 
                               'n_trials'])
```

`set_variables` allows the value of specified variables to be set at runtime.  It must be a dictionary with keys corresponding to the names of the variables to be set, each with a corresponding value for the variable.  To set the value of a variable seperately for each setup, you can supply a dictionary with keys which match the setup numbers. The above example sets the variable *session_duration* to 2 hours for all the setups, and the variable *reward_durations* to [80,90] for setup 1 and [75,85] for setup 2.

`persistent_variables` is used to make the values of specified variables persistent across sessions. The values of persistent variables are read from each setup at the end of the session and stored in text files in the data folder for the experiment.  The above example makes the variable *state* persistant across sessions.

`summary_variables` is used to specify that certain variables are summary information which should be displayed at the end of the session.  The value of each summary variable is displayed for all subjects at the end of the run and is also copied to the clipboard in a format which allows pasting directly into a spreadsheet.

### Running an experiment

The recomended way to run an experiment is to just double click the *run_experiments.py* file in the *cli* folder.

You can also run the function from a python interpreter using:

```python
from cli import run_experiment 

run_experiment()
```

You will be presented with a numbered list of experiments which correspond to those you have created in the file *host/config/experiments.py*.  Enter the number for the experiment you want to run.  

You will be asked whether you want to run a hardware test.  If you select yes the state machine *hardware_test* from the *tasks* folder will be run on the setups. Running a hardware test allows you to to check that all the experimental hardware is working before starting the days experiments.  If you want to use it you will need to create an appropriate hardware test for your setups.

When the hardware test is completed or skipped, the program uploads the task state machine to all the setups, sets variables as specified in the experiment definition and waits for the user to start the experiment by pressing enter.  While the experiment is running, the data output from the setups is displayed on the screen and written to seperate files for each setups.  The files are saved in the data folder *pyControl/data/start_date-experiment_name*.  The data file names format is *subject_ID-YYYY-MM-DD*.

### Config menu

When you start `run_experiment` you can enter a config menu by selecting option 0.  The config menu allows you to do the following
operations on all the pyboards.

- **Reload framwork**: Used to update the framework or install the framework on all the boards the first time they are used.
- **Reload hardware definition**: Used to change the hardware definition on the boards.
- **Save hardware IDs**:  Each pyboard has a unique hardware ID number.  This function saves the hardware ID numbers of all the boards to a file *hardware_unique_IDs.txt* in the *config* folder.  The hardware unique IDs are then checked against these saved values each time run_experiment is used to ensure that the COM port numbers have not got reasigned (which can in principle happen when boards are disconnected and reconnected).
- **Hard reset boxes**:  Hard reset all the boards, equivalent to pressing the reset button on each board.
- **Reset filesystems**: Reset the filesystem of all the boards.


























