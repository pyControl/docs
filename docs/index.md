# pyControl

Open source, Python based, behavioural experiment control.

---

## Overview

**pyControl** is a system of open source [hardware](user-guide/hardware.md) and software for controlling behavioural experiments, built around the [Micropython](https://micropython.org/) microcontroller.

pyControl makes it easy to program complex behavioural tasks using a clean, intuitive, and flexible syntax for specifying tasks as state machines. The user created task definition files, written in Python, run directly on the microcontroller, supported by pyControl framework code.  This gives users the power and simplicity of Python for specifying task behaviour, while allowing advanced users low-level access to the microcontroller hardware.  For more information see [programming tasks](user-guide/programming-tasks.md).  

pyControl is available both as a [Graphical User Interface](user-guide/graphical-user-interface.md) (GUI) and as a [Command Line Interface](user-guide/command-line-interface.md) (CLI). 

The pyControl [google group](https://groups.google.com/forum/#!forum/pycontrol) is a email list for pyControl users.

![pyControlGUI frontpage](media/pycontrol-gui-frontpage.png)

---

## Download

The GUI is distributed as a standalone executable for Mac and Windows. Source code installation is also possible under Linux.  

The CLI is downloaded as a zip file, setup instructions are provided in the user guide.

| Type | Description |
|---|---|
|[pycontrolGUI installer](https://bitbucket.org/fchampalimaud/pycontrol-gui/downloads)| Download binaries for Mac OS and Windows (**recommended**)|
|[Source code installation (GUI)](http://pycontrol-gui.readthedocs.io/en/latest/)  | Refer to the pycontrol-gui documentation. |
|[Download zip (CLI)](https://bitbucket.org/takam/pycontrol/downloads/) | Refer to the [CLI user guide](user-guide/command-line-interface.md). |

## Developer's guide

Do you want to contribute for the pyControl project? You can find more information [here](/contributing).