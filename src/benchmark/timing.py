from functools import wraps
from time import time
from typing import Callable, TypeVar

from src.shared import Logger


__all__ = [
    "timing",
]


T = TypeVar("T")


def timing(func: Callable[..., T]):
    @wraps(func)
    def wrap(*args, **kw):
        ts = time()
        result = func(*args, **kw)
        te = time()
    
        Logger.warning('function: %r with args: [%r, %r] took: %2.4f seconds to complete' % \
            (func.__name__, args, kw, te-ts))
    
        return result
    
    return wrap
