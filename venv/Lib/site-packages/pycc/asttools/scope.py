"""Containers for variable scope rules."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import ast

from .. import enum


SCOPE_TYPE = enum.Enum(("MODULE", "FUNCTION", "CLASS"))


def is_scope(node):
    """True if the ast node is a scope else False."""
    if not isinstance(node, ast.AST):

        raise TypeError("The input must be an AST node.")

    return (
        isinstance(node, ast.Module) or
        isinstance(node, ast.FunctionDef) or
        isinstance(node, ast.ClassDef)
    )


def scope_type(node):
    """Get the type of scope represented by a node."""
    if not isinstance(node, ast.AST):

        raise TypeError("The input must be an AST node.")

    if not is_scope(node):

        raise ValueError("Node must be the beginning of a scope.")

    if isinstance(node, ast.Module):

        return SCOPE_TYPE.MODULE

    if isinstance(node, ast.FunctionDef):

        return SCOPE_TYPE.FUNCTION

    if isinstance(node, ast.ClassDef):

        return SCOPE_TYPE.CLASS


def parent_scope(node):
    """Find the AST node that represents the first enclosing scope."""
    if not isinstance(node, ast.AST):

        raise TypeError("The input must be an AST node.")

    node = node.parent if hasattr(node, "parent") else None

    while node is not None:

        if (
            isinstance(node, ast.Module) or
            isinstance(node, ast.FunctionDef) or
            isinstance(node, ast.ClassDef)
        ):

            return node

        node = node.parent

    raise ValueError("No valid scope found in node path.")


def child_scopes(node):
    """Generate child AST nodes that represent lexical scopes."""
    if not isinstance(node, ast.AST):

        raise TypeError("The input must be an AST node.")

    if not is_scope(node):

        raise ValueError("The input must be a lexical scope.")

    for child in ast.iter_child_nodes(node):

        if is_scope(child):

            yield child
