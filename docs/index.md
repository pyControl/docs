# pyControl

Controlling behavioural experiments using Micropython.

---

## Overview

**pyControl** is a system of software and hardware for controlling behavioural experiments based around the Micropython microcontroller.

![pyControlGUI frontpage](https://bytebucket.org/fchampalimaud/pycontrol-gui/wiki/media/pycontrol-gui-frontpage.png)

---

## Installation

**PyControlGUI** is distributed as a standalone executable for Mac and Windows but source code installation is also possible under Linux.

| Type | Description |
|---|---|
|[Binaries](https://bitbucket.org/fchampalimaud/pycontrol-gui/downloads)| Download binaries for Mac OS and Windows (**recommended**)
| [Source code installation](user-guide/souce-code-installation/) | Source code installation step by step

## Documentation

### Framework and Command Line Interface (CLI)

|Name|Description|
|---|---|
|[pyControl framework](https://pycontrol-framework.readthedocs.org/)| CLI and framework|

### Graphical User Interface (GUI)

|Name|Description|
|---|---|
|[pyControl GUI](https://pycontrol-gui.readthedocs.org/)|Main graphical user interface package|
|[pyControl API](https://pycontrol-api.readthedocs.org/)| pyControl API|
|[pyBoard communication API](https://pyboard-communication.readthedocs.org/)| Communication with pyBoard |

### GUI Plugins

|Name|Description|
|---|---|
|[Welcome window](https://readthedocs.org/projects/pycontrol-gui-welcome)|Show a welcome window at startup|
|[Session log](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-session-log)|Window to visualise the session log.|
|[Session TPC/IP Broadcast](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-session-broadcast)|Broadcast all states and events to an external application (check Cube app in the Other examples section)|
|[Terminal](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-terminal)|Control the GUI interface using terminal commands.|
|[Session timeline](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-timeline)|Visualise in a timeline the sequence of states that are happening in the moment.|
|[Experiment macros](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-export-code)|Execute macros if an state occurs.|
|[Project 2 code](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-export-code)|Generate code to the API automatically.|
|[Remote project](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-remote-project)|Control a project running on a remote host.|

### Other libraries

|Name|Description|
|---|---|
|[pysettings](http://pyforms.readthedocs.io/en/latest/)| pysettings|
|[pyForms](http://pyforms.readthedocs.io/en/latest/)|pyForms|
|[pyforms-generic-editor](http://pyforms-generic-editor.readthedocs.io/en/latest/)| pyforms-generic-editor |
|[pyserial](http://pyserial.readthedocs.io/en/latest/)| pyserial |
|[Send2Trash](http://Send2Trash.readthedocs.io/en/latest/)| Send2Trash |
