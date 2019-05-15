# Troubleshooting

The page details how to fix common problems that can occur when using pyControl.  If you encounter a problem that is not covered on this page, please contact the [google group](https://groups.google.com/forum/#!forum/pycontrol).

### Can't open GUI

To open the GUI you need to run the file *pyControl_GUI.py* in the folder *pyControl/gui* using Python.  One way to do this is to set the file association for *.py* files to Python 3 so that you can run the file by double clicking it.  Alternatively you can open a command prompt, change directory to the folder *pyControl/gui* and run the file with the command `python pyControl_GUI.py`.

If the GUI does not open this is probably because you do not have the required [dependencies](../index.md#dependencies) installed, you should see an error message indicating which dependency could not be loaded. 

### Can't connect to acquisition board.

If the GUI status says 'Connection Failed' when you try to connect to the board, reset the board using the *Reset* button on the breakout board or micropython microcontroller.

### Board acting funny

If a board is acting strangely, e.g. giving error messages like *Error: Unable to transfer file.*, *Error: Unable to execute command.* or *pyControl Framework:Import error* try the following steps to fix the problem:

1. Disconnect from the board using the GUI and reset it using the *Reset* button either on the pyboard or on the pyControl breakout board.

2.  If resetting the board does not solve the problem, it is possible the pyboard's filesystem has got corrupted.  Reset the filesystem by following the instructions [here](https://docs.micropython.org/en/latest/pyboard/tutorial/reset.html#factory-reset-the-filesystem).  The instructions say to use the *Reset* and *USR* buttons and LEDs on the micropython board for the file system reset.  Depending on how the pyControl breakout board is mounted it may be hard to access these.  However the *Reset* and *USR* buttons on the front of pyControl breakout board 1.2 have identical functionality to those on the pyboard, and indicator LEDs 3 and 4 from the left on the breakout board have the same behaviour as the orange and green LEDs on the pyboard, so the filesystem can be reset with access only to the front of the breakout board.  After the filesystem reset has finished, reset the board again using the *Reset* button, then connect to the board with the GUI.  The filesystem reset removes both the pyControl framework and any hardware definition from the pyboard.  The GUI will automatically reload the framework when you connect to the board but you will have to manually reload the correct hardware definition using the board config menu.

These two steps will solve the great majority of board misbehaviour.

### Unable to setup state machine

If you get a message saying *Error: Unable to setup state machine* when you upload a task, this means that there is a problem with the task definition file which gives an error when it is imported.  The error message will be followed by a traceback saying the line in the task file where the error occured and what the error was.  Task definition files are renamed *task_file.py* when they are transferred to the pyboard, so the traceback will refer to errors in the task definition file using this name.

### Error during framework run

If you get a message saying *Error during framework run* while the framework is running, this indicates there is a problem with the task file that does not prevent the file being imported but only occurs while the task is running.  This is often due to errors in state behaviour functions which only occur when the function is called.  The error message will include a traceback indicating the line number in the task file where the error occured and what the error was.