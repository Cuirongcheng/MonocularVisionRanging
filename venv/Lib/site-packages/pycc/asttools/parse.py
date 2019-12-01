"""Utilities for generating AST objects from source."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import ast

from . import references


def parse(source, filename='<unknown>', mode='exec'):
    """An ast.parse extension.

    This function behaves identically to the standard ast.parse except that it
    adds parent and sibling references to each node.
    """
    node = ast.parse(source, filename, mode)
    references.add_parent_references(node)
    references.add_sibling_references(node)

    return node
