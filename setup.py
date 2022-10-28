#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='BioinformaticsHomework',
      version='0.1',
      description='Homeworks for Bioinformatics practice at ELTE IK',
      author='Tamas Nyiri',
      packages=find_packages(),
      package_data={'resources': ['*.txt'],
      }
)