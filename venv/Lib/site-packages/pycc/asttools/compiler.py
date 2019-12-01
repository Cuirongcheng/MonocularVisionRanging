"""Utilities for compiling AST nodes."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import ast
import io
import time

from astkit.render import SourceCodeRenderer

from .. import pycompat


def _code_to_bytecode_py2(code):
    """Get bytecode for PY2.

    This implementation borrows heavily from the standard lib implementation
    in the py_compile.compile function.
    """
    # Importing in this function because it only contains useful data when
    # loaded in a PY2 environment.
    import py_compile
    import marshal

    bytecode = io.BytesIO()
    # NOTE: Intentionally not using the BytesIO initializer to write the inital
    # bytes. Initializing the objects with '\0\0\0\0' resulted in no bytes
    # being written to the buffer. Instead, use the write method explicitly to
    # write the placeholder for the magic number.
    bytecode.write(str('\0\0\0\0'))
    py_compile.wr_long(bytecode, pycompat.long(time.time()))
    bytecode.write(marshal.dumps(code))
    bytecode.seek(0, 0)
    bytecode.write(py_compile.MAGIC)
    return bytecode.getvalue()


def _code_to_bytecode_py3(code):
    """Get bytecode for PY3.

    This implementation borrows heavily from the standard lib implementation
    in the py_compile.compile function.
    """
    # Importing in this function because it only contains useful data when
    # loaded in a PY# environment.
    import py_compile
    import marshal

    bytecode = io.BytesIO()
    bytecode.write(str('\0\0\0\0'))
    py_compile.wr_long(bytecode, pycompat.long(time.time()))
    py_compile.wr_long(bytecode, pycompat.long(0))
    bytecode.write(marshal.dumps(code))
    bytecode.seek(0, 0)
    bytecode.write(py_compile.MAGIC)
    return bytecode.getvalue()


def _code_to_bytecode_py34(code):
    """Get bytecode for PY34.

    This implementation leverages the functions used by the new py_compile
    found in the importlib._bootstrap module.
    """
    # Importing in this function because it only exsists in a PY34 environment.
    import importlib._bootstrap
    return importlib._bootstrap._code_to_bytecode(code, time.time())


def _code_to_bytecode(code):
    """Get bytecode from a code object."""
    if pycompat.PY2:

        return _code_to_bytecode_py2(code)

    if pycompat.PY3 and pycompat.VERSION.minor < 4:

        return _code_to_bytecode_py3

    return _code_to_bytecode_py34(code)


class ByteCodeCompiler(object):

    """Compiler which generates Python bytecode."""

    def __call__(self, node, location='<AST>'):
        """Compile the AST into bytecode."""
        ast.fix_missing_locations(node)
        codeobject = compile(node, location, 'exec')
        return _code_to_bytecode(codeobject)


class SourceCodeCompiler(object):

    """Compiler which generates new Python source code from an AST."""

    def __call__(self, node):
        """Compile the AST into source code."""
        return SourceCodeRenderer.render(node)
