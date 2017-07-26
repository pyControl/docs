# Importing data

The module [data_import.py]() contains tools for importing and representing pyControl sessions and experiments in Python.  

The data import module has the following dependencies:

- Python 3.5+

- numpy

## Session class

The `Session` class is used to import a pyControl data file and represent it as a Python object.  

**Example usage:**

```python
import data_import as di # Import the data import module.

session = di.Session('path//to//session//file') # Instantiate session object from data file.

session.events # List of state entries and events in order they occured.  Each item is a 
               # namedtuple with fields 'time' & 'name', such that you can get the 
               # name and time of event/state entry x with x.name and x.time respectively.

session.times # Dictionary with keys that are the names of the framework events and states and 
              # values which are Numpy arrays of the times (in milliseconds since the
              # start of the framework run) at which the event/state entry occured.

session.print_lines # List of all the lines output by print statements during the framework run, 
                    # each line starts with the time in milliseconds at which it was printed.

```

**Class reference** 

```python
class Session(file_path, int_subject_IDs=True)
```

*Arguments:*

`file_path` Path of the pyControl data file to import.

`int_subject_IDs` If `True`, subject ID is converted to integer, e.g. `'m012'` is converted to `12`.  Otherwise subject ID is a string.

*Attributes:*

`Session.file_name` Name of data file.

`Session.experiment_name` Name of experiment.

`Session.task_name` Name of the pyControl task used to generate the file.

`Session.subject_ID` ID of subject.

`Session.datetime` The date and time that the session started stored as a [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) object.

`Session.datetime_string` The date and time that the session started stored as a string of format 'YYYY-MM-DD HH:MM:SS'

`Session.events` List of state entries and events in order they occured.  Each item is a namedtuple with fields 'time' & 'name', such that you can get the name and time of event/state entry x with x.name and x.time respectively.

`Session.times` Dictionary with keys that are the names of the framework events and states and values which are Numpy arrays of the times (in milliseconds since the start of the framework run) at which the event/state entry occured.

`Session.print_lines` List of all the lines output by print statements during the framework run, each line starts with the time in milliseconds at which it was printed.

## Experiment class

The `Experiment` class is used to import all data files from a given experiment and represent the experiment as a Python object.  All the data files must be in a single folder.

**Example usage:**

```python
import data_import as di # Import the data import module.

experiment = di.Experiment('path//to//experiment//folder') # Instantiate experiment object from data folder.

experiment.save() # Save sessions as .pkl file to speed up subsequent loading of experiment.

experiment.get_sessions(subject_IDs='all', when=1) # Return session number 1 for all subjects.

experiment.get_sessions(subject_IDs='all', when=[1,3,5]) # Return session numbered 1,3 or 5 for all subjects.

experiment.get_sessions(subject_IDs=[12,13], when='2017-06-23') # Return sessions from specified subjects and date.

```

**Class reference** 

```python
class Experiment(folder_path, int_subject_IDs=True)
```

*Arguments:*

`folder_path` Path of the pyControl data folder to import.

`int_subject_IDs` If `True`, subject IDs are converted to integers, e.g. `'m012'` is converted to `12`.  Otherwise subject IDs are strings.

*Attributes:*

`Experiment.folder_name` Name of the experiment folder.

`Experiment.path` Path of the experiment folder

`Experiment.sessions` List of all sessions in experiment.

`Experiment.subject_IDs` List of all subject IDs

`Experiment.n_subjects` Number of subjects.

*Methods:*

```python
Experiment.save()
```
 Save all sessions as .pkl file. Speeds up subsequent instantiation of experiment as sessions do not need to be created from data files.

```python
Experiment.get_sessions(subject_IDs='all', when='all')
```
Returns a list of sessions which match specified subject ID and time. 

`subject_ID` can be `'all'` to select sessions from all subjects or can be a list of subject IDs.  

`when` argument determines session numbers or dates to select, see examples below:

```python
when = 'all'      # All sessions
when = 1          # Sessions numbered 1
when = [3,5,8]    # Session numbered 3,5 & 8
when = [...,10]   # Sessions numbered <= 10
when = [5,...]    # Sessions numbered >= 5
when = [5,...,10] # Sessions numbered 5 <= n <= 10
when = '2017-07-07' # Select sessions from date '2017-07-07'
when = ['2017-07-07','2017-07-08'] # Select specified list of dates
when = [...,'2017-07-07'] # Select session with date <= '2017-07-07'
when = ['2017-07-01',...,'2017-07-07'] # Select session with '2017-07-01' <= date <= '2017-07-07'.
```
