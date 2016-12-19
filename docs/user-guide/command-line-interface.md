# Command line interface

The `pycboard` class and `run_experiment` script provide ways of controlling micropython boards (pyboards) running pyControl from a Python interpreter running on the host computer.  To use them, open a Python 3 interpreter on a computer connected to the pyboards, make sure the folder *pyControl/host* is on the Python path such that you can import they pycboard class with:

```python
from pycboard import Pycboard
```

### Configuration files

The pyControl command line interface expects to find some configuration files in folder *pyControl/host/config*.  When you first install pyControl from the Bitbucket repository this folder will not exist, instead there will be a folder *pyControl/host/example_config* containing example configuration files.  This ensures that if you update your installation of pyControl from the repository your configuration files will not get overwritten. Create directory *pyControl/host/config* and copy the files from *pyControl/host/example_config* into it.  If you are using a [hardware definition](hardware.md) file, put it in this folder and name it *hardware_definition.py*.

You will need to edit [config.py](https://bitbucket.org/takam/pycontrol/src/default/host/example%20config/config.py?at=default&fileviewer=file-view-default) to specify what serial ports your behavioural setups are plugged into.  Edit the variable *box_serials* in *pyControl/host/config/config.py* to specify the serial port for each box number.  For example if you have 4 boxes (numbered 1 - 4) plugged into COM ports 1 - 4, the variable *box_serials* would be set to:

```python
box_serials={1:'COM1',    #Dictionary of box numbers and respective serial port addresses.
             2:'COM2',
             3:'COM3',
             4:'COM4'}
```

Each micropython board has a unique hardware ID number.  Once all of the setups are plugged in with the correctly assigned COM ports, and you have configured the box serials in *config.py*, it is a good idea to save these hardware ID numbers to ensure that if COM port numbers get accidentally reasigned (which can in principle happen when boards are disconnected and reconnected) you will be warned when you run an experiment.  To do this, run the program *run_experiments.py* in *pyControl/host*, select option 0 to enter the config menu, then select option 2 to save hardware IDs.  This will create a file in *pyControl/host/config* called *hardware_unique_IDs.txt* which contains a dictionary of the box numbers and hardware IDs.

## pycboard class

The pycboard class provides an interface to control a micropython board running pyControl from a Python interpreter running on a computer.  It provides methods to load the framework and hardware definition, setup state machines, start and stop the framework running, and various other useful things.

```python
class Pycboard(serial_port)
```

*Methods:*

`Pycboard.load_framework()`

Load the pyControl framework onto the pyboard, this will take some time.  The framework stays on the pyboard filesystem so you only need to load it the first time you use the board, to update the framework to a new version, or if the board filesystem gets corrupted and you have to reset it.

`Pycboard.load_hardware_definition(hwd_path=default_hwd_path)`

Transfer a hardware definition file to pyboard.  If no path is specified the file *hardware_definition.py* from *pyControl/host/config* folder is used by default.  Irespective of the name of the transferred file, it is renamed *hardware_definition.py* on the pyboard filesystem.  The hardware definition file stays on the pyboard filesystem until a new hardward definition is loaded so you do not have to reload it each time you use the board.

`Pycboard.setup_state_machine(sm_name, sm_dir=None)`

Transfer state machine definition file *sm_name.py* to pyboard and instantiate state machine on board.  If directory sm_dir is not provided it defaults to *pyControl/tasks* then *pyControl/examples*.

`Pycboard.run_framework(dur=None, verbose=False)`

Run the framework for the specified duration (seconds) printing the output to the screen.  If duration is not supplied the framework will run until stopped with *ctrl+c*.  If `verbose` is set to `True`, state and event names rather than IDs will be printed.

`Pycboard.set_variable(v_name, v_value)`

Set variable with name `v_name` to value `v_value`.  Note; variables defined in state machine definitions with the syntax `v.` e.g. `v.my_variable = 5`.  When getting or setting the value of variables using the pycboard class you do not need to include the `v.` in the variable name.  You can set variables to numbers, strings, booleans, lists, dicts and tuples, but not with more complex python objects.

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

The program [run_experiment.py](https://bitbucket.org/takam/pycontrol/src/default/host/run_experiment.py) is used for running behavioural experiments with pyControl.

### Specifying experiments

The file [experiments.py](https://bitbucket.org/takam/pycontrol/src/default/host/example_config/experiments.py?at=default&fileviewer=file-view-default) is used to specify the details of all the experiments that are available to be run.  A single experiment is a set of subjects run on a given task at the same time.  An experiment is specified by creating an instance of the [Experiment](https://bitbucket.org/takam/pycontrol/src/default/host/experiment.py) class as in the example below:


```python
example_experiment = Experiment(
                         name = 'Example',    
                         start_date = '2015-07-29',
                         subjects = {1: 's001',
                                     2: 's002'},
                         task = 'example_task')
```

The argument `name` specified the name the experiment will appear as in the menu of experiments in run_experiment.py.  

The argument `task` must correspond to the name of a task description file in either the *pyControl/task* or *pyControl/examples* folders.  

The optional argument `set_variables` can be used to set variables of the task at run time.  The value of the set variables argument must be a dictionary with keys corresponding to the names of the variables to be set, each with a corresponding value for the variable.  The code below would set the value of *variable_A* to the integer 5 and *variable_B* to the string 'x'.  

```python
example_experiment = Experiment(
                         name = 'Example',    
                         start_date = '2015-07-29',
                         subjects = {1: 's001',
                                     2: 's002'},
                         task = 'example_task',
                         hardware = "hw.Box('bkb')",
                         set_variables = {'variable_A': 5,
                                          'variable_B': 'x'})

```

Note; all variables in pyControl tasks should have names that start with `v.`, e.g. `v.variable_A` (see [programming tasks](programming-tasks.md)).  When you are specifying set variables and persistant variables (see below) in an experiment definition you do not include the `v.` at the start of the name.  To set the value of a variable seperately for each box, you can supply a dictionary with keys which match the box numbers.  The following `set_variables` argument would set the value of *variable_C* to 0.5 for box 1 and 0.6 for box 2:

```python
                         set_variables = {'variable_C':  {1: 0.5,
                                                          2: 0.6}}
```

The persistent variables argument can be used to make the values of variables persistent across sessions.  The values of persistent variables are read from each setup at the end of the session and stored in human readable format in the data folder for the experiment.  At the start of the next session the values are loaded from file and set on the setups such that the variable starts the session with the same value it finished the previous session.  The following code would set the values of *variable_D* and *variable_E* to be persistent.

```python
example_experiment = Experiment(
                         name = 'Example',    
                         start_date = '2015-07-29',
                         subjects = {1: 's001',
                                     2: 's002'},
                         task = 'example_task',
                         hardware = "hw.Box('bkb')",
                         persistent_variables = ['variable_D', 'variable_E'])

```

### Running an experiment

To run an experiment, run the program *run_experiment.py*.  You will be presented with a numbered list of experiments which correspond to those you have created in the file *host/config/experiments.py*.  Enter the number for the experiment you want to run.  You will be asked whether you want to run a hardware test.  If you select yes the state machine *hardware_test* from the examples folder will be run on the boxes.  This script is designed to allow the user to test the specific hardware used for running the Two step task, if you are using a different hardware configuration you will want to write your own hardware test script.  When the hardware test is complete (or skipped), the program uploads the task state machine to all the boxes, sets variables as specified in the experiment definition and waits for the user to start the experiment by pressing enter.  While the experiment is running, the data output from the boxes is displayed on the screen and written to seperate files for each box.  The files are saved in the data folder *pyControl/data/start_date-experiment_name* .  The data file names are the subject ID and date.  


























