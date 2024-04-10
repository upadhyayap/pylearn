# Regular imports
# example: import sys
# multiple modules can be imported using a single import statement
# example: import sys, os
# renaming a module while importing
# example: import sys as system
# submodules can be imported using the dot operator
# example: import os.path

# importing a part of a module
# example: from os import path
# importing multiple parts of a module
# example: from functools import lru_cache
# we could have imported the whole module using import functools but we only needed lru_cache in this case we would beed to call the function as functools.lru_cache
# but in the above case we can call the function directly as lru_cache
# importing all the functions from a module using *
# example: from functools import *

# importing a module from a package
# example: from package_name import module_name
# importing a module from a subpackage
# example: from package_name.subpackage_name import module_name


# optional imports
# example:
import importlib.util
import importlib
try:
    from urlparse import urljoin
    from urllib2 import urlopen
except ImportError:
    # Python 3
    from urllib.parse import urljoin
    from urllib.request import urlopen

# Local imports


def square_root(a):
    # This import is into the square_root functions local scope
    import math
    return math.sqrt(a)


# importlib: Python provides the importlib package as part of its standard library of modules.
# Its purpose is to provide the implementation of Python’s import statement
# (and the _import_() function). In addition, importlib gives the programmer
# the ability to create their own custom objects (AKA an importer)
# that can be used in the import process.

# takes a module name as an argument, imports the module and returns the module object
def dynamic_import(module):

    return importlib.import_module(module)


module = dynamic_import('foo')
module.main()

module_two = dynamic_import('bar')
module_two.main()


# check if a module can be imported
def check_module(module_name):
    """
    Checks if module can be imported without actually
    importing it
    """

    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print('Module: {} not found'.format(module_name))
        return None
    else:
        print('Module: {} can be imported!'.format(module_name))
        return module_spec


def import_module_from_spec(module_spec):
    """
    Import the module via the passed in module specification
    Returns the newly imported module
    """

    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


module_spec = check_module('fake_module')
module_spec = check_module('collections')
if module_spec:
    module = import_module_from_spec(module_spec)
    print(dir(module))
