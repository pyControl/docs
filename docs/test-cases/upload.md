# pyControlGUI Test Cases - Board jobs

##  Upload task for subject

### Resume table

| Test name | Date | Result | Comments |
|---|---|---|---|
| 1. Upload task "blinker"
| 2. Board without framework
| 3. Board with framework corrupted
| 4. Subject without task
| 5. Subject without board
| 6. Invalid task
| 7. Board with serial port not available
| 8. Cancel by pressing “stop” button on GUI
| 9. Interrupt board connection
| 10. Upload task for all boards
| 11. Upload task for all and then cancel by pressing “stop all” button on GUI
| 12. Upload task for all and then one board stops/fails

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

### 1. Upload task "blinker"

**Scenario type:** Success

* Follow step ***Preparing test case***

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m239***
2. Select option "Upload"

**What to expect:**

* Task is uploaded to this subject board 
* Board messages printed to board console
* Buttons “upload”, “configure”, “run”, “upload all” and “run all” get blocked

### 2. Board without framework

**Scenario type:** Error

**Preconditions:** 

* Follow step ***Preparing test case***
* Manually remove folder ***pyControl*** from pyBoard filesystem (if exists) connected on COM4 (board1)

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m845***
2. Select option "Upload"

**What to expect:**

* No task uploaded
* Board messages printed to board console
* GUI Message: “Please install framework on board”

### 3. Board with framework corrupted

See [issue](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/77/how-to-test-board-with-framework-corrupted).

### 4. Subject without task

**Scenario type:** Error

**Preconditions:** Follow step ***Preparing test case***

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***mxx1***
2. Select option "Upload"

**What to expect:**

* No task uploaded
* Board messages printed to board console
* GUI Message: “Please assign task to subject”


### 5. Subject without board

**Scenario type:** Error

**Preconditions:** Follow step ***Preparing test case***

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***mxx2***
2. Select option "Upload"

**What to expect:**

* No task uploaded
* Board messages printed to board console
* GUI Message: “Please assign board to subject”

### 6. Invalid task

**Scenario type:** Error

**Preconditions:** 

* Follow step ***Preparing test case***
* Alternative: provide any kind of invalid task (examples: task name with spaces, path not found, no set variables defined, task code is empty, etc.)

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***mxx3*** (assigned task code empty)
2. Select option "Upload"

**What to expect:**

* No task uploaded
* Board messages printed to board console
* GUI Message: “Invalid task: %error%”


### 7. Board with serial port not available

**Scenario type:** Error

**Preconditions:** Follow step ***Preparing test case***
 
**Workflow:**

1. Copy content from task ***blinker2*** to ***task_xx*** 
2. Expand ***Experiments > Fox P2 extended***, select subject ***mxx3***
3. Select option "Upload"

**What to expect:**

* Task is not uploaded
* Board messages printed to board console
* Buttons are reset
* GUI Message: “Board serial port not available: COM243”


### 8. Cancel by pressing “stop” button on GUI

**Scenario type:** Success

**Preconditions:** Follow step ***Preparing test case***

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m845***
2. Select option "Upload"
3. Select option "Stop"

**What to expect:**

* Operation is aborted (upload may or not be completed)
* Buttons reset
* Board messages printed to board console
* GUI Message: None



### 9. Interrupt board connection

**Scenario type:** Error

**Preconditions:** Follow step ***Preparing test case***

**Workflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m845***
2. Select option "Upload"
3. Interrupt connection: press "reset" button OR disconnect cable OR eject board via software

**What to expect:**

* Operation is aborted (upload may or not be completed)
* Buttons reset
* Board messages printed to board console
* GUI Message: “Problem connecting with board serial port %serialport%”


### 10. Upload task for all boards (different tasks assigned)

**Scenario type:** Success

**Preconditions:** 

* Follow step ***Preparing test case***
* Remove subjects ***mxx1***, ***mxx2*** and ***mxx3***

**Workflow:**

1. Expand ***Experiments***
2. Select experiment ***Fox P2 extended***
2. Select option "Upload all"

**What to expect:**

* All boards get task uploaded in parallel
* Board messages printed to board console
* Buttons “Upload”, “configure”, “Run”, “Upload all” and “Run all” get blocked


### 11. Upload task for all and then cancel by pressing “stop all” button on GUI


**Scenario type:** Success

**Preconditions:**

* Follow step ***Preparing test case***
* Remove subjects ***mxx1***, ***mxx2*** and ***mxx3***

**Workflow:**

1. Expand ***Experiments***
2. Select experiment ***Fox P2 extended***
2. Select option "Upload all"
4. Select option "Stop all"

**What to expect:**

* Operation is aborted for all boards (upload may or not be completed)
* Buttons reset
* Board messages printed to board console
* GUI Message: None

### 12. Upload task for all and then one board stops/fails

**Scenario type:** Error

**Preconditions:**

* Follow step ***Preparing test case***
* Remove subjects ***mxx1***, ***mxx2*** and ***mxx3***

**Workflow:**

1. Expand ***Experiments***
2. Select experiment ***Fox P2 extended***
2. Select option "Upload all"
3. Select option "Stop" or disconnect board in one of the running subjects

**What to expect:**

* Operation is aborted for each board disconnected/stopped (upload may or not be completed)
* Buttons are reset for subject of disconnected board
* Board messages printed to board console
* All other boards get unaffected
* GUI Message: “Problem connecting with board serial port %serialport%” (if it applies)


