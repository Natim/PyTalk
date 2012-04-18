# -*- coding: utf-8 -*-

# tools.py
# Part of enum, a package providing enumerated types for Python.
#
# Copyright © 2007 Ben Finney
# This is free software; you may copy, modify and/or distribute this work
# under the terms of the GNU General Public License, version 2 or later
# or, at your option, the terms of the Python license.

""" Helper tools for unit tests
"""

import os
import sys

test_dir = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.dirname(test_dir)
if not test_dir in sys.path:
    sys.path.insert(1, test_dir)
if not code_dir in sys.path:
    sys.path.insert(1, code_dir)


def make_params_iterator(default_params_dict):
    """ Make a function for generating test parameters """

    def iterate_params(params_dict=None):
        """ Iterate a single test for a set of parameters """
        if not params_dict:
            params_dict = default_params_dict
        for key, params in params_dict.items():
            yield key, params

    return iterate_params
