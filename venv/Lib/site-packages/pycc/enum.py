"""Enum implementation."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


class EnumValue(object):

    """An object which represents a value in an Enum."""

    def __init__(self, name):
        """Initialize the value with the name."""
        self._name = name

    def __repr__(self):
        """Get the name used to represent the value."""
        return self._name


class Enum(object):

    """An object which acts like an Enum.

    Each enum attribute has a unique object value which makes it possible to
    use the 'is' operator for comparisons.
    """

    def __init__(self, names):
        """Initialize the enum with an iterable of names."""
        self._names = tuple(names)
        for name in self._names:
            setattr(self, name, EnumValue(name))

    def __iter__(self):
        """Return an iterator of Enum values for use with the 'in' operator."""
        return (getattr(self, name) for name in self._names)
