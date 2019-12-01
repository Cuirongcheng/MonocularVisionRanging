"""Core extension for constant in-lining."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from . import interfaces
from ...optimizers import constant


class ConstantInlineExtension(interfaces.CliExtension):

    """A CLI extension which enables constant in-lining."""

    name = 'constants'
    description = 'Inline constant values.'
    arguments = ()

    @staticmethod
    def optimize(node):
        """In-line all constant values."""
        constant.optimize(node)
