# pyControlGUI Test Cases

## Creating and loading project

Below, we describe test cases for: 

* creating project
* opening project

### Resume table

| Test name | Date | Result | Comments |
|---|---|---|---|
| 1. Create, modify and save project | --- | --- | ---
| 1.1 Create project
| 1.2 Add experiments
| 1.3 Add subjects
| 1.4 Add and import task
| 1.5 Add experimental setup
| 1.6 Quit project
| 2. Open, modify and save project | --- | --- | ---
| 2.1 Modify experiment
| 2.2 Remove experiment
| 2.3 Modify subject
| 2.4 Remove subject
| 2.5 Modify task
| 2.6 Remove task
| 2.7 Modify experimental setup
| 2.8 Remove experimental setup
| 2.9 Assign board to subject
| 2.10 Modify board and task on subject and upload
| 2.11 Remove board and task assignment on subject
| 3. Alternative cases for create project | --- | --- | ---
| 3.1 Create project and cancel (a)
| 3.2 Create project and cancel (b)
| 3.3 Create project when another project is loaded
| 3.4 Create project that already exists on filesystem
| 3.5 Create project with same name when another project is loaded
| 4. Alternative cases for open project | --- | --- | ---
| 4.1 Open project when another project is loaded
| 4.2 Project folder is invalid: file settings.json is missing
| 4.3 Project folder is invalid: main folders are missing: data, frameworks or tasks (all are required)
| 4.4 Settings file is invalid: Invalid fields
| 4.5 Settings file is invalid: Missing fields
| 4.6 Settings file is invalid: File content not in sync with data folder content (example: experiment folder missing)
| 4.7 Settings file is invalid: Setup referencing missing task
| 4.8 Settings file is invalid: Setup referencing missing board
| 4.9 Settings file is invalid: Setup referencing missing subject
| 5. Move project location on filesystem
| 6. Open project with latin characters

### 1. Create, modify and save project

**Scenario type:** Success

**Preconditions:** 

* Create a folder in your desktop called "test\_case\_project"

#### 1.1 Create project

1. Start application
2. Select ***File > New project***
3. Insert project name: ***My project***
4. Select project location: ***Desktop\test\_case\_project***

**What to expect:**

* Created folder structure with settings file:

```
My project
   | data
   | frameworks
   | tasks
   | settings.json
```

#### 1.2 Add experiments

1. Select ***Actions > Add experiment*** (or right-click Experiments)
2. Insert experiment name: ***Fox_p1***
3. Select ***Actions > Add experiment*** (or right-click Experiments)
4. Insert experiment name: ***Fox_p1*** (name exists)
5. Dialog shows up: ***Experiment already exists***. Press ***OK***.
6. Select ***Actions > Add experiment*** (or right-click Experiments)
7. Insert experiment name: ***Experência 2***
8. ~~Select **File > Save project**~~ [already auto saved](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/74/auto-save-project-whenever-a-field-is)

**What to expect:**

* Updated settings file
* New folder content:

```
My project
   | data
      Fox_p1
      Experência 2
   | frameworks
   | tasks
   | settings.json
```

#### 1.3 Add subjects

1. Select ***Fox_p1***
2. Select ***Actions > Add subject*** (or right-click ***Fox_p1***)
3. Insert subject name: ***m239***
4. Select ***Actions > Add subject*** (or right-click ***Fox_p1***)
4. Insert subject name: ***m239*** (name exists)
6. Dialog shows up: ***Subject already exists***. Press ***OK***.
7. Select ***Experência 2***
8. Select ***Actions > Add subject*** (or right-click ***Experência 2***)
9. Insert subject name: ***Subject 1***
10. Select ***Actions > Add subject*** (or right-click ***Experência 2***)
11. Insert subject name: ***m845***
12. Select ***Actions > Add subject*** (or right-click ***Experência 2***)
13. Insert subject name: ***indivíduo 5***

**What to expect:**

* Updated settings file
* New folder content:

