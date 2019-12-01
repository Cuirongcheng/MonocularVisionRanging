"""Optimizer for inlining constant values."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import ast

from ..asttools import name as nametools
from ..asttools import visitor
from ..astwrappers import name as namewrap


def _resolve_constant_value(name):
    """Get the AST node representing the constant value of a name."""
    decl = name.declaration

    if isinstance(decl, ast.Assign):

        target = decl.targets[0]
        value = decl.value

        if isinstance(target, ast.Tuple) and isinstance(value, ast.Tuple):

            for idx, elt in enumerate(target.elts):

                if isinstance(elt, ast.Name) and elt.id == name.token:

                    return value.elts[idx]

        else:

            return value


class ConstantInliner(visitor.NodeTransformer):

    """NodeTransformer which places constant values in-line."""

    def visit_Name(self, node):
        """Replace ast.Name with a value if it is a constant reference."""
        n = namewrap.Name(node)

        # Skip if not loading the value from memory.
        if not isinstance(node.ctx, ast.Load):

            return node

        # Skip if value is not constant.
        if not n.constant or n.node is n.declaration:

            return node

        # Skip if the node represents the initial assignment.
        if n.node is n.declaration:

            return node

        # Skip if the constant value cannot be found.
        if n.source in (
            nametools.NAME_SOURCE.BUILTIN,
            nametools.NAME_SOURCE.IMPORTED,
        ):

            return node

        value = _resolve_constant_value(n)

        # Skip if the value is a complex typ.
        if not (
            isinstance(value, ast.Num) or
            isinstance(value, ast.Str) or
            isinstance(value, ast.Name)
        ):

            return node

        if value is None:

            return node

        return value

    def visit_BinOp(self, node):
        """Perform binary ops if all values are constant."""
        self.generic_visit(node)
        if isinstance(node.op, ast.Add):

            if (
                isinstance(node.left, ast.Num) and
                isinstance(node.right, ast.Num)
            ):

                return ast.Num(n=node.left.n + node.right.n)

            if (
                isinstance(node.left, ast.Str) and
                isinstance(node.right, ast.Str)
            ):

                return ast.Str(s=node.left + node.right)

        if isinstance(node.op, ast.Sub):

            if (
                isinstance(node.left, ast.Num) and
                isinstance(node.right, ast.Num)
            ):

                return ast.Num(n=node.left.n - node.right.n)

        if isinstance(node.op, ast.Mult):

            if (
                isinstance(node.left, ast.Num) and
                isinstance(node.right, ast.Num)
            ):

                return ast.Num(n=node.left.n * node.right.n)

            if (
                isinstance(node.left, ast.Str) and
                isinstance(node.right, ast.Num)
            ):

                return ast.Str(s=node.left * node.right)

        if isinstance(node.op, ast.Div):

            if (
                isinstance(node.left, ast.Num) and
                isinstance(node.right, ast.Num)
            ):

                return ast.Num(n=node.left.n / node.right.n)

        if isinstance(node.op, ast.FloorDiv):

            if (
                isinstance(node.left, ast.Num) and
                isinstance(node.right, ast.Num)
            ):

                return ast.Num(n=node.left.n // node.right.n)

        if isinstance(node.op, ast.Mod):

            if (
                isinstance(node.left, ast.Num) and
                isinstance(node.right, ast.Num)
            ):

                return ast.Num(n=node.left.n % node.right.n)

        if isinstance(node.op, ast.Pow):

            if (
                isinstance(node.left, ast.Num) and
                isinstance(node.right, ast.Num)
            ):

                return ast.Num(n=node.left.n ** node.right.n)

        return node


def optimize(node):
    """Optimize an AST by in-lining constant values."""
    modified = True
    while modified is True:

        inliner = ConstantInliner(node)
        inliner.visit()
        modified = inliner.modified
