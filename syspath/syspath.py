import inspect
import os
import sys


def append_path(path):
    sys.path.append(path)


def caller_path(index):
    """ Get the caller's file path, by the index of the stack """
    frame = inspect.stack()[index]
    module = inspect.getmodule(frame[0])
    filename = module.__file__
    return os.path.realpath(filename)
