import inspect
import os
import sys


def append_path(path):
    sys.path.append(path)


def caller_path(index):
    """
    Get the caller's file path, by the index of the stack,
    does not work when the caller is stdin through a CLI python
    """
    module = None
    stack = inspect.stack()
    while not module:
        if index >= len(stack):
            raise RuntimeError("Cannot find import path")
        frame = stack[index]
        module = inspect.getmodule(frame[0])
        index += 1
    filename = module.__file__
    path = os.path.dirname(os.path.realpath(filename))
    return path


def append_current_path(index=2):
    """
    Append the caller's path to sys.path
    If the caller is a CLI through stdin, the current working directory is used
    """
    try:
        path = caller_path(index)
    except RuntimeError:
        path = os.getcwd()
    append_path(path)
