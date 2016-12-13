# Demonstration project - Simple blink Task

In this very basic example, we can see how to blink a LED on the pyBoard using the pyControl GUI.


## 1. Create entities

**Note**: if you already know how to create entities you can jump directly to section 2.

### 1.1. Create project

1. Start application
2. Select ***File > New project***
3. Insert project name: ***my\_simple\_blink***
4. Select project location: ***Desktop\test\_case***

![new_project_menu.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/new_project_menu.png)

![new_project_name.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/new_project_name.png)

![new_project_target_parent_folder.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/new_project_target_parent_folder.png)

### 1.2. Add experiment

1. Start application
2. Select ***File > Open project***
3. Select project location: ***Desktop\test\_case\my\_simple\_blink***
4. Select ***Actions > Add experiment*** (or right-click Experiments)
5. Insert experiment name: ***Fox_p1***

![add_experiment_menu.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/add_experiment_menu.png)

![add_experiment_name.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/add_experiment_name.png)

### 1.3. Add subject

1. Select experiment ***Fox_p1***
2. Select ***Actions > Add subject*** (or right-click ***Fox_p1***)
3. Insert subject name: ***m111***

![add_subject_menu.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/add_subject_menu.png)

![add_subject_name](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/add_subject_name.png)

### 1.4. Add task

1. Select ***Actions > Add task*** (or right-click Tasks)
2. Insert task name: ***simple_blink***
3. Copy task content from ***[simple_blink.py](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink/simple_blink.py)***
4. Paste content on task code editor and press ***Save***
5. Close task code editor window

![add_task_menu.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/add_task_menu.png)

![add_task_name.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/add_task_name.png)

![add_task_save.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/add_task_save_2.png)

#### Tasks general rules

Each task is composed of:

* A list of states
* A list of events
* A variable to indicate initial state
* Zero or more auxiliar variables
* A function for each declared state (this function always receive an event)
* A set of auxiliar functions (optional)

**Useful tips**:

* Use the special "hw" object which is useful to invoke operations related to hardware. 
* Import the pyControl.utility module that offers several useful operations.
* You can directly use functions from the pyBoard framework ([pyb module](http://docs.micropython.org/en/latest/pyboard/library/pyb.html))

For more information on task and framework concepts, please refer to [basic_concepts](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/basic_concepts).


#### Simple blink task explained

The only thing that simple\_blink.py script does is to switch on and off the internal LED availalbe in the pyBoard. As you can see, there are only 2 states - **LED\_ON** and **LED\_off** - and one event - **timer\_evt**. This event is already offered by the PyControl framework, and counts time using cpu interrupts.

We set 2 auxiliar variables - **v.period\_on** and **v.period\_off** - which define the timer duration (in ms).

Finally, we use the **goto** special function to perform state transitions.




### 1.5. Add experimental setup (board)

1. Select ***Actions > Add experimental setup*** (or right-click Experimental setups)
2. Insert experimental setup name: ***board1***
4. Close application

![add_experimental_setup_menu.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/add_experimental_setup_menu.png)

![add_experimental_setup_name.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/add_experimental_setup_name.png)


## 2. Prepare subject to run task

Open project [my\_simple\_blink](https://bitbucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/my_simple_blink.zip).

### 2.1. Install framework on experimental setup (board)

1. Expand ***Experimental setups***, select experimental setup ***board1***
2. Define desired serial port
2. Select option "Install framework"
3. The console for this experimental setup automatically opens
3. A confirmation message will show up in the experimental setup console if framework is installed with success

![board_install_framework.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/board_install_framework.png)

### 2.2 Assign experimental setup and task to subject

1. Expand ***Experiments > FoxP1***, select subject ***m111***
3. On Details window, in ***Board / Task table*** select ***+*** option
4. Dialog shows up: ***Assign board and task***.
5. On ***Select experimental setup***, choose **board1**
6. On ***Select task***, choose **simple\_blink**
6. Press ***OK***

![subject_assign.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/subject_assign.png)

### 2.3 Sync task variables (upload task)

1. Expand ***Experiments > FoxP1***, select subject ***m111***
2. Select option "configure"
3. ***Configure task*** window shows up
4. Select option "sync"

*Note: this action will both upload task and sync task variables.*

*Note2: alternatively, you can only upload task using "upload" button.*

![task_sync.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/task_sync.png)

### 2.4 Run task

1. Expand ***Experiments > FoxP1***, select subject ***m111***
2. Select option "Run"
3. Expand ***Subject m111*** and select the bottom session (most recent one)
4. Right-click on session to open file (RAW data) or load available plugins (e.g. Trials plot)

*Note: this action will both upload and run task.*

![session_options.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/session_options.png)

![session_raw_data.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/session_raw_data.png)

![session_run.png](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/tutorials/simple_blink_demonstration/session_run.png)