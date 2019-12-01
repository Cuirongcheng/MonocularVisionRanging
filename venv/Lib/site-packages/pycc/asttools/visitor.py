"""Utilities for iterating over child AST nodes."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import ast
import collections

from . import references


class NodeVisitor(object):

    """Alternate visitor implementation.

    This NodeVisitor interface differs slightly from the standard
    implementation. Primarily, the AST node to visit is given during
    initialization rather than at visit time. This has the effect of making
    instances of this NodeVisitor only usable with one AST and only one time.
    Subsequent calls will have no effect.

    This implementation provides a "generic_visit" method which can be used
    within individual visit methods in order to evaluate all the children of
    a node. This method may be used but should not be overwritten.

    This implementation provides no return value from the visit method. This
    makes it not well suited for use in a compiler.

    The benefit of this implementation is that it does not leverage function
    recursion. Rough benchmarks show this to be somewhere between two and four
    times faster than the default implementation.
    """

    def __init__(self, node):
        """Seed the visitor with an AST node.

        All calls to visit will begin with this node.
        """
        self._node = node
        self._nodes = collections.deque((self._node,))

    def generic_visit(self, node):
        """Queue up all child nodes for visiting."""
        self._nodes.extend(ast.iter_child_nodes(node))

    def visit(self):
        """Visit the nodes.

        This method will always start with the node given at initialization.
        """
        while len(self._nodes) > 0:

            current = self._nodes.popleft()
            method = 'visit_' + current.__class__.__name__
            visitor = getattr(self, method, self.generic_visit)
            visitor(current)


class NodeVisitorIter(NodeVisitor):

    """NodeVisitor subclass which produces all visitor return values.

    Unlike the base NodeVisitor in this module, this subclass returns an
    iterable from the visit method which contains all values returned by
    individual visit methods.
    """

    def visit(self):
        """Visit the nodes.

        This method returns an iterable of values returned by visitor methods.

        If multiple values are returned by a visitor they will all be included
        in the resulting iterable.
        """
        while len(self._nodes) > 0:

            current = self._nodes.popleft()
            method = 'visit_' + current.__class__.__name__
            visitor = getattr(self, method, self.generic_visit)
            value = visitor(current)
            if value is not None:

                try:

                    for v in value:

                        yield v

                except TypeError:

                    yield value


class NodeTransformer(NodeVisitor):

    """Alternate implementation of ast.NodeTransformer.

    This implementation subclasses the non-recursive NodeVisitor from this
    module. This implementation should behave identically to that of the
    standard behaviour in how it replaces nodes.

    However this implementation differs in behaviour as layed out in the
    documentation for the non-recursive NodeVisitor. Another major difference
    in behaviour is that the visit method does not return the modified AST.
    Instead you must rely on the fact that the node is modified in place. The
    standard implementation also modifies the AST in place, it simply returned
    the resulting value for convenience.

    This implementation relies on the parent and sibling references provided
    by the asttools.references module.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the visitor."""
        super(NodeTransformer, self).__init__(*args, **kwargs)
        self._modified = False

    @property
    def modified(self):
        """Determine whether or not the source was altered."""
        return self._modified

    def _replace(self, new, old):
        """Replace a node in the AST with a new one."""
        # Don't replace nodes that are identical.
        if new is old:

            return None

        self._modified = True
        parent = old.parent
        if parent is None:

            raise ValueError("Attempting to replace the top level node.")

        for field, original in ast.iter_fields(parent):

            if isinstance(original, ast.AST) and original is old:

                if new is None:

                    delattr(parent, field)
                    continue

                new = references.copy_location(new, old)
                setattr(parent, field, new)
                return None

            if isinstance(original, list) and old in original:

                if new is None:

                    original.remove(old)
                    continue

                new = references.copy_location(new, old)
                original[original.index(old)] = new
                return None

    def visit(self):
        """Visit the nodes."""
        while len(self._nodes) > 0:

            current = self._nodes.popleft()
            method = 'visit_' + current.__class__.__name__
            visitor = getattr(self, method, None)
            if visitor is not None:

                self._replace(visitor(current), current)
                continue

            self.generic_visit(current)
