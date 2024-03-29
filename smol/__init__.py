__version__ = '0.0.1'

from .paints import *
from .regex import *
from .subproc import *

from . import bin


def load_cli_entry_points():
    import os
    import importlib

    for f in os.listdir(os.path.dirname(__file__)):
        if f.startswith('bin_') and f.endswith('.py'):
            m = os.path.splitext(f)[0]

            module = importlib.import_module('.' + m, 'smol')
            setattr(bin, m[4:], module)

            del globals()[m]

load_cli_entry_points()

del load_cli_entry_points
