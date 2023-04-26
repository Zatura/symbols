#!/usr/bin/env python
from setuptools import setup, find_packages

long_description_content_type = 'text/markdown'
long_description = open('README.md').read()

setup(
    name='symbols',
    version='0.5.0',
    author='Matheus Tura',
    author_website='zatura.me',
    packages=find_packages(),
    long_description='\n'.join(long_description),
    long_description_content_type="text/markdown",
    install_requires=[],
    url='https://github.com/zatura/symbols',
    description='A library for cryptocurrency ticker symbols manipulation',
    license="GPL-3.0",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries"
    ],
    python_requires='>=3.6',
)
