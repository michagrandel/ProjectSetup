# ProjectSetup

[![PythonVersions](https://img.shields.io/pypi/pyversions/ProjectSetup.svg)](http://pypi.python.org)
[![Travis](https://img.shields.io/travis/michagrandel/ProjectSetup/master.svg)](https://travis-ci.org/michagrandel/ProjectSetup)
![Coverage](https://img.shields.io/codecov/c/github/michagrandel/ProjectSetup/master.svg)
[![GitHub release](https://img.shields.io/github/release/michagrandel/ProjectSetup.svg)](https://github.com/michagrandel/releases)
[![PyPI](https://img.shields.io/pypi/v/ProjectSetup.svg)](http://pypi.python.org)
[![license](https://img.shields.io/github/license/michagrandel/ProjectSetup.svg)](https://github.com/michagrandel/ProjectSetup/blob/master/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Initialize your Python Project

## Features

ProjectSetup helps you to get started with your Python Project as fast as possible.

It will handle these tasks for you:

* initialize a **python module** named after your project
* add **Community Files**
    * Readme.md
    * Contributing.md
    * CODE_OF_CONDUCT.md
    * issue_template.md
    * PULL_REQUEST_TEMPALTE.md
* add important project files like **LICENSE**, **setup.py**, **requirements.txt** and more
* initialize **Sphinx documentation**
* prepare **test**-directory with a skipping dummy test
* build a initial **source distribution** and **python wheel**
* Some **additional customizations** are done for *Jetbrains PyCharm IDE*
* and [many more features ...][wiki]

*To get a full list of all supported features, please read the [project wiki][wiki].*

## Getting Started

### Installing

```
pip install ProjectSetup
```

If this doesn't work, try to download the code, 
extract the zip-file and run:

```
python setup.py install -r requirements.txt
```

### How to run

To run the script, just use the *quickstart.py*-Script in the *script*-folder.

## Customize the settings

To customize everything, you just need to edit the *quickstart.py*.

In future releases, you will be able to use a command line interface without needing to edit the script code.

## Running the tests

If you like to run the tests, just open a terminal in the project directory and run:

```
python -m unittest discover -s test -p "*_test.py"
```

## Built With

* [lxml](http://lxml.de/) \
  *combines the speed and XML feature completeness of these libraries with the simplicity of a native Python API*
* [Jinja2](http://jinja.pocoo.org/)\
  *is a full featured template engine for Python*

## Contributing

First of all: Thank you very kindly for your interest in contributing to our code!

Please take a moment and read [CONTRIBUTING.md](Contributing.md) to get you started!

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available,
see the [releases on this repository][github-releases].

## Authors

* **Micha Grandel** - *Author and maintainer* - [Github][github]

We thank all of our [contributors][github-contributors], who participated in this project.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details

## Code of Conduct

Everyone interacting in the ProjectSetup project's codebases, issue trackers, chat rooms, and mailing lists 
is expected to follow the [Code of Conduct][code_of_conduct].

[github]: https://github.com/michagrandel
[github-releases]: https://github.com/michagrandel/ProjectSetup/releases
[github-contributors]: https://github.com/michagrandel/ProjectSetup/graphs/contributors
[python]: https://www.python.org/downloads/
[pip]: https://pypi.python.org/pypi/pip
[flask]: http://flask.pocoo.org
[gitflow]: https://danielkummer.github.io/git-flow-cheatsheet/
[gitflow-model]: http://nvie.com/posts/a-successful-git-branching-model/
[wiki]: https://github.com/michagrandel/ProjectSetup/wiki
[code_of_conduct]: https://github.com/michagrandel/ProjectSetup/blob/master/CODE_OF_CONDUCT.md
