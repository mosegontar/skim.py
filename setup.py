#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='skim.py',
    version='0.1.0',
    description='Skim python files and display python classes and functions used',
    long_description=readme,
    author='Alexander Gontar',
    author_email='mosegontar@gmail.com',
    url='https://github.com/mosegontar/skim.py.git',
    license='MIT',
    packages=['skim'],
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points = {
        'console_scripts': ['skim = skim.skim:run'],
    }
)