# python comes with a builtin module called functools
# functools is a module that provides functions for higher order functions, that is functions that act on or return other functions
from functools import lru_cache
from functools import singledispatch
from functools import partial
import urllib.request
import urllib.error

# lr_cache: 1. It is a decorator that wraps a function with a memoizing callable that saves up to the maxsize most recent calls.


@lru_cache(maxsize=24, typed=True)
def get_webpage(module):
    """
    Gets the specified Python module web page
    """
    webpage = "https://docs.python.org/3/library/{}.html".format(module)
    try:
        with urllib.request.urlopen(webpage) as request:
            return request.read()
    except urllib.error.HTTPError:
        return None

# partial: 1. It is a function that returns a new partial object which when called will behave like func called with the positional arguments args and keyword arguments keywords.


@singledispatch
def add(x, y):
    return x + y


p_add = partial(add, 10)
print(p_add(20))
# or
run(p_add, 20)

# singledispatch: 1. It is a generic function decorator that allows to register multiple functions as the implementation of a single type.
# overloading add method that accepts first parameter as int and second as float


@add.register(int)
@add.register(float)
def _(a, b):
    return a+b

# wraps: 1. It is a decorator for updating the attributes of the wrapping function(func) to those of the original function(wrapped).
