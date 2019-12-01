"""Common utilities for CLI modules."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import collections
import os
import sys

from ..asttools import parse
from .extensions import utils


def register_arguments(parser):
    """Add arguments required for all CLI tools."""
    parser.add_argument(
        '--source',
        required=True,
        help='Path to load the Python source from.',
    )
    parser.add_argument(
        '--destination',
        required=False,
        help='Path to place the optimized result or "stdout".',
    )

    utils.register_extensions(parser)

    return parser


PySource = collections.namedtuple('PySource', ('node', 'path'))


def abspath(path):
    """Resolve a path to an absolute path."""
    return os.path.realpath(
        os.path.expanduser(
            os.path.expandvars(
                path,
            ),
        ),
    )


def load_dir(path):
    """Get an iterable of PySource from the given directory."""
    for root, subdirs, files in os.walk(abspath(path)):

        files = (abspath(os.path.join(root, fname)) for fname in files)
        files = (fname for fname in files if fname.endswith('.py'))
        for file_name in files:

            with open(file_name, 'r') as file_handle:

                source = file_handle.read()
                yield PySource(parse.parse(source), file_name)


def load_path(path):
    """Get an iterable of PySource from the given path."""
    path = abspath(path)

    if os.path.isdir(path):

        return load_dir(path)

    with open(path, 'r') as file_handle:

        return (PySource(parse.parse(file_handle.read()), path),)


def run_optimizers(args):
    """Optimize each of an iterable of PySource objects."""
    sources = tuple(load_path(args.source))
    for source in sources:

        utils.execute(args, source.node)

    return sources


def write_result(body, path, path_override=None):
    """Write the body into a file in path or path_override."""
    dest = abspath(path)
    if path_override is not None:

        if path_override == 'stdout':

            sys.stdout.write(body)
            sys.stdout.write('\n')
            return None

        file_name = os.path.split(path)[1]
        dest = os.path.join(abspath(path_override), file_name)

    # Lazy create destination directories if they don't already exist.
    dest_dir = os.path.split(dest)[0]
    if not os.path.isdir(dest_dir):

        os.makedirs(dest_dir, exists_ok=True)

    with open(dest, 'wb') as output:

        output.write(body)
