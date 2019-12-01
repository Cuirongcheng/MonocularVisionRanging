"""CLI tool for generating optimized Python source code."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse

from ..asttools import compiler
from . import common


def parse_args():
    """Get user input."""
    parser = argparse.ArgumentParser(description='PyCC Transformer')
    common.register_arguments(parser)
    return parser.parse_args()


def main():
    """Generate optimized source code."""
    args = parse_args()
    optimized = common.run_optimizers(args)
    source_compiler = compiler.SourceCodeCompiler()

    for module in optimized:

        bytecode = source_compiler(
            module.node
        )
        common.write_result(
            body=bytecode,
            path=module.path.replace('.py', '') + '_optimized.py',
            path_override=args.destination
        )


if __name__ == '__main__':

    main()
