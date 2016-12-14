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

pyControl is composed of several independent packages in order to achieve better flexibility and maintenance. To develop for pyControl, you will need to:

* Install python3 and PyQt (with QScintilla2) environments
* Install external dependencies
* Install pycontrol framework package
* Install GUI packages
* Install GUI plugins (optional)

In order to make changes, you should fork and download all pyControl family packages. You can find detailed documentation for all these projects below.

### Framework and Command Line Interface (CLI)

|Name|Description|
|---|---|
|[pyControl framework](https://bitbucket.org/takam/pycontrol/wiki/Home)| CLI and framework|

<!---
|[pyControl framework](https://pycontrol-framework.readthedocs.org/)| CLI and framework|
-->

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



## Submitting Pull Requests

Once you are happy with your changes or you are ready for some feedback, push
it to your fork and send a pull request. For a change to be accepted it will
most likely need to have tests and documentation if it is a new feature.

## Final note
This guide was based on the MKdocs project documentation.

[MkDocs]: http://www.mkdocs.org
[PyPA Code of Conduct]: https://www.pypa.io/en/latest/code-of-conduct/
