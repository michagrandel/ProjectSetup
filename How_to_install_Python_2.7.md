# How to install Python 2.7.x on Windows

First, download the [latest version of Python 2.7][python].
 
The Windows version is provided as an **MSI package**. To install it manually,
just double-click the file. If asked, please let the Setup set your
**PATH** variable accordingly.

By design, Python installs to a directory with the version number embedded,
e.g. **Python version 2.7** will install at `C:\Python27\`, so that you can have
multiple versions of Python on the same system without conflicts.

## Setting the PATH

Of course, only one interpreter can be the default application for Python file types.
It also does not automatically modify the **PATH** environment variable, so that you
always have control over which copy of Python is run.

Typing the full path name for a Python interpreter each time quickly gets tedious,
so add the directories for your default Python version to the **PATH**. Assuming that
your Python installation is in `C:\Python27\`, add this to your **PATH**:

`C:\Python27\;C:\Python27\Scripts\`

You can do this easily by running the following in powershell:

`[Environment]::SetEnvironmentVariable("Path", "C:\Python27\;C:\Python27\Scripts\;$env:Path", "User")`

This is also an option during the installation process.

The second (Scripts) directory receives command files when certain packages 
are installed, so it is a very useful addition. You do not need to install or 
configure anything else to use Python.

[python]: https://www.python.org/downloads/