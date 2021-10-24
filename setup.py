#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path
from typing import Any, Dict


# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

about: Dict[str, Any] = {}
with open(path.join(here, 'syspath', '__version__.py')) as f:
    exec(f.read(), about)

setup(
    name='syspath',

    version=about['__version__'],

    description='Easily add common paths to sys.path',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/albertyw/syspath',

    author='Albert Wang',
    author_email='git@albertyw.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',

        'Typing :: Typed',
    ],

    keywords='',

    package_data={"syspath": ["py.typed"]},
    packages=find_packages(exclude=["tests"]),

    install_requires=[],

    test_suite="syspath.tests",

    # testing requires flake8 and coverage but they're listed separately
    # because they need to wrap setup.py
    extras_require={
        'dev': [],
        'test': [],
    },
)
