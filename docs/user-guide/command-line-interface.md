# Command line interface

The pyControl command line interface (CLI) provides a text based interface for controlling micropython boards (pyboards) running pyControl. Before the GUI was developed the CLI was the principal way of using pyControl, but it is now depreciated and will be removed from future versions of pyControl at some point. 

The two principal tools are the scripts *run_task.py* and *run_experiment.py*. The *run_task* script configures and runs a task on a single pyboard. The *run_experiment* script runs experiments specified in a configuration file on a set of pyboards, it is used for running experiments on many setups in parallel.  

## Run task

The *run_task* script in folder *pyControl/cli* can be used to setup, configure and run tasks on a single pyboard.  To run it double click the script file, the menus should be pretty self explanatory. All functionality of the CLI *run_task* script is also supported by the GUI and using the GUI is recommended for interacting with a single pyboard.

## Run experiment

The *run_experiment* script in folder *pyControl/cli* is used for running an experiment on multiple pyControl setups in parallel.  It also has a board config menu which allows you to perform various operations on a set of boards.

### Configuration

The *config* folder contains configuration files which you will need to edit to match your experimental setup.

The file *hardware_definition.py* specifies the hardware connected to your pyboards, see [hardware](hardware.md) for more information.  When you change your hardware definition you will need to upload the new version to the pyboards using the board config menu in the GUI or *run_task* or *run_experiment* CLI scripts.

The file *config.py* specifies various configuration variables but the only one you need to edit is `board_serials` which specifies what serial ports your behavioural setups are plugged into. For example if you have 4 setups (numbered 1 - 4) plugged into COM ports 1 - 4 you would set:

```python
board_serials = {1:'COM1',    # Setup numbers with serial port addresses.
                 2:'COM2',
                 3:'COM3',
                 4:'COM4'}
```

Once you have specified the serial ports of your boards in the config file you can select them in *run_task.py* by just entering the board number rather than the serial port.

The file *experiments.py* specifies the experiments available to run using the script *run_experiment.py*, see below for more information.

### Specifying experiments


To use the *run_experiment* script you first have to edit the file *config\experiments.py* which specifies the experiments that are available to run.  The file must start with:

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

`subjects` must be a dictionary of setup numbers and their corresponding subject IDs.

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

`set_variables` allows the value of specified variables to be set at runtime.  Must be a dictionary with keys corresponding to the names of the variables to be set, each with a corresponding value for the variable.  To set the value of a variable separately for each setup, you can supply a dictionary with keys which match the setup numbers used in the experiment.  The above example sets the variable *session_duration* to 2 hours for all the setups, and the variable *reward_durations* to [80,90] for setup 1 and [75,85] for setup 2.  

Note, setting variables to invalid values due to typo's or mistakes in the set_variables argument is a common cause of crashes in pyControl experiments (e.g. setting a variable that needs to be a number to a list). If you have a task that runs fine normally but is giving errors when you run it with set variables, double check that the set variables arguement is correct.

`persistent_variables` is used to make the values of specified variables persistent across sessions. The values of persistent variables are read from each setup at the end of the session and stored in text files in the data folder for the experiment.  The above example makes the variable *state* persistent across sessions.

`summary_variables` is used to specify that certain variables are summary information which should be displayed at the end of the session.  The value of each summary variable is displayed for all subjects at the end of the run and is also copied to the clipboard in a format which allows pasting directly into a spreadsheet.

### Running an experiment

To run the script, double click the *run_experiments.py* file. You will be presented with a numbered list of experiments which correspond to those you have created in the *experiments.py* file.  Enter the number for the experiment you want to run.  

You will be asked whether you want to run a hardware test.  If you select yes the state machine *hardware_test* from the *tasks* folder will be run on the setups. Running a hardware test allows you to to check that all the experimental hardware is working before starting the days experiments.  If you want to use it you will need to create an appropriate hardware test for your setups.

When the hardware test is completed or skipped, the program uploads the task state machine to all the setups, sets variables as specified in the experiment definition and waits for the user to start the experiment by pressing enter.  While the experiment is running, the data output from the setups is displayed on the screen and written to separate files for each setups.  The files are saved in the data folder *pyControl/data/start_date-experiment_name*.  The data file names format is *subject_ID-YYYY-MM-DD*.

### Config menu

When you start `run_experiment` you can enter a config menu by selecting option 0.  The config menu allows you to do the following
operations on all the pyboards.

- **Reload framwork**: Used to update the framework or install the framework on all the boards the first time they are used.
- **Reload hardware definition**: Used to change the hardware definition on the boards.
- **Save hardware IDs**:  Each pyboard has a unique hardware ID number.  This function saves the hardware ID numbers of all the boards to a file *hardware_unique_IDs.txt* in the *config* folder.  The hardware unique IDs are then checked against these saved values each time run_experiment is used to ensure that the COM port numbers have not got reassigned (which can in principle happen when boards are disconnected and reconnected).
- **Hard reset boards**:  Hard reset all the boards, equivalent to pressing the reset button on each board.
- **Reset filesystems**: Reset the filesystem of all the boards.