# pyControlGUI Test Cases - Board jobs

##  Run task for subject

![Running task](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/run_task.png)

### Resume table

| Test name | Date | Result | Comments |
|---|---|---|---|
| 1. Run task "blinker"
| 2. Run task "left\_poke\_button"
| 3. Board without framework
| 4. Board with framework corrupted
| 5. Subject without task
| 6. Subject without board
| 7. Invalid task
| 8. Board with serial port not available
| 9. Cancel by pressing “stop” button on GUI
| 10. Interrupt board connection
| 11. Run for all boards
| 12. Run all and then cancel by pressing “stop all” button on GUI
| 13. Run for all and then one board stops/fails

### Preparing test case

NB: For this test case we will consider ***COM4*** and ***COM5*** serial ports.

1. Download project sample [My project - step 3.zip](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/test-cases/samples/my-project-step3.zip) and unzip folder
2. Connect 2 pyBoards and find out serial ports names (example on UNIX: /dev/tty.usbmodem1233, example on Windows: COM4)
3. Start ***pyControlGUI***
4. Select ***File > Open project***
5. Choose ***My project - step 3*** example
6. Expand ***Experimental setups***, select experimental setup ***board1***
7. On Details window, press ***Install framework***
8. Expand ***Experimental setups***, select experimental setup ***board 2***
9. On Details window, press ***Install framework***

### 1. Run task "blinker"

**Scenario type:** Success

**Preconditions:** Follow step ***Preparing test case***

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m329***
2. Select option "Run"

**What to expect:**

* Task is uploaded and starts running on this subject board
* Board messages printed to board console
* Buttons “Upload”, “Configure”, “Run”, “Upload all” and “Run all” get blocked
* "Run" button changes to "Stop"
* New session file is created and appears under this setup node
* GUI message: None

### 2. Run task "left\_poke\_button"

**Scenario type:** Success

**Preconditions:** Follow step ***Preparing test case***

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m996***
2. Select option "Run"
3. Press button on board several times

**What to expect:**

* Task is uploaded and starts running on this subject board
* Board messages printed to board console
* Buttons “Upload”, “Configure”, “Run”, “Upload all” and “Run all” get blocked
* "Run" button changes to "Stop"
* New session file is created and appears under this setup node
* GUI message: None

### 3. Board without framework

**Scenario type:** Error

**Preconditions:** 

* Follow step ***Preparing test case***
* Manually remove folder ***pyControl*** from pyBoard filesystem (if exists) connected on COM4 (board1)

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m845***
2. Select option "Run"

**What to expect:**

* Task is not uploaded
* Board messages printed to board console
* Buttons are reset
* GUI Message: “Please install framework on board”

### 4. Board with framework corrupted

See [issue](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/77/how-to-test-board-with-framework-corrupted).

### 5. Subject without task

**Scenario type:** Error

**Preconditions:** Follow step ***Preparing test case***

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***mxx1***
2. Select option "Run"

**What to expect:**

* Task is not uploaded
* Board messages printed to board console
* Buttons are reset
* GUI Message: “Please assign task to subject”


### 6. Subject without board

**Scenario type:** Error

**Preconditions:** Follow step ***Preparing test case***

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***mxx2***
2. Select option "Run"

**What to expect:**

* Task is not uploaded
* Board messages printed to board console
* Buttons are reset
* GUI Message: “Please assign board to subject”

### 7. Invalid task

**Scenario type:** Error

**Preconditions:** 

* Follow step ***Preparing test case***
* Alternative: provide any kind of invalid task (examples: task name with spaces, path not found, no set variables defined, task code is empty, etc.)

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***mxx3*** (assigned task code empty)
2. Select option "Run"

**What to expect:**

* No task uploaded
* Board messages printed to board console
* GUI Message: “Invalid task: %error%”

### 8. Board with serial port not available

**Scenario type:** Error

**Preconditions:** Follow step ***Preparing test case***
 
**Workflow:**

1. Copy content from task ***blinker2*** to ***task_xx*** 
2. Expand ***Experiments > Fox P2 extended***, select subject ***mxx3***
3. Select option "Run"

**What to expect:**

* Task is not uploaded
* Board messages printed to board console
* Buttons are reset
* GUI Message: “Board serial port not available: COM243”

### 9. Cancel by pressing “stop” button on GUI

**Scenario type:** Success

**Preconditions:** Follow step ***Preparing test case***

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m845***
2. Select option "Run"
3. Select option "Stop"

**What to expect:**

* Operation is aborted (board stops running task)
* Buttons are reset
* Board messages printed to board console
* GUI Message: None

### 10. Interrupt board connection

**Scenario type:** Error

**Preconditions:** Follow step ***Preparing test case***

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m845***
2. Select option "Run"
3. Interrupt connection: press "reset" button OR disconnect cable OR eject board via software

**What to expect:**

* Operation is aborted (board stops running task)
* Buttons are reset
* Board messages printed to board console
* GUI Message: “Problem connecting with board: %error_message%”

### 11. Run task for all boards (different tasks assigned)

**Scenario type:** Success

**Preconditions:** 

* Follow step ***Preparing test case***
* Remove subjects ***mxx1***, ***mxx2*** and ***mxx3***

**Workflow:**

1. Expand ***Experiments***
2. Select experiment ***Fox P2 extended***
2. Select option "Run all"

**What to expect:**

* Task is uploaded and starts running on each board (in parallel)
* Board messages printed to board console
* Buttons “Upload”, “Configure”, “Run”, “Upload all” and “Run all” get blocked
* "Run all" button changes to "Stop"
* For each subject, new session file is created and appears under setup node
* GUI message: None

### 12. Run task for all and then cancel by pressing “stop all” button on GUI


**Scenario type:** Success

**Preconditions:**

* Follow step ***Preparing test case***
* Remove subjects ***mxx1***, ***mxx2*** and ***mxx3***

**Workflow:**

1. Expand ***Experiments***
2. Select experiment ***Fox P2 extended***
2. Select option "Run all"
4. Select option "Stop all"

**What to expect:**

* Operation is aborted for all boards (all boards stop running task)
* Buttons reset
* Board messages printed to board console
* GUI Message: None

### 13. Run task for all and then one board stops/fails

**Scenario type:** Error

**Preconditions:**

* Follow step ***Preparing test case***
* Remove subjects ***mxx1***, ***mxx2*** and ***mxx3***

**Workflow:**

1. Expand ***Experiments***
2. Select experiment ***Fox P2 extended***
2. Select option "Run all"
3. Select option "Stop" or disconnect board in one of the running subjects

**What to expect:**

* Operation is aborted for each board disconnected/stopped
* Buttons are reset for subject of disconnected board
* Board messages printed to board console
* All other boards get unaffected
* GUI Message: “Problem connecting with board serial port %serialport%” (if it applies)

