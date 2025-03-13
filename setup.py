#!/usr/bin/env python

from distutils.core import setup

setup(name='paneltools',
      version='1.0',
      description='Tools to use with Panel',
      packages=['paneltools'],
      package_dir={"paneltools": "paneltools"},
      entry_points={
      }, 
      install_requires=['panel==1.5.0'
    ]
     )