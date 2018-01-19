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

__status__ = 'Planning'
__author__ = 'Micha Grandel'
__version__ = '0.0.1'
__copyright__ = 'written with <3 by Micha Grandel'
__license__ = 'Apache 2.0 license'
__contact__ = 'talk@michagrandel.de'

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'Readme.rst'), encoding='utf-8') as f:
    long_description = f.read()


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
        with open(file_, encoding='utf-8') as requirements_file:
            content = requirements_file.read()
        content = content.split('\n')
    except (IOError, OSError):
        content = []

    return content


setup(
    name='projectsetup',  # Required
    version=__version__,  # Required
    description='Initialize a python project',  # Required
    long_description=long_description,  # Optional
    url='https://github.com/michagrandel/ProjectSetup',  # Optional
    author=__author__,  # Optional
    author_email=__contact__,  # Optional
    # keywords='',  # Optional space separated string
    packages=packages,  # Required
    install_requires=requirements(),  # Optional
    extras_require={  # Optional
        'dev': requirements('dev'),
        'test': requirements('test'),
    },
    scripts=[os.path.join('script', f) for f in os.listdir('script')],

    package_data={  # Optional
        b'': [
            b'templates/*', b'data/*', b'images/*', b'icons/*', b'sample data/*',
            b'LC_MESSAGES/*', b'*.ts', b'*.strings', b'languages/*', b'*.pot', b'*.po', b'*.mo',
            b'*.pro', b'*.pro.user', b'*.ui', b'*.qrc', b'*.qm', b'*.qml', b'*.rc', b'resources/*', b'ui/*',
            b'*.zip', b'*.7z', b'*.z', b'*.bzip', b'*.tar', b'*.gz', b'*.tar.gz', b'*.bin',
            b'*.txt', b'*.rst', b'*.md', b'*.xml',
            b'*.conf', b'*.json', b'*.yml', b'*.yaml', b'*.ini', b'*.plist', b'*.csv', b'*.properties', b'*.jinja2',
            b'*.xmp',
            b'Makefile', b'*.bat', b'*.cmd', b'*.sh', b'*.ps1', b'*.lua',
            b'*.html', b'*.css', b'*.js', b'*.pdf',
            b'*.db', b'*.sql', b'*.sqlite'
            b'*.otf', b'*.ttf', b'*.woff',
            b'*.xpm', b'*.xbm', b'*.gif', b'*.ico',
            b'*.jpg', b'*.jpeg', b'*.tga', b'*.tiff', b'*.png',
            b'*.hdr', b'*.dng', b'*.exr', b'*.iff',
            b'*.svg',
            b'*.aiff', b'*.aif', b'*.mp3', b'*.m4a', b'*.ogg', b'*.oga',
            b'*.mpeg', b'*.mp4', b'*.m4v', b'*.asf', b'*.webm', b'*.ogv',
            b'*.sample', b'*.b64']
    },

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
    # data_files=[
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

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',

        # Indicate who your project is intended for
        # Valid Values:
        #
        # 'Intended Audience :: Customer Service',
        # 'Intended Audience :: Developers',
        # 'Intended Audience :: Education',
        # 'Intended Audience :: End Users/Desktop',
        # 'Intended Audience :: Financial and Insurance Industry',
        # 'Intended Audience :: Healthcare Industry',
        # 'Intended Audience :: Information Technology',
        # 'Intended Audience :: Legal Industry',
        # 'Intended Audience :: Manufacturing',
        # 'Intended Audience :: Other Audience',
        # 'Intended Audience :: Religion',
        # 'Intended Audience :: Science/Research',
        # 'Intended Audience :: System Administrators',
        # 'Intended Audience :: Telecommunications Industry',

        # Valid Values:
        #
        # 'Topic :: Artistic Software',
        # 'Topic :: Communications',
        # 'Topic :: Communications :: Chat',
        # 'Topic :: Communications :: Chat :: Internet Relay Chat',
        # 'Topic :: Communications :: Email',
        # 'Topic :: Communications :: Email :: Address Book',
        # 'Topic :: Communications :: Email :: Email Clients (MUA)',
        # 'Topic :: Communications :: Email :: Filters',
        # 'Topic :: Communications :: Email :: Mailing List Servers',
        # 'Topic :: Communications :: Email :: Mail Transport Agents',
        # 'Topic :: Database',
        # 'Topic :: Desktop Environment',
        # 'Topic :: Desktop Environment :: File Managers',
        # 'Topic :: Desktop Environment :: Gnome',
        # 'Topic :: Desktop Environment :: Screen Savers',
        # 'Topic :: Documentation',
        # 'Topic :: Documentation :: Sphinx',
        # 'Topic :: Education',
        # 'Topic :: Education :: Testing',
        # 'Topic :: Games/Entertainment',
        # 'Topic :: Games/Entertainment :: Arcade',
        # 'Topic :: Games/Entertainment :: Board Games',
        # 'Topic :: Games/Entertainment :: First Person Shooters',
        # 'Topic :: Games/Entertainment :: Fortune Cookies',
        # 'Topic :: Games/Entertainment :: Multi-User Dungeons (MUD)',
        # 'Topic :: Games/Entertainment :: Puzzle Games',
        # 'Topic :: Games/Entertainment :: Real Time Strategy',
        # 'Topic :: Games/Entertainment :: Role-Playing',
        # 'Topic :: Games/Entertainment :: Side-Scrolling/Arcade Games',
        # 'Topic :: Games/Entertainment :: Simulation',
        # 'Topic :: Games/Entertainment :: Turn Based Strategy',
        # 'Topic :: Internet',
        # 'Topic :: Internet :: WWW/HTTP',
        # 'Topic :: Internet :: WWW/HTTP :: Browsers',
        # 'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        # 'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        # 'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System',
        # 'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki',
        # 'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        # 'Topic :: Internet :: WWW/HTTP :: Site Management',
        # 'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking',
        # 'Topic :: Internet :: WWW/HTTP :: WSGI',
        # 'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        # 'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        # 'Topic :: Multimedia',
        # 'Topic :: Multimedia :: Graphics',
        # 'Topic :: Multimedia :: Graphics :: 3D Modeling',
        # 'Topic :: Multimedia :: Graphics :: 3D Rendering',
        # 'Topic :: Multimedia :: Graphics :: Capture',
        # 'Topic :: Multimedia :: Graphics :: Capture :: Digital Camera',
        # 'Topic :: Multimedia :: Graphics :: Capture :: Scanners',
        # 'Topic :: Multimedia :: Graphics :: Capture :: Screen Capture',
        # 'Topic :: Multimedia :: Graphics :: Editors',
        # 'Topic :: Multimedia :: Graphics :: Editors :: Raster-Based',
        # 'Topic :: Multimedia :: Graphics :: Editors :: Vector-Based',
        # 'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        # 'Topic :: Multimedia :: Graphics :: Presentation',
        # 'Topic :: Multimedia :: Graphics :: Viewers',
        # 'Topic :: Multimedia :: Sound/Audio',
        # 'Topic :: Multimedia :: Sound/Audio :: Capture/Recording',
        # 'Topic :: Multimedia :: Sound/Audio :: Conversion',
        # 'Topic :: Multimedia :: Sound/Audio :: Speech',
        # 'Topic :: Multimedia :: Video',
        # 'Topic :: Multimedia :: Video :: Capture',
        # 'Topic :: Multimedia :: Video :: Conversion',
        # 'Topic :: Multimedia :: Video :: Display',
        # 'Topic :: Multimedia :: Video :: Non-Linear Editor',
        # 'Topic :: Office/Business',
        # 'Topic :: Office/Business :: Financial :: Spreadsheet',
        # 'Topic :: Office/Business :: Office Suites',
        # 'Topic :: Other/Nonlisted Topic',
        # 'Topic :: Printing',
        # 'Topic :: Religion',
        # 'Topic :: Scientific/Engineering',
        # 'Topic :: Scientific/Engineering :: Artificial Intelligence',
        # 'Topic :: Scientific/Engineering :: Artificial Life',
        # 'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        # 'Topic :: Scientific/Engineering :: Image Recognition',
        # 'Topic :: Scientific/Engineering :: Visualization',
        # 'Topic :: Security',
        # 'Topic :: Security :: Cryptography',
        # 'Topic :: Software Development :: Interpreters',
        # 'Topic :: Software Development :: Libraries :: Python Modules',
        # 'Topic :: Software Development :: User Interfaces',
        # 'Topic :: Software Development :: Version Control :: Git',
        # 'Topic :: Software Development :: Widget Sets',
        # 'Topic :: System',
        # 'Topic :: System :: Archiving',
        # 'Topic :: System :: Archiving :: Backup',
        # 'Topic :: System :: Archiving :: Compression',
        # 'Topic :: System :: Archiving :: Mirroring',
        # 'Topic :: System :: Archiving :: Packaging',
        # 'Topic :: System :: Installation/Setup',
        # 'Topic :: System :: Logging',
        # 'Topic :: System :: Monitoring',
        # 'Topic :: System :: Networking',
        # 'Topic :: System :: Software Distribution',
        # 'Topic :: System :: Systems Administration',
        # 'Topic :: System :: System Shells',
        # 'Topic :: Terminals',
        # 'Topic :: Text Editors',
        # 'Topic :: Text Editors :: Integrated Development Environments (IDE)',
        # 'Topic :: Text Processing',
        # 'Topic :: Text Processing :: Markup',
        # 'Topic :: Text Processing :: Markup :: HTML',
        # 'Topic :: Text Processing :: Markup :: LaTeX',
        # 'Topic :: Text Processing :: Markup :: XML',
        # 'Topic :: Utilities',

        'License :: OSI Approved',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',

        'Natural Language :: English',
    ],

)