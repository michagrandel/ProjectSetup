.. _features:

=============================
Features of ProjectSetup
=============================

Use ProjectSetup to initialize your project.

* :ref:`structure`
* :ref:`sphinx`
* :ref:`travis`
* :ref:`pypi`
* :ref:`github`
* :ref:`pycharm`


.. _structure:

------------------------
Create Project Structure
------------------------

ProjectSetup generates a simple, but powerful file structure for you.
In your folder, it creats a Python Package (including *__init__.py*) named after your project.

Additionally, it will create a *setup.py* and a *requirements.txt* at the top level of your project.
Use these as a starting point and edit them so they fit your needs.

The setup will also create some community friendly files to help you build a strong community. It includes
a *Readme.md*, *Contributing.md* and *CODE_OF_CONDUCT.md* to you project. Use these files as template,
they include many information on how to use them.

To round things up, the project setup build a *LICENSE* file to let everyone know what they are and are
not allowed to do.


.. _sphinx:

--------------------------------
Initialize Sphinx documentation
--------------------------------

Write useful docs right away, without the need to configure and install sphinx first. It is all included with your
setup. You will get a basic setup with makefile and bat-file, so you can get things done quickly.

In your docs folder, there is a *issue_template.md* and a *PULL_REQUEST_TEMPLATE.md*, too. You will find them useful for
github to manage issue reports and PR's!

.. _travis:

----------------------------------------------------------------
Prepare unit test and Continuous Integration with Travis
----------------------------------------------------------------

Do you use travis for continous integration? Just go to the Travis homepage, login and activate your newly generated
github repository. No need for editing a configuration file - your repository already include a basic *.travis.yml*.

To test everything, you can just initialize a build on the Travis Homepage. It will work right out of the box!

To add additional tests, just put some unit tests into the test-folder in your project. By default, every file called
*test_###.py* will be used to build on Travis.

.. _pypi:

-------------------
Distribute on PyPI
-------------------

.. _github:

-------------------------------------------
Create a git repository and push to Github
-------------------------------------------

.. _pycharm:

-----------------------------------------------
Custom Project Settings in Jetbrains PyCharm
-----------------------------------------------
