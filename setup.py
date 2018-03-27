#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @formatter:off
#
#                                             ,,
#                                             db
#     \
#     _\,,          `7MM  `7MM  `7MMpMMMb.  `7MM  ,p6"bo   ,pW"Wq.`7Mb,od8 `7MMpMMMb.
#    "-=\~     _      MM    MM    MM    MM    MM 6M'  OO  6W'   `Wb MM' "'   MM    MM
#       \\~___( ~     MM    MM    MM    MM    MM 8M       8M     M8 MM       MM    MM
#      _|/---\\_      MM    MM    MM    MM    MM 8M       8M     M8 MM       MM    MM
#     \        \      MM    MM    MM    MM    MM YM.    , YA.   ,A9 MM       MM    MM
#                     `Mbod"YML..JMML  JMML..JMML.YMbmd'   `Ybmd9'.JMML.   .JMML  JMML.
#
#                     written with <3 by Micha Grandel, talk@michagrandel.de
#
#                     Project:         https://github.com/michagrandel/ProjectSetup
#                     Report a bug:    https://github.com/michagrandel/ProjectSetup/issues
#                     Contribute:      https://github.com/michagrandel/ProjectSetup/wiki/Contribute
#
#                     Facebook:        https://me.me/micha.animator
#                     Instagram:       @michagrandel
#                     -----------------------------------------------------------------
#
#                     Copyright 2018
#
#                     Licensed under the Apache License, Version 2.0 (the 'License');
#                     you may not use this file except in compliance with the License.
#                     You may obtain a copy of the License at
#                     
#                     http://www.apache.org/licenses/LICENSE-2.0
#                     
#                     Unless required by applicable law or agreed to in writing,
#                     software distributed under the License is distributed on an
#                     'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
#                     either express or implied. See the License for the specific
#                     language governing permissions and limitations under the License.
#                     -----------------------------------------------------------------
#                     @formatter:on