```
My project
   | data
      Fox_p1
      |   m239
      Experência 2
      |   Subject 1
      |   m845
      |   indivíduo 5
   | frameworks
   | tasks
   | settings.json
```


#### 1.4 Add and import task

1. Select ***Actions > Add task*** (or right-click Tasks)
2. Insert task name: ***blinker***
3. Copy task content from ***[blinker.py](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/test-cases/samples/blinker.py)***
4. Paste content on task code editor and press ***Save***
5. Close task code editor window
6. Select ***Actions > Add task*** (or right-click Tasks)
7. Insert task name: ***blékãr23***
8. Leave task content empty
9. Close task code editor window
10. Select ***Actions > Add task*** (or right-click Tasks)
11. Insert task name: ***blinker*** (name exists)
12. Dialog shows up: ***Task already exists***. Press ***OK***.
13. Select ***Actions > Add task*** (or right-click Tasks)
14. Insert task name: ***my task*** (name with spaces)
15. Dialog shows up: ***Task name cannot have spaces***. Press ***OK***.
16. Download as file this task example: ***[left\_poke\_button.py](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/test-cases/samples/left_poke_button.py)***
17. Select ***Actions > Import task*** (or right-click Tasks)
18. Select ***left\_poke\_button.py*** location
19. ~~Select **File > Save project**~~ [already auto saved](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/74/auto-save-project-whenever-a-field-is)

**What to expect:**

* Updated settings file
* New folder content:

```
My project
   | data
      Fox_p1
      |   m239
      Experência 2
      |   Subject 1
      |   m845
      |   indivíduo 5
   | frameworks
   | tasks
   |   blékãr23.py
   |   blinker.py
   |   left_poke_button.py
   | settings.json
```

#### 1.5 Add experimental setup

1. Select ***Actions > Add experimental setup*** (or right-click Experimental setups)
2. Insert experimental setup name: ***board1***
3. Select ***Actions > Add experimental setup*** (or right-click Experimental setups)
4. Insert experimental setup name: ***board1*** (name exists)
5. Dialog shows up: ***Experimental setup already exists***. Press ***OK***.
6. Select ***Actions > Add experimental setup*** (or right-click Experimental setups)
7. Insert experimental setup name: ***board 1***
8. Select ***Actions > Add experimental setup*** (or right-click Experimental setups)
9. Insert experimental setup name: ***éxpérimãnt 54***
10. ~~Select **File > Save project**~~ [already auto saved](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/74/auto-save-project-whenever-a-field-is)

**What to expect:**

* Updated settings file
* Folder content unchanged

#### 1.6 Quit project

1. Select ***File > Exit***
2. Press ***Yes***

**What to expect:**

* Updated settings file
* Project window is closed


### 2. Open, modify and save project

**Scenario type:** Success

**Preconditions:** 

* Follow step 1. Create, modify and save project

#### 2.1 Modify experiment

**Preconditions:** Follow step ***1. Create, modify and save project***

1. Start application
2. Select ***File > Open project***
3. Select project location: ***Desktop\test\_case\_project\My project***
4. Select experiment ***Experiência 2***
5. On Details window change experiment name to ***Fox_p1***
6. Dialog shows up: ***Experiment name in use***. Press ***OK***.
7. On Details window change experiment name to ***Fox P2 extended***
8. ~~Select “File > Save project”~~ [already auto saved](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/74/auto-save-project-whenever-a-field-is)

**What to expect:**

* Updated settings file
* New folder content:


```
My project
   | data
      Fox_p1
      |   m239
      Fox P2 extended
      |   Subject 1
      |   m845
      |   indivíduo 5
   | frameworks
   | tasks
   |   blékãr23.py   
   |   blinker.py
   |   left_poke_button.py
   | settings.json
```

#### 2.2 Remove experiment

**Preconditions:** Follow step ***2.1 Modify experiment***

