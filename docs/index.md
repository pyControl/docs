# pyControl

**Open source, Python based, behavioural experiment control.**

![run_task_GUI.jpg](media/GUI/run_task_tab.png)

## Overview

pyControl is a system of open source hardware and software for controlling behavioural experiments in neuroscience and psychology, built around the [Micropython](https://micropython.org/) microcontroller.

pyControl makes it easy to program complex behavioural tasks using a clean, intuitive, and flexible syntax for specifying tasks as state machines. User created task definition files, written in Python, run directly on the microcontroller, supported by pyControl framework code.  This gives users the power and simplicity of Python for specifying task behaviour, while allowing low-level access to the microcontroller hardware directly from task code.  For more information see [programming tasks](user-guide/programming-tasks.md).


pyControl has a [Graphical User Interface](user-guide/graphical-user-interface.md) for controlling experiments and visualing behaviour.

Tools for importing pyControl data into Python for analysis are provided in the [data_import](user-guide/pycontrol-data.md) module.

![Hardware overview](media/hardware/hardware-overview.png)


pyControl [hardware](user-guide/hardware.md) consists of a breakout board and a set of devices such as nose-pokes, audio boards, LED drivers, rotary encoders and stepper motor controllers that are connected to the breakout board to create behavioural setups.  Assembled pyControl hardware is available from the [OpenEphys store :material-cart:](#){ .md-button }.

pyControl hardware, software and documentation repositories are on [GitHub :octicons-mark-github-16:](https://github.com/pyControl){ .md-button }.

The pyControl [manuscript :material-newspaper-variant-outline:](https://www.biorxiv.org/content/10.1101/2021.02.22.432227v1){ .md-button } gives a high level overview of the system design and it's rationale and has validation experiments and example use cases.  If you use pyControl in a publication, please cite it.

If you do fiber photometry experiments, you may be interested in pyControl's sister project [pyPhotometry](https://pyphotometry.readthedocs.io){ .md-button }.

## Support

If you encounter problems take a look at the [troubleshooting](user-guide/troubleshooting.md) page or contact the [Google Group :material-forum:](https://groups.google.com/forum/#!forum/pycontrol){ .md-button }

## Developer's guide

Do you want to contribute for the pyControl project? We'd love your help! You can find more information [here](/contributing).
