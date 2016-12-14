# Contributing to pyControl

An introduction to contributing to the pyControl project.

The pyControl project welcomes, and depends, on contributions from developers and
users in the open source community. Contributions can be made in a number of
ways, a few examples are:

- Code patches via pull requests
- Documentation improvements
- Bug reports and patch reviews

## Code of Conduct

Everyone interacting in the pyControl project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the [PyPA Code of Conduct].

## Reporting an Issue

Please include as much detail as you can. Let us know your platform and pyControl
version. If the problem is visual (for example a theme or design issue) please
add a screenshot and if you get an error please include the full error and
traceback.

## Testing the Development Version

If you want to just install and try out the latest development version of
pyControl you can do so following the steps on the [source-code-installation](/user-guide/source-code-installation.md) page. This can be useful if you
want to provide feedback for a new feature or want to confirm if a bug you
have encountered is fixed in the git master.

## Installing for Development

pyControl is composed of several independent packages in order to achieve better flexibility and maintenance. You can find detailed documentation for all these projects below.

#### External libraries

|Name|Description|
|---|---|
|pysettings [readthedocs](https://pysettings.readthedocs.io/en/latest/) [github](https://github.com/UmSenhorQualquer/pysettings)| Python library to provide settings files for modular applications |
|pyForms [readthedocs](https://pyforms.readthedocs.io/en/latest/) [github](https://github.com/UmSenhorQualquer/pyforms)| Python layer of Windows forms, based on PyQT and OpenGL |
|pyforms-generic-editor [readthedocs](http://pyforms-generic-editor.readthedocs.io/en/latest/) [bitbucket](https://bitbucket.org/fchampalimaud/pyforms-generic-editor) | Easy way to bootstrap projects that make use of pyForms |
|pyserial [readthedocs](https://pyserial.readthedocs.io/en/latest/) [github](https://github.com/pyserial/pyserial)| Python serial port access library | 
|Send2Trash [github](https://github.com/hsoft/send2trash)| Python library to natively send files to Trash (or Recycle bin) on all platforms. |

#### pyControl Framework and Command Line Interface (CLI)

|Library name|Description| mercurial link |
|---|---|---|
|pyControl framework [wiki](https://bitbucket.org/takam/pycontrol/wiki/Home) [bitbucket](https://bitbucket.org/takam/pycontrol/wiki/Home)| CLI and framework| https://bitbucket.org/takam/pycontrol |

<!---
|[pyControl framework](https://pycontrol-framework.readthedocs.org/)| CLI and framework|
-->

#### pyControl Graphical User Interface (GUI)

|Library name|Description| git link |
|---|---|---|
|pycontrol-gui [readthedocs](https://pycontrol-gui.readthedocs.org/) [bitbucket](https://bitbucket.org/fchampalimaud/pycontrol-gui)|Main graphical user interface package| https://bitbucket.org/fchampalimaud/pycontrol-gui.git |
|pycontrol-api [readthedocs](https://pycontrol-api.readthedocs.org/) [bitbucket](https://bitbucket.org/fchampalimaud/pycontrol-api)| pyControl API| https://bitbucket.org/fchampalimaud/pycontrol-api.git |
|pyboard-communication [readthedocs](https://pyboard-communication.readthedocs.org/) [bitbucket](https://bitbucket.org/fchampalimaud/pyboard-communication)| Communication with pyBoard | https://bitbucket.org/fchampalimaud/pyboard-communication.git |

#### pyControl GUI Plugins

|Library name|Description| git link |
|---|---|---|
|pycontrol-gui-welcome [src](https://readthedocs.org/projects/pycontrol-gui-plugin-welcome)|Show a welcome window at startup| https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-welcome.git |
|pycontrol-gui-plugin-session-log [src](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-session-log)|Window to visualise the session log.| https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-session-log.git |
|pycontrol-gui-plugin-session-broadcast [src](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-session-broadcast)|Broadcast all states and events to an external application (check Cube app in the Other examples section)| https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-session-broadcast.git |
|pycontrol-gui-plugin-terminal [src](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-terminal)|Control the GUI interface using terminal commands.| https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-welcome.git |
|pycontrol-gui-plugin-timeline [src](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-timeline)|Visualise in a timeline the sequence of states that are happening in the moment.| https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-timeline.git |
|pycontrol-gui-plugin-experiment-macros [src](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-experiment-macros)|Execute macros if an state occurs.| https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-experiment-macros.git |
|pycontrol-gui-plugin-export-code [src](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-export-code)|Generate code to the API automatically.| https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-export-code.git |
|pycontrol-gui-plugin-remote-project [src](https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-remote-project)|Control a project running on a remote host.| https://bitbucket.org/fchampalimaud/pycontrol-gui-plugin-remote-project.git |

### Step-by-step installation for running GUI

#### Install python3 and PyQt (with QScintilla2) environments


#### Download GUI libraries sources from git

To develop for pyControl GUI, you will need "pyboard-communication", "pycontrol-api" and "pycontrol-gui" libraries sources.

    # folder pyboard-communication is created
    git clone https://bitbucket.org/fchampalimaud/pyboard-communication.git
     
    # folder pycontrol-api is created
    git clone https://bitbucket.org/fchampalimaud/pycontrol-api.git
    
    # folder pycontrol-gui is created
    git clone https://bitbucket.org/fchampalimaud/pycontrol-gui.git
    
### Install required libraries

On the command line, navigate inside the pycontrol-gui folder. You will find a "requirements.txt" file.
To install requirements, run pip as this:

    cd pycontrol-gui
    pip3 install -r requirements.txt --upgrade
    
This file assumes that "pyboard-communication" and "pycontrol-api" sources are on the parent folder. You should expect the following directory structure:

    | pyboard-communication
       | pyboard-communication
       | ...
    | pycontrol-api
       | pycontrolapi
       | ...
    | pycontrol-gui
       | pycontrolgui
       | requirements.txt
       | ...

#### Download and configure pycontrol framework

1. Download pycontrol-framework source code from [here](https://bitbucket.org/takam/pycontrol/get/37fd9d1d22fd.zip) and unzip it (you should see a pyControl folder).
2. Inside the pycontrol-gui folder, locate the file "user_settings.py.template". Make a copy and change the name for "user_settings.py".
3. Open the file "user_settings.py".
4. Change the variable value **PYCONTROLAPI_PYCONTROL_PATH** to point to the folder "pyControl" inside the pycontrol-framework project just downloaded
5. Change the variable value **PYCONTROLAPI_DEVICES_PATH** to point to the folder "devices" inside the pycontrol-framework project just downloaded

Folder structure should look like these:

    | pycontrol-gui
       | pycontrolgui
       | requirements.txt
       | user_settings.py.template
       | user_settings.py
       | ...
       
    | pyControl
       | devices
       | examples
       | host
       | license
       | pyControl
       | ...


### Run project
On the command line, navigate inside the pycontrol-gui folder.
Run the following command:
    
    python3 -m pycontrolgui


## Submitting Pull Requests

Once you are happy with your changes or you are ready for some feedback, push
it to your fork and send a pull request. For a change to be accepted it will
most likely need to have tests and documentation if it is a new feature.

## Final note
This guide was based on the MKdocs project documentation.

[MkDocs]: http://www.mkdocs.org
[PyPA Code of Conduct]: https://www.pypa.io/en/latest/code-of-conduct/
