#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path
import footprint

here = path.abspath(path.dirname(__file__))
readme = path.join(here, 'README.md')

with open(readme, encoding='utf-8') as f:
    long_description = f.read()

with open('dependency.txt') as f:
    dependency = list(map(str.strip, f.readlines()))

setup(
    name=footprint.__name__,
    version=footprint.__version__,
    description="A tool of stats whose report a dump of memory analysis",
    long_description=long_description,
    classifiers=[
        "Environment :: Console",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='footprint memory analysis pandas table stats',
    author=footprint.__author__,
    author_email=footprint.__email__,
    url=footprint.__url__,
    zip_safe=False,
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples',
                                    'tests', 'docs', '__pycache__']),
    platforms='unix',
    dependency_links=dependency,
    entry_points={  # no entry-points yet
        'console_scripts': [
            'footprint = footprint:main',
            'mar-footprint = footprint:main'
        ]
    },
)