"""ProjectSetup

A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from __future__ import unicode_literals, print_function
# To use a consistent encoding
from io import open
import os
import sys
import platform
import shutil
from distutils.dir_util import copy_tree

# Always prefer setuptools over distutils
try:
    from setuptools import setup, find_packages
    packages = find_packages(exclude=['contrib', 'docs', 'test', 'build', 'dist', 'venv', 'script'])
except ImportError:
    from distutils.core import setup
    from pkgutil import walk_packages

    import ProjectSetup


    def find_packages(path=__path__, prefix=""):
        """
        replacement for setuptools find_packages

        :param path: start search
        :param prefix:

        :return:
        """
        yield prefix
        prefix += "."
        for _, name, ispkg in walk_packages(path, prefix):
            if ispkg:
                yield name


    packages = list(find_packages(ProjectSetup.__path__, ProjectSetup.__name__))


try:
    import array
except ImportError:
    array = False

try:
    from six import PY3
except ImportError:
    PY3 = sys.version_info[0] == 3

# import some windows related packages to enable AppDirs class
try:
    if PY3:
        import winreg as _winreg
    else:
        import _winreg
except ImportError:
    _winreg = False

try:
    from win32com.shell import shellcon, shell
    winshell = True
except ImportError:
    winshell = False
    shell = False

try:
    import ctypes
except ImportError:
    ctypes = False

try:
    import win32api
except ImportError:
    win32api = False

try:
    import win32con
except ImportError:
    win32con = False

try:
    from com.sun import jna
    from com.sun.jna.platform import win32
except ImportError:
    jna = False


__status__ = 'planing'
__author__ = 'Micha Grandel'
__version__ = '1.0.2'
__maintainer__ = 'Micha Grandel'
__copyright__ = 'written with <3 by Micha Grandel'
__license__ = 'Apache 2.0 license'
__contact__ = 'talk@michagrandel.de'
__maintainer_contact__ = 'talk@michagrandel.de'

project_directory = os.path.dirname(os.path.abspath(__file__))
project_name = os.path.basename(project_directory)
assert project_name == 'ProjectSetup', 'Wrong name.'
# Get the long description from the README file
with open(os.path.join(project_directory, 'Readme.rst'), encoding='utf-8') as f:
    long_description = f.read()
if PY3:
    unicode = str


def requirements(category='install'):
    """
    return list with requirements

    :param category: category of requirements
    :return: list with requirements
    """
    if category.lower().startswith('install'):
        file_ = 'requirements.txt'
    elif category.lower().startswith('dev'):
        file_ = 'development-requirements.txt'
    elif category.lower().startswith('test'):
        file_ = 'test-requirements.txt'
    else:
        return []

    try:
        with open(file_, 'r', encoding='utf-8') as requirements_file:
            content = requirements_file.read()
        content = content.split('\n')
    except (IOError, OSError) as error:
        content = []

    return content


def status(s):
    if s.lower() in ('planing', 'planning'):
        return 'Development Status :: 1 - Planning'
    if s.lower() in ('pre-alpha'):
        return 'Development Status :: 2 - Pre-Alpha'
    if s.lower().startswith('alpha'):
        return 'Development Status :: 3 - Alpha'
    if s.lower().startswith('beta'):
        return 'Development Status :: 4 - Beta'
    if s.lower().startswith('production') or __status__.lower().startswith('stable'):
        return 'Development Status :: 5 - Production/Stable'
    if s.lower().startswith('mature'):
        return 'Development Status :: 6 - Mature'
    if s.lower().startswith('inactive'):
        return 'Development Status :: 7 - Inactive'


class AppDirs(object):
    """Convenience wrapper for getting application dirs."""
    def __init__(self, appname=None, appauthor=None, version=None, roaming=False, multipath=False):
        self.appname = appname
        self.appauthor = appauthor
        self.version = version
        self.roaming = roaming
        self.multipath = multipath

        # get platform
        if sys.platform.startswith('java'):
            os_name = platform.java_ver()[3][0]
            if os_name.startswith('Windows'):  # "Windows XP", "Windows 7", etc.
                self.system = 'win32'
            elif os_name.startswith('Mac'):  # "Mac OS X", etc.
                self.system = 'darwin'
            else:  # "Linux", "SunOS", "FreeBSD", etc.
                # Setting this to "linux2" is not ideal, but only Windows or Mac
                # are actually checked for and the rest of the module expects
                # *sys.platform* style strings.
                self.system = 'linux2'
        else:
            self.system = sys.platform

        # on windows, import platform specific packages
        if self.system == "win32":
            try:
                import win32com.shell
                self._get_win_folder = AppDirs._get_win_folder_with_pywin32
            except ImportError:
                try:
                    from ctypes import windll
                    self._get_win_folder = AppDirs._get_win_folder_with_ctypes
                except ImportError:
                    try:
                        import com.sun.jna
                        self._get_win_folder = AppDirs._get_win_folder_with_jna
                    except ImportError:
                        self._get_win_folder = AppDirs._get_win_folder_from_registry


    @property
    def user_data_dir(self):
        """
        Return full path to the user-specific data dir for this application.
        """
        appauthor = self.appauthor
        if self.system == "win32":
            if appauthor is None:
                appauthor = self.appname
            const = self.roaming and "CSIDL_APPDATA" or "CSIDL_LOCAL_APPDATA"
            try:
                path = os.path.normpath(self._get_win_folder(const))
            except NotImplementedError:
                path = os.path.expanduser('~/bin')
            if self.appname:
                if appauthor is not False:
                    path = os.path.join(path, appauthor, self.appname)
                else:
                    path = os.path.join(path, self.appname)
        elif self.system == 'darwin':
            path = os.path.expanduser('~/Library/Application Support/')
            if self.appname:
                path = os.path.join(path, self.appname)
        else:
            path = os.getenv('XDG_DATA_HOME', os.path.expanduser("~/.local/share"))
            if self.appname:
                path = os.path.join(path, self.appname)
        if self.appname and self.version:
            path = os.path.join(path, self.version)
        return path


    @property
    def site_data_dir(self):
        """Return full path to the user-shared data dir for this application.

        "appname" is the name of application.
            If None, just the system directory is returned.
        "appauthor" (only used on Windows) is the name of the
            appauthor or distributing body for this application. Typically
            it is the owning company name. This falls back to appname. You may
            pass False to disable it.
        "version" is an optional version path element to append to the
            path. You might want to use this if you want multiple versions
            of your app to be able to run independently. If used, this
            would typically be "<major>.<minor>".
            Only applied when appname is present.
        "multipath" is an optional parameter only applicable to *nix
            which indicates that the entire list of data dirs should be
            returned. By default, the first item from XDG_DATA_DIRS is
            returned, or '/usr/local/share/<AppName>',
            if XDG_DATA_DIRS is not set

        Typical site data directories are:
            Mac OS X:   /Library/Application Support/<AppName>
            Unix:       /usr/local/share/<AppName> or /usr/share/<AppName>
            Win XP:     C:\Documents and Settings\All Users\Application Data\<AppAuthor>\<AppName>
            Vista:      (Fail! "C:\ProgramData" is a hidden *system* directory on Vista.)
            Win 7:      C:\ProgramData\<AppAuthor>\<AppName>   # Hidden, but writeable on Win 7.

        For Unix, this is using the $XDG_DATA_DIRS[0] default.

        WARNING: Do not use this on Windows. See the Vista-Fail note above for why.
        """
        appauthor = self.appauthor
        appname = self.appname

        if self.system == "win32":
            if appauthor is None:
                appauthor = appname
            try:
                path = os.path.normpath(self._get_win_folder("CSIDL_COMMON_APPDATA"))
            except NotImplementedError:
                path = os.path.expanduser('~/bin')
            if appname:
                if appauthor is not False:
                    path = os.path.join(path, appauthor, appname)
                else:
                    path = os.path.join(path, appname)
        elif self.system == 'darwin':
            path = os.path.expanduser('/Library/Application Support')
            if appname:
                path = os.path.join(path, appname)
        else:
            # XDG default for $XDG_DATA_DIRS
            # only first, if multipath is False
            path = os.getenv('XDG_DATA_DIRS', os.pathsep.join(['/usr/local/share', '/usr/share']))
            pathlist = [os.path.expanduser(x.rstrip(os.sep)) for x in path.split(os.pathsep)]
            if appname:
                if self.version:
                    appname = os.path.join(appname, self.version)
                pathlist = [os.sep.join([x, appname]) for x in pathlist]

            if self.multipath:
                path = os.pathsep.join(pathlist)
            else:
                path = pathlist[0]
            return path

        if appname and self.version:
            path = os.path.join(path, self.version)
        return path


    @property
    def user_config_dir(self):
        """Return full path to the user-specific config dir for this application.

            "appname" is the name of application.
                If None, just the system directory is returned.
            "appauthor" (only used on Windows) is the name of the
                appauthor or distributing body for this application. Typically
                it is the owning company name. This falls back to appname. You may
                pass False to disable it.
            "version" is an optional version path element to append to the
                path. You might want to use this if you want multiple versions
                of your app to be able to run independently. If used, this
                would typically be "<major>.<minor>".
                Only applied when appname is present.
            "roaming" (boolean, default False) can be set True to use the Windows
                roaming appdata directory. That means that for users on a Windows
                network setup for roaming profiles, this user data will be
                sync'd on login. See
                <http://technet.microsoft.com/en-us/library/cc766489(WS.10).aspx>
                for a discussion of issues.

        Typical user config directories are:
            Mac OS X:               ~/Library/Preferences/<AppName>
            Unix:                   ~/.config/<AppName>     # or in $XDG_CONFIG_HOME, if defined
            Win *:                  same as user_data_dir

        For Unix, we follow the XDG spec and support $XDG_CONFIG_HOME.
        That means, by default "~/.config/<AppName>".
        """
        if self.system == "win32":
            path = self.user_data_dir()
        elif self.system == 'darwin':
            path = os.path.expanduser('~/Library/Preferences/')
            if self.appname:
                path = os.path.join(path, self.appname)
        else:
            path = os.getenv('XDG_CONFIG_HOME', os.path.expanduser("~/.config"))
            if self.appname:
                path = os.path.join(path, self.appname)
        if self.appname and self.version:
            path = os.path.join(path, self.version)
        return path


    @property
    def site_config_dir(self):
        """Return full path to the user-shared data dir for this application.

            "appname" is the name of application.
                If None, just the system directory is returned.
            "appauthor" (only used on Windows) is the name of the
                appauthor or distributing body for this application. Typically
                it is the owning company name. This falls back to appname. You may
                pass False to disable it.
            "version" is an optional version path element to append to the
                path. You might want to use this if you want multiple versions
                of your app to be able to run independently. If used, this
                would typically be "<major>.<minor>".
                Only applied when appname is present.
            "multipath" is an optional parameter only applicable to *nix
                which indicates that the entire list of config dirs should be
                returned. By default, the first item from XDG_CONFIG_DIRS is
                returned, or '/etc/xdg/<AppName>', if XDG_CONFIG_DIRS is not set

        Typical site config directories are:
            Mac OS X:   same as site_data_dir
            Unix:       /etc/xdg/<AppName> or $XDG_CONFIG_DIRS[i]/<AppName> for each value in
                        $XDG_CONFIG_DIRS
            Win *:      same as site_data_dir
            Vista:      (Fail! "C:\ProgramData" is a hidden *system* directory on Vista.)

        For Unix, this is using the $XDG_CONFIG_DIRS[0] default, if multipath=False

        WARNING: Do not use this on Windows. See the Vista-Fail note above for why.
        """
        appname = self.appname
        if self.system == 'win32':
            path = self.site_data_dir()
            if appname and self.version:
                path = os.path.join(path, self.version)
        elif self.system == 'darwin':
            path = os.path.expanduser('/Library/Preferences')
            if appname:
                path = os.path.join(path, appname)
        else:
            # XDG default for $XDG_CONFIG_DIRS
            # only first, if multipath is False
            path = os.getenv('XDG_CONFIG_DIRS', '/etc/xdg')
            pathlist = [os.path.expanduser(x.rstrip(os.sep)) for x in path.split(os.pathsep)]
            if appname:
                if self.version:
                    appname = os.path.join(appname, self.version)
                pathlist = [os.sep.join([x, appname]) for x in pathlist]

            if self.multipath:
                path = os.pathsep.join(pathlist)
            else:
                path = pathlist[0]
        return path


    @property
    def user_cache_dir(self):
        """Return full path to the user-specific cache dir for this application."""
        opinion = True
        appauthor = self.appauthor
        if self.system == "win32":
            if appauthor is None:
                appauthor = self.appname
            try:
                path = os.path.normpath(self._get_win_folder("CSIDL_LOCAL_APPDATA"))
            except NotImplementedError:
                path = os.path.expanduser('~/bin')
            if self.appname:
                if appauthor is not False:
                    path = os.path.join(path, appauthor, self.appname)
                else:
                    path = os.path.join(path, self.appname)
                if opinion:
                    path = os.path.join(path, "Cache")
        elif self.system == 'darwin':
            path = os.path.expanduser('~/Library/Caches')
            if self.appname:
                path = os.path.join(path, self.appname)
        else:
            path = os.getenv('XDG_CACHE_HOME', os.path.expanduser('~/.cache'))
            if self.appname:
                path = os.path.join(path, self.appname)
        if self.appname and self.version:
            path = os.path.join(path, self.version)
        return path


    @property
    def user_state_dir(self):
        """Return full path to the user-specific state dir for this application.

            "appname" is the name of application.
                If None, just the system directory is returned.
            "appauthor" (only used on Windows) is the name of the
                appauthor or distributing body for this application. Typically
                it is the owning company name. This falls back to appname. You may
                pass False to disable it.
            "version" is an optional version path element to append to the
                path. You might want to use this if you want multiple versions
                of your app to be able to run independently. If used, this
                would typically be "<major>.<minor>".
                Only applied when appname is present.
            "roaming" (boolean, default False) can be set True to use the Windows
                roaming appdata directory. That means that for users on a Windows
                network setup for roaming profiles, this user data will be
                sync'd on login. See
                <http://technet.microsoft.com/en-us/library/cc766489(WS.10).aspx>
                for a discussion of issues.

        Typical user state directories are:
            Mac OS X:  same as user_data_dir
            Unix:      ~/.local/state/<AppName>   # or in $XDG_STATE_HOME, if defined
            Win *:     same as user_data_dir

        For Unix, we follow this Debian proposal <https://wiki.debian.org/XDGBaseDirectorySpecification#state>
        to extend the XDG spec and support $XDG_STATE_HOME.

        That means, by default "~/.local/state/<AppName>".
        """
        if self.system in ["win32", "darwin"]:
            path = self.user_data_dir()  # no version number!
        else:
            path = os.getenv('XDG_STATE_HOME', os.path.expanduser("~/.local/state"))
            if self.appname:
                path = os.path.join(path, self.appname)
        if self.appname and self.version:
            path = os.path.join(path, self.version)
        return path


    @property
    def user_log_dir(self):
        """Return full path to the user-specific log dir for this application."""
        opinion = True
        version = self.version
        if self.system == "darwin":
            path = os.path.join(os.path.expanduser('~/Library/Logs'),self.appname)
        elif self.system == "win32":
            path = self.user_data_dir
            version = False
            if opinion:
                path = os.path.join(path, "Logs")
        else:
            path = self.user_cache_dir
            version = False
            if opinion:
                path = os.path.join(path, "log")
        if self.appname and version:
            path = os.path.join(path, self.version)
        return path


    @staticmethod
    def _get_win_folder_from_registry(csidl_name):
        """
        return location of AppData folder on this machine.

        This is implemented for windows only.
        This implementation uses windows registry.

        This is a fallback technique at best. I'm not sure if using the
        registry for this guarantees us the correct answer for all CSIDL_*
        names.

        :param csidl_name: AppData vs Common AppData vs Local AppData
        :return: path of AppData folder
        """
        if _winreg:
            shell_folder_name = {
                "CSIDL_APPDATA": "AppData",
                "CSIDL_COMMON_APPDATA": "Common AppData",
                "CSIDL_LOCAL_APPDATA": "Local AppData",
            }[csidl_name]

            key = _winreg.OpenKey(
                _winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
            )
            dir, type = _winreg.QueryValueEx(key, shell_folder_name)
            return dir
        else:
            raise NotImplementedError('Cannot get windows appdata folder from registry')


    @staticmethod
    def _get_win_folder_with_pywin32(csidl_name):
        """
        return location of AppData folder on this machine.

        This is implemented for windows only.
        This implementation uses pywin32.

        :param csidl_name: AppData vs Common AppData vs Local AppData
        :return: path of AppData folder
        """
        if shell and shellcon:
            dir = shell.SHGetFolderPath(0, getattr(shellcon, csidl_name), 0, 0)
            # Try to make this a unicode path because SHGetFolderPath does
            # not return unicode strings when there is unicode data in the
            # path.
            try:
                dir = unicode(dir)

                # Downgrade to short path name if have highbit chars. See
                # <http://bugs.activestate.com/show_bug.cgi?id=85099>.
                has_high_char = False
                for c in dir:
                    if ord(c) > 255:
                        has_high_char = True
                        break
                if has_high_char:
                    if win32api:
                        dir = win32api.GetShortPathName(dir)
            except UnicodeError:
                pass
            return dir
        else:
            raise NotImplementedError('Cannot get windows appdata folder with pywin32')


    @staticmethod
    def _get_win_folder_with_ctypes(csidl_name):
        """
        return location of AppData folder on this machine.

        This is implemented for windows only.
        This implementation uses ctypes.

        :param csidl_name: AppData vs Common AppData vs Local AppData
        :return: path of AppData folder
        """
        if ctypes:
            csidl_const = {
                "CSIDL_APPDATA": 26,
                "CSIDL_COMMON_APPDATA": 35,
                "CSIDL_LOCAL_APPDATA": 28,
            }[csidl_name]

            buf = ctypes.create_unicode_buffer(1024)
            ctypes.windll.shell32.SHGetFolderPathW(None, csidl_const, None, 0, buf)

            # Downgrade to short path name if have highbit chars. See
            # <http://bugs.activestate.com/show_bug.cgi?id=85099>.
            has_high_char = False
            for c in buf:
                if ord(c) > 255:
                    has_high_char = True
                    break
            if has_high_char:
                buf2 = ctypes.create_unicode_buffer(1024)
                if ctypes.windll.kernel32.GetShortPathNameW(buf.value, buf2, 1024):
                    buf = buf2

            return buf.value
        else:
            raise NotImplementedError('Cannot get windows appdata folder with ctypes')


    @staticmethod
    def _get_win_folder_with_jna(csidl_name):
        """
        return location of AppData folder on this machine.

        This is implemented for windows only.
        This implementation uses JNA.

        :param csidl_name: AppData vs Common AppData vs Local AppData
        :return: path of AppData folder
        """
        if jna and win32 and array:
            buf_size = win32.WinDef.MAX_PATH * 2
            buf = array.zeros('c', buf_size)
            shell = win32.Shell32.INSTANCE
            shell.SHGetFolderPath(None, getattr(win32.ShlObj, csidl_name), None, win32.ShlObj.SHGFP_TYPE_CURRENT, buf)
            dir = jna.Native.toString(buf.tostring()).rstrip("\0")

            # Downgrade to short path name if have highbit chars. See
            # <http://bugs.activestate.com/show_bug.cgi?id=85099>.
            has_high_char = False
            for c in dir:
                if ord(c) > 255:
                    has_high_char = True
                    break
            if has_high_char:
                buf = array.zeros('c', buf_size)
                kernel = win32.Kernel32.INSTANCE
                if kernel.GetShortPathName(dir, buf, buf_size):
                    dir = jna.Native.toString(buf.tostring()).rstrip("\0")

            return dir
        else:
            raise NotImplementedError('Cannot get windows appdata folder with JNA')


appdirs = AppDirs(appname=project_name, appauthor=False, roaming=True)


setup(
    name=project_name.lower(),  # Required
    version=__version__,  # Required
    description='describe your project',  # Required
    long_description=long_description,  # Optional
    url='https://github.com/michagrandel/{}'.format(project_name),  # Optional
    author=__author__,  # Optional
    author_email=__contact__,  # Optional
    maintainer=__maintainer__,  # Optional
    maintainer_email=__maintainer_contact__,  # Optional
    keywords='python',  # Optional
    entry_points={
        'console_scripts': [
            'quickstart = script.quickstart:main',
        ],
        #
        # 'gui_scripts': [
        #     'baz = my_package_gui:start_func',
        # ]
        #
    },

    classifiers=[
        status(__status__),
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        # 'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
    ],

    packages=packages,  # Required
    install_requires=requirements(),  # Optional
    extras_require={  # Optional
        'dev': requirements('dev'),
        'test': requirements('test'),
    },

    # package_data={  # Optional
    #     b'': [
    #         b'templates/*', b'data/*', b'images/*', b'icons/*', b'sample data/*',
    #         b'LC_MESSAGES/*', b'*.ts', b'*.strings', b'languages/*', b'*.pot', b'*.po', b'*.mo',
    #         b'*.pro', b'*.pro.user', b'*.ui', b'*.qrc', b'*.qm', b'*.qml', b'*.rc', b'resources/*', b'ui/*',
    #         b'*.zip', b'*.7z', b'*.z', b'*.bzip', b'*.tar', b'*.gz', b'*.tar.gz', b'*.bin',
    #         b'*.txt', b'*.rst', b'*.md', b'*.xml',
    #         b'*.conf', b'*.json', b'*.yml', b'*.yaml', b'*.ini', b'*.plist', b'*.csv', b'*.properties', b'*.jinja2',
    #         b'*.xmp',
    #         b'Makefile', b'*.bat', b'*.cmd', b'*.sh', b'*.ps1', b'*.lua',
    #         b'*.html', b'*.css', b'*.js', b'*.pdf',
    #         b'*.db', b'*.sql', b'*.sqlite'
    #         b'*.otf', b'*.ttf', b'*.woff',
    #         b'*.xpm', b'*.xbm', b'*.gif', b'*.ico',
    #         b'*.jpg', b'*.jpeg', b'*.tga', b'*.tiff', b'*.png',
    #         b'*.hdr', b'*.dng', b'*.exr', b'*.iff',
    #         b'*.svg',
    #         b'*.aiff', b'*.aif', b'*.mp3', b'*.m4a', b'*.ogg', b'*.oga',
    #         b'*.mpeg', b'*.mp4', b'*.m4v', b'*.asf', b'*.webm', b'*.ogv',
    #         b'*.sample', b'*.b64']
    # },

    data_files = [
        (os.path.join('share', project_name.lower(), '.templates'), [
            'ProjectSetup/templates/.editorconfig',
            'ProjectSetup/templates/.travis.yml',
            'ProjectSetup/templates/__init__.py.jinja2',
            'ProjectSetup/templates/CODE_OF_CONDUCT.md',
            'ProjectSetup/templates/conf.py.jinja2',
            'ProjectSetup/templates/Contributing.md.jinja2',
            'ProjectSetup/templates/discover.py.jinja2',
            'ProjectSetup/templates/How_to_install_Python_2.7.md',
            'ProjectSetup/templates/index.rst.jinja2',
            'ProjectSetup/templates/issue_template.md',
            'ProjectSetup/templates/LICENSE',
            'ProjectSetup/templates/LICENSE.txt',
            'ProjectSetup/templates/make.bat.jinja2',
            'ProjectSetup/templates/Makefile.jinja2',
            'ProjectSetup/templates/PULL_REQUEST_TEMPLATE.md',
            'ProjectSetup/templates/Readme.md.jinja2',
            'ProjectSetup/templates/setup.py.jinja2',
        ]),
        # ('.templates', [
        #     'ProjectSetup/templates/.editorconfig',
        #     'ProjectSetup/templates/.travis.yml',
        #     'ProjectSetup/templates/__init__.py.jinja2',
        #     'ProjectSetup/templates/CODE_OF_CONDUCT.md',
        #     'ProjectSetup/templates/conf.py.jinja2',
        #     'ProjectSetup/templates/Contributing.md.jinja2',
        #     'ProjectSetup/templates/discover.py.jinja2',
        #     'ProjectSetup/templates/How_to_install_Python_2.7.md',
        #     'ProjectSetup/templates/index.rst.jinja2',
        #     'ProjectSetup/templates/issue_template.md',
        #     'ProjectSetup/templates/LICENSE',
        #     'ProjectSetup/templates/LICENSE.txt',
        #     'ProjectSetup/templates/make.bat.jinja2',
        #     'ProjectSetup/templates/Makefile.jinja2',
        #     'ProjectSetup/templates/PULL_REQUEST_TEMPLATE.md',
        #     'ProjectSetup/templates/Readme.md.jinja2',
        #     'ProjectSetup/templates/setup.py.jinja2',
        # ])
    ],

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #
    # sys.prefix:
    # A string giving the site-specific directory prefix where the platform independent
    # Python files are installed; by default, this is the string '/usr/local'.
    # This can be set at build time with the --prefix argument to the configure script.
    # The main collection of Python library modules is installed in the directory prefix/lib/pythonX.Y
    # while the platform independent header files (all except pyconfig.h) are stored in prefix/include/pythonX.Y,
    # where X.Y is the version number of Python, for example 2.7.
    #
    # data_files = [
    #     ('templates'), []),

    #     ('Backup API/0.1.0/openapi',
    #      [
    #         'openapi/v0.1.0/openapi.html',
    #         'openapi/v0.1.0/openapi.json',
    #         'openapi/v0.1.0/openapi.yaml',
    #      ]),
    #     ('Backup API/0.1.0/templates',
    #      [
    #         'templates/openapi.html'
    #      ])
    # ],  # Optional
)
