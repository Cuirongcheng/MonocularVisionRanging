"""Standardized interfaces for extensions."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import collections


Arg = collections.namedtuple('Arg', ('name', 'type', 'description',))


class CliExtension(object):

    """This object represents the interface that extensions must implement."""

    # Name must be a unique for the extension. It will become a CLI argument.
    name = 'extension'
    # Description must be a short explaination of the extensino.
    description = 'A CLI Extension.'
    # Arguments must be an iterable of Arg like objects.
    # Arguments will automatically be prefixed with the name from above when
    # they appear on the CLI. However, they will not be prefixed when they are
    # passed into the optimize metehod. All dashes are converted to underscores
    # when passing args to optimize.
    arguments = (Arg('num-tries', int, 'Number of times to try something.'),)

    @staticmethod
    def optimize(node, *args, **kwargs):
        """Run the optimizer for the given node.

        Arguments given on the CLI will be passed in as keyword arguments.
        """
        raise NotImplementedError()
