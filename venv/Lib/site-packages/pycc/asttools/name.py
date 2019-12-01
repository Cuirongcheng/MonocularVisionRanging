"""Utilities for working with ast.Name nodes."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import ast
import itertools

from .. import enum
from .. import pycompat
from . import references
from . import scope


NAME_SOURCE = enum.Enum(('DEFINED', 'ADOPTED', 'IMPORTED', 'BUILTIN'))


def declaration(node, start=None):
    """Find the AST node where a name is first declared.

    The search begins in the same scope as the given ast.Name node. To search
    within a custom path pass in an AST node as the 'start' parameter.
    """
    if not isinstance(node, ast.Name):

        raise TypeError('The input must be an AST.Name node.')

    scopes = [start or scope.parent_scope(node)]

    while len(scopes) > 0:

        current_scope = scopes.pop()
        for child in ast.iter_child_nodes(current_scope):

            if (
                isinstance(child, ast.Import) or
                isinstance(child, ast.ImportFrom)
            ):

                for a in child.names:

                    # 'names' always contains ast.alias.
                    if (
                        (a.asname is not None and node.id == a.asname) or
                        (a.asname is None and node.id == a.name)
                    ):

                        return child

            if isinstance(child, ast.Assign):

                target = child.targets[0]

                if isinstance(target, ast.Name) and target.id == node.id:

                    return child

                if isinstance(target, ast.Tuple):

                    for elt in target.elts:

                        if isinstance(elt, ast.Name) and elt.id == node.id:

                            return child

            if (
                (
                    isinstance(child, ast.FunctionDef) or
                    isinstance(child, ast.ClassDef)
                ) and child.name == node.id
            ):

                return child

            if isinstance(child, ast.arguments):

                args = ()
                if pycompat.PY2:

                    args = itertools.chain(
                        (child.vararg, child.kwarg,),
                        (c.id for c in child.args),
                    )

                if pycompat.PY3 and pycompat.VERSION.minor < 4:

                    args = itertools.chain(
                        (child.vararg, child.kwarg,),
                        (c.arg for c in child.args),
                        (c.arg for c in child.kwonlyargs),
                    )

                if pycompat.PY3 and pycompat.VERSION.minor > 3:

                    args = itertools.chain(
                        (
                            child.vararg.arg
                            if child.vararg is not None else None,

                            child.kwarg.arg
                            if child.kwarg is not None else None,
                        ),
                        (c.arg for c in child.args),
                        (c.arg for c in child.kwonlyargs),
                    )

                for arg in args:

                    if arg == node.id:

                        return child

        if current_scope.parent is None:

            return None

        scopes.append(current_scope.parent)


def name_source(node, declared=None):
    """Get the NAME_SOURCE for the given name.

    If 'declared' is not given it will be derived from the given name.
    """
    if not isinstance(node, ast.Name):

        raise TypeError('The input must be an AST.Name node.')

    declared = declared or declaration(node)

    if declared is None:

        return NAME_SOURCE.BUILTIN

    if (
        isinstance(declared, ast.Import) or
        isinstance(declared, ast.ImportFrom)
    ):

        return NAME_SOURCE.IMPORTED

    if (
        scope.parent_scope(node) is
        scope.parent_scope(declared)
    ):

        return NAME_SOURCE.DEFINED

    return NAME_SOURCE.ADOPTED


class NameVisitorMixin(object):

    """Generates ast.Name nodes for a given tree.

    Surrogate ast.Name nodes will be given for names created by other actions
    such as function/definitions and function parameters.
    """

    def visit_Name(self, node):
        """Return ast.Name values unaltered."""
        return node

    def visit_alias(self, node):
        """Get a surrogate name using an alias."""
        return references.copy_location(
            ast.Name(
                id=(
                    node.asname
                    if node.asname is not None
                    else node.name
                ),
                ctx=ast.Store(),
            ),
            node,
        )

    def visit_FunctionDef(self, node):
        """Get a surrogate name from a function or class definition."""
        self.generic_visit(node)
        return references.copy_location(
            ast.Name(
                id=node.name,
                ctx=ast.Store(),
            ),
            node,
        )

    visit_ClassDef = visit_FunctionDef

    def visit_Global(self, node):
        """Get a surrogate name from a global or nonlocal statement."""
        for raw_name in node.names:

            yield references.copy_location(
                ast.Name(
                    id=raw_name,
                    ctx=ast.Store(),
                ),
                node,
            )

    visit_Nonlocal = visit_Global

    def visit_arguments(self, node):
        """Get surrogate name nodes from function arguments.

        This method only handles the *args and **kwargs variable names. In PY2
        the rest of the children for this node names. In PY3+ they are args
        and handled by another visitor.
        """
        # PY2 vararg and kwarg are raw strings which represent the tokens of
        # the variable name chosen. These have become arg nodes in PY33.
        if pycompat.PY2 or (pycompat.PY3 and pycompat.VERSION.minor < 4):

            if node.vararg is not None:

                yield references.copy_location(
                    ast.Name(
                        id=node.vararg,
                        ctx=ast.Param(),
                    ),
                    node,
                )

            if node.kwarg is not None:

                yield references.copy_location(
                    ast.Name(
                        id=node.kwarg,
                        ctx=ast.Param(),
                    ),
                    node,
                )

    def visit_arg(self, node):
        """Get a surrogate name from an argument specification."""
        return references.copy_location(
            ast.Name(
                id=node.arg,
                ctx=ast.Param()
            ),
            node,
        )
