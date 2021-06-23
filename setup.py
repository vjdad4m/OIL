#!/usr/bin/env python3

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='OIL',
    version='0.1',
    description='Open Image Labeling library',
    author='Adam Vajda',
    license='MIT',
    long_description=long_description,
    packages=['OIL'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=['numpy', 'opencv-python', 'pygame'],
    python_requires='>=3.8',
    include_package_data=True
    )