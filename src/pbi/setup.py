#!/usr/bin/env python

import os
import re

from setuptools import setup, find_packages

extension_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(extension_path, 'azext_pbi', 'version.py'), 'r') as file:
    VERSION = re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]', file.read(), re.MULTILINE).group(1)

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = [
]

setup(
    name='azure-pbi',
    version=VERSION,
    description='PowerBI CLI',
    long_description='PowerBI CLI',
    license='MIT',
    author='Andrei Zhozhin',
    author_email='email@example.com',
    url='',
    classifiers=CLASSIFIERS,
    package_data={'azext_pbi': ['azext_metadata.json']},
    packages=find_packages(),
    install_requirements=DEPENDENCIES
)
