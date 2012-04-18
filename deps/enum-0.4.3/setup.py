#! /usr/bin/env python
# -*- coding: utf-8 -*-

# setup.py
# Part of enum, a package providing enumerated types for Python.
#
# Copyright © 2007 Ben Finney
# This is free software; you may copy, modify and/or distribute this work
# under the terms of the GNU General Public License, version 2 or later
# or, at your option, the terms of the Python license.

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

main_module_name = 'enum'
main_module = __import__(main_module_name)

description = main_module.__doc__.split('\n\n', 1)

setup(
    name = "enum",
    version = main_module.__version__,
    packages = find_packages(exclude=["test"]),
    package_dir = "",
    py_modules = [main_module_name],

    # setuptools metadata
    zip_safe = True,
    test_suite = "test.test_enum.suite",
    package_data = {
        '': ["LICENSE.*"],
    },

    # PyPI metadata
    author = main_module.__author_name__,
    author_email = main_module.__author_email__,
    description = description[0].strip(),
    license = main_module.__license__,
    keywords = "enum enumerated enumeration",
    url = main_module.__url__,
    long_description = description[1],
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)
