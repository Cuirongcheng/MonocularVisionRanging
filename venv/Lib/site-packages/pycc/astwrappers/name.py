"""Wrappers for ast.Name nodes."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import ast

from ..asttools import references as reftools
from ..asttools import name as nametools
from ..asttools import scope as scopetools
from ..asttools import visitor as visitortools


class NameGenerator(visitortools.NodeVisitorIter, nametools.NameVisitorMixin):

    """Visitor which produces Name objects."""

    def visit(self):
        """Produce Name objects from a NameVisitorMixin."""
        return (
            Name(n)
            for n in super(NameGenerator, self).visit()
        )


class Name(object):

    """Wrapper for an ast.Name node for ease of use."""

    __slots__ = (
        '_node',
        '_scope',
        '_declaration',
        '_declaration_scope',
        '_source',
    )

    def __init__(self, node):
        """Initialize the object with as ast.Name node."""
        if not isinstance(node, ast.Name):

            raise TypeError("Node must be an ast.Name.")

        self._node = node
        self._scope = scopetools.parent_scope(self._node)
        self._declaration = nametools.declaration(self._node)
        self._source = nametools.name_source(self._node, self._declaration)
        self._declaration_scope = None
        if self._source is not nametools.NAME_SOURCE.BUILTIN:

            self._declaration_scope = scopetools.parent_scope(
                self._declaration,
            )

    @property
    def node(self):
        """Get the raw ast.Name node."""
        return self._node

    @property
    def declaration(self):
        """Get the first declaration of the Name."""
        return self._declaration

    @property
    def source(self):
        """Get the asttools.name.NAME_SOURCE of the Name."""
        return self._source

    @property
    def token(self):
        """Get the string which represents the Name."""
        return self._node.id

    @property
    def uses(self):
        """Get an iterable of all uses of the name.

        If the source is asttools.name.NAME_SOURCE.BUILTIN this iterable will
        contain all uses of the name in the module. Otherwise only uses within
        the lexical scope of the declaration are contained within the iterable.
        """
        search_path = self._declaration_scope
        if search_path is None:

            search_path = reftools.get_top_node(self._node)

        return (
            n for n in NameGenerator(search_path).visit()
            if n == self
        )

    @property
    def assignments(self):
        """Get an iterable of all assignments to a name.

        The scoping rules for this method are identical to that which produces
        an iterable of name uses.
        """
        return (
            n for n in self.uses
            if isinstance(n.node.ctx, ast.Store) or
            isinstance(n.node.ctx, ast.Param)
        )

    @property
    def constant(self):
        """True if name is assigned to only once within its lexical scope."""
        # Built in names are never assigned to. Using == 1 to compensate for
        # those names with 0 assignments.
        return len(tuple(self.assignments)) == 1

    def __repr__(self):
        """Get a string repr of the Name."""
        return '<Name {0} - {1}>'.format(
            self._node.id,
            self._source,
        )

    def __lt__(self, other):
        """Less than for Name which compares the string token.

        Input may be an ast.Name node or another Name object.
        """
        if isinstance(other, ast.Name):

            return self._node.id < other.id

        if not isinstance(other, Name):

            raise TypeError("Other must be a Name object or ast.Name node.")

        return self.token < other.token

    def __gt__(self, other):
        """Greater than for Name which negates the less than implementation."""
        return not self.__lt__(other)

    def __eq__(self, other):
        """Equal for Name which compares the string token and declaration.

        Input may be an ast.Name node or another Name object.
        """
        if isinstance(other, ast.Name):

            other = Name(other)

        if not isinstance(other, Name):

            raise TypeError("Other must be a Name object or ast.Name node.")

        return (
            self.token == other.token and
            self.declaration == other.declaration
        )

    def __ne__(self, other):
        """Not equal for Name which negates the equal implementation."""
        return not self.__eq__(other)

    def __le__(self, other):
        """Less than equal for Name."""
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        """Greater than equal for Name."""
        return self.__gt__(other) or self.__eq__(other)

    def __hash__(self):
        """Hash for Name which combines the token and declaration."""
        return hash((self.token, self.declaration))
