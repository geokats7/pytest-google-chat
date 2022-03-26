#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import setuptools
from setuptools import setup

version = '0.4.2'

def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


with open('requirements/requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name='pytest-google-chat',
    version=version,
    author='Yorgos Katsaros',
    author_email='yorgos.katsaros@gmail.com',
    maintainer='Yorgos Katsaros',
    maintainer_email='yorgos.katsaros@gmail.com',
    license='MIT',
    url='https://github.com/geokats7/pytest-google-chat',
    description='Notify google chat channel for test results',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    py_modules=['pytest_google_chat'],
    python_requires='>=3.6',
    install_requires=install_requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'pytest-google-chat = pytest_google_chat.plugin',
        ],
    },
)