1. Right-click experiment ***Fox_p1***
2. Select option ***Remove experiment***
3. Dialog shows up: ***Remove experiment: Fox_p1?***. Press ***yes***
4. ~~Select “File > Save project”~~ [already auto saved](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/74/auto-save-project-whenever-a-field-is)

**What to expect:**

* Updated settings file
* New folder content:

```
My project
   | data
      Fox P2 extended
      |   Subject 1
      |   m845
      |   indivíduo 5
   | frameworks
   | tasks
   |   blékãr23.py
   |   blinker.py
   |   left_poke_button.py
   | settings.json
```

#### 2.3 Modify subject (setup)

**Preconditions:** Follow step ***2.2 Remove experiment***

1. Under ***Fox P2 extended***, select subject ***Subject 1***
2. On Details window change subject name to ***m845***
3. Dialog shows up: ***Subject name in use***. Press ***OK***.
4. Under ***Fox P2 extended***, select subject ***Subject 1***
2. On Details window change subject name to ***m329***
3. ~~Select “File > Save project”~~ [already auto saved](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/74/auto-save-project-whenever-a-field-is)

**What to expect:**

* Updated settings file
* New folder content:


```
My project
   | data
      Fox P2 extended
      |   m329
      |   m845
      |   indivíduo 5
   | frameworks
   | tasks
   |   blékãr23.py
   |   blinker.py
   |   left_poke_button.py
   | settings.json
```

#### 2.4 Remove subject (setup)

**Preconditions:** Follow step ***2.3 Modify subject (setup)***

1. Under ***Fox P2 extended***, right-click subject ***indivíduo 5***
2. Select option ***Remove subject***
3. Dialog shows up: ***Remove suject: indivíduo 5?***. Press ***yes***
4. ~~Select “File > Save project”~~ [already auto saved](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/74/auto-save-project-whenever-a-field-is)

**What to expect:**

* Updated settings file
* New folder content:


```
My project
   | data
      Fox P2 extended
      |   m329
      |   m845
   | frameworks
   | tasks
   |   blékãr23.py
   |   blinker.py
   |   left_poke_button.py
   | settings.json
```

#### 2.5 Modify task

**Preconditions:** Follow step ***1. Create, modify and save project***

1. Expand ***Tasks***, select task ***blinker***
2. On Details window change task name to ***left\_poke\_button***
3. Dialog shows up: ***Task name in use***. Press ***OK***.
4. On Details window change task name to ***blinker2***
5. Double-clik ***blinker2*** (or press ***Edit source code***)
6. On functions ***LED_on*** and ***LED_off*** change 0.3 to 0.5 and 0.7 to 0.5 respectively
7. Press ***Save***

**What to expect:**

* Under project tasks folder, old task file ***blinker*** renamed to ***blinker2***
* New ***blinker2*** file content updated
* Updated assignments on related subjects **(NOT IMPLEMENTED YET)**
* New folder content:

```
My project
   | data
      Fox P2 extended
      |   m329
      |   m845
   | frameworks
   | tasks
   |   blékãr23.py
   |   blinker2.py
   |   left_poke_button.py
   | settings.json
```


#### 2.6 Remove task

**Preconditions:** Follow step ***2.5 Modify task (setup)***

1. Expand ***Tasks***, select task ***blékãr23***
2. Select option ***Remove task***
3. Dialog shows up: ***Remove task: blékãr23?***. Press ***yes***

**What to expect:**

* Under project tasks folder, task file ***blékãr23*** no longer exists (moved to trash)
* Updated assignments on related subjects **(NOT IMPLEMENTED YET)**
* New folder content:

```
My project
   | data
      Fox P2 extended
      |   m329
      |   m845
   | frameworks
   | tasks
   |   blinker2.py
   |   left_poke_button.py
   | settings.json
```

#### 2.7 Modify experimental setup

**Preconditions:** Follow step ***1. Create, modify and save project***

