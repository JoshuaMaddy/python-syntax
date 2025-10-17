# This file demonstrates the import syntax. It will not run.
# Imports are executed top down, and order *can* matter in some specific cases, 
# particularly in cyclical imports.

# Importing a Class/method/variable from a module
from pathlib import Path

# Importing from a sub-module
from os.path import pathsep

# Importing from a relative file/module
# *This is not usually recommended* 
from .methods import multiply
from .my_module import my_module_func
from ..syntax.truthiness import any_object_with__bool__

# The preferred 'absolute' way of importing
from syntax.methods import multiply
from syntax.my_module import my_module_func
from syntax.truthiness import any_object_with__bool__


# importing a whole module
import re

