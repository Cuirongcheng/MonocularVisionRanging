"""Utilities for getting and using extensions."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import pkg_resources


def iter_extensions():
    """Get an iterable of extensions."""
    for extension in pkg_resources.iter_entry_points('pycc.optimizers'):

        yield extension.load()


def register_extensions(parser):
    """Register the CLI args for all extensions using the given parser."""
    for extension in iter_extensions():

        parser.add_argument(
            '--{0}'.format(extension.name),
            dest=extension.name,
            action='store_true',
            help=extension.description,
        )
        for arg in extension.arguments:

            if arg.type is bool:

                parser.add_argument(
                    '--{0}-{1}'.format(extension.name, arg.name),
                    dest='{0}_{1}'.format(extension.name, arg.name),
                    action='store_true',
                    help=arg.description,
                )

            else:

                parser.add_argument(
                    '--{0}-{1}'.format(extension.name, arg.name),
                    type=arg.type,
                    help=arg.description,
                )


def execute(args, node):
    """Run the enabled extensions."""
    args_dict = vars(args)
    possible_extensions = []
    for key in args_dict:

        if args_dict[key] is True:

            possible_extensions.append(key)

    enabled_extensions = (
        ext for ext in iter_extensions()
        if ext.name in possible_extensions
    )

    for ext in enabled_extensions:

        kwargs = {}
        for arg in ext.arguments:

            val = args_dict.get(
                '{0}-{1}'.format(ext.name, arg.name).replace('-', '_'),
                None,
            )

            if val is not None:

                kwargs[arg.name.replace('-', '_')] = val

        ext.optimize(node, **kwargs)