1. Expand ***Experimental setups***, select board ***board 1***
2. On Details window change experimental setup name to ***board1***
3. Dialog shows up: ***Experimental setup name in use***. Press ***OK***.
4. On Details window change experimental setup name to ***board 2***
5. ~~Select “File > Save project”~~ [already auto saved](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/74/auto-save-project-whenever-a-field-is)

**What to expect:**

* Updated settings file
* Updated assignments on related subjects **(NOT IMPLEMENTED YET)**


#### 2.8 Remove experimental setup

**Preconditions:** Follow step ***2.7 Modify experimental setup***

1. Expand ***Experimental setups***
2. Right-click experimental setup ***éxpérimãnt 54***
2. Select option ***Remove experimental setup***
3. Dialog shows up: ***Remove experimental setup: éxpérimãnt 54?***. Press ***yes***
4. ~~Select “File > Save project”~~ [already auto saved](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/74/auto-save-project-whenever-a-field-is)

**What to expect:**

* Updated settings file
* Updated assignments on related subjects **(NOT IMPLEMENTED YET)**

#### 2.9 Assign board to subject

**Preconditions:** Follow step ***2.7 Modify experimental setup***

1. Expand ***Experiments > Fox P2 extended***
2. Select ***m845***
3. On Details window, in ***Board / Task table*** select ***+*** option
4. Dialog shows up: ***Assign board and task***.
5. On ***Select board***, choose **board 2**
6. Press ***OK***
7. On Details window, select ***Upload*** option
8. Dialog shows up: ***Please assign task to subject first***.
9. Press ***OK***
10. ~~Select “File > Save project”~~ [already auto saved](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/74/auto-save-project-whenever-a-field-is)


**What to expect:**

* No task uploaded
* Updated settings file with new assignment

```
{
    "boards":[
        [
            "board 2",
            ""
        ]
    ],
    "setup_id":"m845",
    "subjects":[
        "m845"
    ]
}
```

#### 2.10 Modify board and task on subject and upload

**Preconditions:** Follow step ***2.9.1 Modify experimental setup***

1. Expand ***Experiments > Fox P2 extended***
2. Select ***m845***
3. On Details window, in ***Board / Task table*** select ***+*** option
4. Dialog shows up: ***Assign board and task***.
5. On ***Select board***, choose **board1**
6. On ***Select task***, choose **blinker**
7. Press ***OK***
8. On Details window, select ***Upload*** option
9. ~~Select “File > Save project”~~ [already auto saved](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/74/auto-save-project-whenever-a-field-is)

**What to expect:**

* Task was uploaded to board (button state reset)
* Updated settings file with new assignment

```
{
    "boards":[
        [
            "board1",
            "blinker"
        ]
    ],
    "setup_id":"m845",
    "subjects":[
        "m845"
    ]
}
```

#### 2.11 Remove board and task assignment on subject

**Preconditions:** Follow step ***2.9.2 Modify board and task on subject***

