#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs

import setuptools
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-google-chat',
    version='0.1.0',
    author='Yorgos Katsaros',
    author_email='yorgos.katsaros@gmail.com',
    maintainer='Yorgos Katsaros',
    maintainer_email='yorgos.katsaros@gmail.com',
    license='MIT',
    url='https://github.com/geokats7/pytest-google-chat',
    description='Notify google chat channel for test results',
    long_description=read('README.md'),
    packages=setuptools.find_packages(),
    py_modules=['pytest_google_chat'],
    python_requires='>=3.6',
    install_requires=['pytest', 'requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'pytest-google-chat = pytest_google_chat.plugin',
        ],
    },
)
