# pyControlGUI Test Cases - Board jobs

##  Sync variables for subject

![Sync set variables](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/sync_set_variables.png)

### Resume table

| Test name | Date | Result | Comments |
|---|---|---|---|
| 1. Sync variables (task blinker)
| 2. Sync variables (task left\_poke\_button)
| 3. Board without framework
| 4. Board with framework corrupted
| 5. Subject without task
| 6. Subject without board
| 7. Invalid task
| 8. Board with serial port not available
| 9. Cancel by pressing “stop” button on GUI
| 10. Interrupt board connection
| 11. Refresh variables when changing task

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

### 1. Sync variables (task blinker)

**Scenario type:** Success

**Preconditions:** Follow step ***Preparing test case***

**Worflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m329***
2. Select option "configure"
3. ***Configure task*** window shows up
4. Select option "sync"

**What to expect:**

* Set variables are updated on this subject board
* "States", "Events" and "Set variables" fields get refreshed on GUI
* Board messages printed to board console
* Buttons “upload”, “configure”, “run”, "sync”, “upload all” and “run all” get blocked

![Sync set variables](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/sync_blinker.png)

### 2. Sync variables (task left\_poke\_button)

**Scenario type:** Success

**Preconditions:** Follow step ***Preparing test case***

**Worflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m996***
2. Select option "configure"
3. ***Configure task*** window shows up
4. Select option "sync"

**What to expect:**

* Set variables are updated on this subject board
* "States", "Events" and "Set variables" fields get refreshed on GUI
* Board messages printed to board console
* Buttons “upload”, “configure”, “run”, "sync”, “upload all” and “run all” get blocked

![Sync set variables](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/sync_left_poke_button.png)

### 3. Board without framework

**Scenario type:** Error

**Preconditions:** 

* Follow step ***Preparing test case***
* Manually remove folder ***pyControl*** from pyBoard filesystem (if exists) connected on COM4 (board1)

**Worflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m845***
2. Select option "configure"
3. ***Configure task*** window shows up
4. Select option "sync"

**What to expect:**

* Variables do not get changed
* Board messages printed to board console
* GUI Message: “Please install framework on board”

### 4. Board with framework corrupted

See [issue](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/77/how-to-test-board-with-framework-corrupted).

### 5. Subject without task

**Scenario type:** Error

**Preconditions:** Follow step ***Preparing test case***

**Worflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***mxx1***
2. Select option "configure"
3. ***Configure task*** window shows up
4. Select option "sync"

**What to expect:**

* Variables do not get changed
* Board messages printed to board console
* GUI Message: “Please assign task to subject”


### 6. Subject without board

**Scenario type:** Error

**Preconditions:** Follow step ***Preparing test case***

**Worflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***mxx2***
2. Select option "configure"
3. ***Configure task*** window shows up
4. Select option "sync"

**What to expect:**

* Variables do not get changed
* Board messages printed to board console
* GUI Message: “Please assign board to subject”

### 7. Invalid task

**Scenario type:** Error

**Preconditions:** 

* Follow step ***Preparing test case***
* Alternative: provide any kind of invalid task (examples: task name with spaces, path not found, no set variables defined, task code is empty, etc.)

**Worflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***mxx3***
2. Select option "configure"
3. ***Configure task*** window shows up
4. Select option "sync"

**What to expect:**

* No task uploaded
* Board messages printed to board console
* GUI Message: “Invalid task: %error%”


### 8. Board with serial port not available

**Scenario type:** Error

**Preconditions:** Follow step ***Preparing test case***

**Worflow:**

1. Copy content from task ***blinker2*** to ***task_xx*** 
2. Expand ***Experiments > Fox P2 extended***, select subject ***mxx3***
3. Select option "configure"
4. ***Configure task*** window shows up
5. Select option "sync"

**What to expect:**

* Variables do not get changed
* Board messages printed to board console
* GUI Message: “Board serial port not available: COM243”


### 9. Cancel by pressing “stop” button on GUI

**Scenario type:** Success

**Preconditions:** Follow step ***Preparing test case***

**Worflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m845***
2. Select option "configure"
3. ***Configure task*** window shows up
4. Select option "sync"

**What to expect:**

* Variables may or not get changed
* "States", "Events" and "Set variables" fields get refreshed on GUI
* Board messages printed to board console
* GUI Message: None

### 10. Interrupt board connection

**Scenario type:** Error

**Preconditions:** Follow step ***Preparing test case***

**Worflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m845***
2. Select option "configure"
3. ***Configure task*** window shows up
4. Select option "sync"
5. Interrupt connection: press "reset" button OR disconnect cable OR eject board via software

**What to expect:**

* Variables may or not get changed
* "States", "Events" and "Set variables" fields get refreshed on GUI
* Board messages printed to board console
* GUI Message: “Problem connecting with board serial port %serialport%”

### 11. Refresh variables when changing task

**Scenario type:** Success

**Preconditions:** Follow step ***Preparing test case***

**Worflow:**

1. Expand ***Experiments > Fox P2 extended***, select subject ***m996***
2. Select option "configure"
3. ***Configure task*** window shows up
4. Select option "sync"
5. Change task assignment to ***blinker2***
6. On ***Configure task*** window, select option "sync"

**What to expect:**

* After step 5: set variables names are imediatelly updated ***Configure task*** window
* After step 6: set variables are updated on board
* "States", "Events" and "Set variables" fields get refreshed on GUI
* Board messages printed to board console
* Buttons “upload”, “configure”, “run”, "sync”, “upload all” and “run all” get blocked
