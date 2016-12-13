# pyControlGUI Test Cases - Board jobs

##  Install framework

![Installing framework](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/media/install_framework.png)

### Resume table

| Test name | Date | Result | Comments |
|---|---|---|---|
| 1. Fresh install (board without framework)
| 2. Re-install framework
| 3. Cancel by pressing “stop” button on GUI
| 4. Interrupt board connection
| 5. Framework invalid path
| 6. Invalid framework
| 7. Serial port not available

### Preparing test case

1. Download project sample [My project - step 2.zip](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/test-cases/samples/my-project-step2.zip) and unzip folder
2. Connect a pyBoard and find out serial port name (example on UNIX: /dev/tty.usbmodem1233, example on Windows: COM4)
3. Manually remove folder ***pyControl*** from pyBoard filesystem (if exists)
4. Start ***pyControlGUI***
5. Select ***File > Open project***
6. Choose ***My project - step 2*** example
7. Expand ***Experimental setups***, select experimental setup ***board 2***
8. On Details window fill in ***Serial port*** field with ***COM4***
9. On Details window fill in ***Framework name*** field with ***breakout\_1\_0*** (this framework is already provided on ***My project - step 2*** example)
10. ~~Select “File > Save project”~~ [already auto saved](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/74/auto-save-project-whenever-a-field-is)

NB: For this test case we will consider ***COM4*** serial port name.

### 1. Fresh install (board without framework)

**Scenario type:** Success

**Preconditions:** Follow step ***Preparing test case***

**Worflow:**

1. Expand ***Experimental setups***, select experimental setup ***board 2***
2. Select option "Install framework"

**What to expect:**

* New framework is uploaded
* Board messages printed to board console
* Button “install framework” changes to "stop" while running job
* GUI Message: None
* pyBoard filesystem now contains a folder named ***pyControl***

### 2. Re-install framework

**Scenario type:** Success

**Preconditions:** Follow step 1. Fresh install (board without framework)

**Worflow:**

1. Expand ***Experimental setups***, select experimental setup ***board 2***
2. Select option "Install framework"

**What to expect:**

* New framework overrides old framework
* Old framework is always deleted even if it has the same name
* Board messages printed to board console
* Button “install framework” changes to "stop" while running job
* GUI Message: None

### 3. Cancel by pressing “stop” button on GUI

**Scenario type:** Success

**Preconditions:** Follow step ***Preparing test case***

**Worflow:**

1. Expand ***Experimental setups***, select experimental setup ***board 2***
2. Select option "Install framework"

**What to expect:**

* Framework may or may not be installed
* Board messages printed to board console
* Button “install framework” is reset
* GUI Message: None

### 4. Interrupt board connection

**Scenario type:** Error

**Preconditions:** Follow step ***Preparing test case***

**Worflow:**

1. Expand ***Experimental setups***, select experimental setup ***board 2***
2. Select option "Install framework"
4. There is some failure on board (examples: user presses board reset button, cable is disconnected, etc.)

**What to expect:**

* Framework may or may not be installed
* Board messages printed to board console
* Button “install framework” is reset
* GUI Message: “Problem connecting with board serial port %serialport%”

### 5. Framework invalid path

**Scenario type:** Error

**Preconditions:** Follow step 1. Fresh install (board without framework)

**Worflow:**

1. Expand ***Experimental setups***, select experimental setup ***board 2***
2. On Details window fill in ***Framework name*** field with ***breakout\_1\_1*** (this framework does not exists under ***frameworks*** project folder)
3. Select option "Install framework"

**What to expect:**

* Current board framework gets untouched
* Board messages printed to board console
* Button “install framework” is reset
* GUI Message: "Framework path not found: %framework_path%"

### 6. Invalid framework

**Scenario type:** Error

**Preconditions:**

* There is a pyBoard available on serial port ***COM4***
* ***board 2*** is assigned to serial port ***COM4***
* Create an invalid framework (examples: no “pyControl” folder inside, "pyControl" folder empty, etc.)

**Worflow:**

1. Expand ***Experimental setups***, select experimental setup ***board 2***
2. Select option "Install framework"

**What to expect:**

* Board gets without any framework installed (old framework was removed)
* Board messages printed to board console
* Button “install framework” is reset
* GUI Message: "Framework invalid: %error_message%"

### 7. Serial port not available

**Scenario type:** Error

**Preconditions:** 

* Follow step ***Preparing test case***
* Serial port COM5 is not available

**Worflow:**

1. Expand ***Experimental setups***, select experimental setup ***board 2***
2. On Details window fill in ***Serial port*** field with ***COM5***
3. Select option "Install framework"

**What to expect:**

* Current board framework gets untouched
* Board messages printed to board console
* Button “install framework” is reset
* GUI Message: “Board serial port not available: %serialport%”


