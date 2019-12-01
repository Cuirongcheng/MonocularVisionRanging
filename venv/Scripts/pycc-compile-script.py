#!D:\WorkSpace\PythonWorkSpace\MonocularVisionRanging\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pycc==2.0.0','console_scripts','pycc-compile'
__requires__ = 'pycc==2.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pycc==2.0.0', 'console_scripts', 'pycc-compile')()
    )