1. Expand ***Experiments > Fox P2 extended***
2. Select ***m845***
3. On Details window, in ***Board / Task table*** select ***-*** option
9. ~~Select “File > Save project”~~ [already auto saved](https://bitbucket.org/fchampalimaud/pycontrol-gui/issues/74/auto-save-project-whenever-a-field-is)

**What to expect:**

* Updated settings file

```
{
    "boards":[],
    "setup_id":"m845",
    "subjects":[
        "m845"
    ]
}
```

### 3. Alternative cases for create project

### 3.1 Create project and cancel (a)

**Scenario type:** Success

**Precondition:** There are no projects loaded

**Worflow:**

1. Start application
2. Select “File > New project”
3. Cancel

**What to expect:**

* No folder is created
* Project not loaded on GUI

#### 3.2 Create project and cancel (b)

**Scenario type:** Success

**Precondition:** There are no projects loaded

**Worflow:**

1. Start application
2. Select “File > New project”
2. Insert project name
3. Cancel

**What to expect:**

* No folder is created
* Project not loaded on GUI

#### 3.3 Create project when another project is loaded

**Scenario type:** Success

**Precondition:** There is one project already loaded

**Worflow:**

1. Start application
2. Select “File > New project”
2. Insert project name
3. Select folder
4. Confirm

**What to expect:**

* All current windows are closed
* Current project is saved and closed
* New folder with project name created on specified path
* Project folder content: “data” (folder), “tasks” (folder), “frameworks” (folder), settings.json (text file) 
* Project is loaded on GUI with nodes: “Experiments”, “Tasks”, “Experimental setups”

#### 3.4 Create project that already exists on filesystem

**Scenario type:** Error

**Preconditions:** 

* There are no projects loaded
* There is one project (folder) on filesystem named "My project"

**Worflow:**

1. Start application
2. Select “File > New project”
2. Insert project name ("My project")
3. Select project parent folder (where inside there is already a folder named "My project")
4. Confirm


**What to expect:**

* Show info message to user on GUI
* No folder is created
* Project not loaded on GUI

#### 3.5 Create project with same name when another project is loaded


**Scenario type:** Error

**Precondition:** There is one project already loaded with name "My project"

**Worflow:**

1. Start application
2. Select “File > New project”
3. Insert project name (“My project”)
4. Select folder
5. Confirm

**What to expect:**

* Show info message to user on GUI
* No folder is created
* New project not loaded on GUI 
* Previously loaded project is not affected

### 4. Alternative cases for open project

#### 4.1 Open project when another project is loaded

**Scenario type:** Success

**Precondition:** There is one project already loaded

**Worflow:** See 7. Open project

**What to expect:**

* All current windows are closed
* Current project is saved and closed
* Project is loaded on GUI with nodes: “Experiments”, “Tasks”, “Experimental setups”
* All fields in settings.json are correctly loaded

#### 4.2 Project folder is invalid: file settings.json is missing

**Scenario type:** Error

**Worflow:** See 7. Open project

**What to expect:**

* Project is loaded on GUI with nodes: “Experiments”, “Tasks”, “Experimental setups”
* All fields in settings.json are correctly loaded

#### 4.3 Project folder is invalid: main folders are missing: "data", "frameworks" or "tasks" (all are required)

**Scenario type:** Error

**Worflow:** See 7. Open project

**What to expect:**

* Project is loaded on GUI with nodes: “Experiments”, “Tasks”, “Experimental setups”
* All fields in settings.json are correctly loaded

#### 4.4 Settings file is invalid: Invalid fields

**Scenario type:** Error

**Worflow:** See 7. Open project

**What to expect:**

* Project is loaded on GUI with nodes: “Experiments”, “Tasks”, “Experimental setups”
* All fields in settings.json are correctly loaded

#### 4.5 Settings file is invalid: Missing fields

**Scenario type:** Error

**Worflow:** See 7. Open project

**What to expect:**

* ???
* GUI message:


#### 4.6 Settings file is invalid: File content not in sync with "data" folder content (example: experiment folder missing)

**Scenario type:** Error

**Worflow:** See 7. Open project

**What to expect:**

* ???
* GUI message:

#### 4.7 Settings file is invalid: Setup referencing missing task

**Scenario type:** Error

**Worflow:** See 7. Open project

**What to expect:**

* ???
* GUI message:

#### 4.8 Settings file is invalid: Setup referencing missing board

**Scenario type:** Error

**Worflow:** See 7. Open project

**What to expect:**

* ???
* GUI message:

#### 4.9 Settings file is invalid: Setup referencing missing subject

**Scenario type:** Error

**Worflow:** See 7. Open project

**What to expect:**

* ???
* GUI message:


### 5 Move project location on filesystem

**Scenario type:** Success

**Preconditions:** Original project location is changed.

**Worflow:** See 7. Open project

**What to expect:**

* Project is loaded without problems



#### 6 Save project (no write permission)

**Scenario type:** Error

**Preconditions:** Project folders have latin characters OR settings.json has latin characters

**Worflow:** See 12. Save project

**What to expect:**

* Project is loaded without problems


