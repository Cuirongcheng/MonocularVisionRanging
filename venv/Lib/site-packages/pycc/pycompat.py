"""Compatibility helpers for Py2 and Py3."""
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import sys


class VERSION(object):

    """Stand in for sys.version_info.

    The values from sys only have named parameters starting in PY27. This
    allows us to use named parameters for all versions of Python.
    """

    major, minor, micro, releaselevel, serial = sys.version_info

PY2 = VERSION.major == 2
PY25 = PY2 and VERSION.minor == 5
PY26 = PY2 and VERSION.minor == 6
PY27 = PY2 and VERSION.minor == 7
PY3 = not PY2
PY31 = PY3 and VERSION.minor == 1
PY32 = PY3 and VERSION.minor == 2
PY33 = PY3 and VERSION.minor == 3
PY34 = PY3 and VERSION.minor == 4

# Provide a nice range function for py2.
try:
    range = xrange
except NameError:
    pass

# Provide a long type for py3.
try:
    long = long
except NameError:
    long = int
