"""CLI tool for generating optimized .pyc files."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse

from ..asttools import compiler
from . import common


def parse_args():
    """Get user input."""
    parser = argparse.ArgumentParser(description='PyCC Compiler')
    common.register_arguments(parser)
    return parser.parse_args()


def main():
    """Generate optimized bytecode."""
    args = parse_args()
    optimized = common.run_optimizers(args)
    bc_compiler = compiler.ByteCodeCompiler()

    for module in optimized:

        bytecode = bc_compiler(
            module.node,
            location=common.abspath(module.path)
        )
        common.write_result(
            body=bytecode,
            path=module.path + 'c',
            path_override=args.destination
        )


if __name__ == '__main__':

    main()
