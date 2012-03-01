#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='Splango',
      version='0.1',
      description='Split (A/B) testing library for Django',
      author='Shimon Rura',
      author_email='shimon@rura.org',
      url='http://github.com/shimon/Splango',
      packages=find_packages(),
      include_package_data=True,
)
