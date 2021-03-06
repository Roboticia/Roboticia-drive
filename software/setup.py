#!/usr/bin/env python

import re
import sys

from setuptools import setup, find_packages


def version():
    with open('roboticia_drive/_version.py') as f:
        return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read()).group(1)

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name='roboticia-drive',
      version=version(),
      packages=find_packages(),

      install_requires=['pypot >= 3.0', 'hampy','rplidar-roboticia'],

      setup_requires=['setuptools_git >= 0.3', ],

      include_package_data=True,
      exclude_package_data={'': ['README', '.gitignore']},

      zip_safe=False,

      author='Julien JEHL',
      author_email='julien.jehl@roboticia.com',
      description='Roboticia-first Software Library',
      url='https://github.com/Roboticia/Roboticia-first',
      license='GNU GENERAL PUBLIC LICENSE Version 3',

      **extra
      )
