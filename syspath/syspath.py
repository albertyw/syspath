import inspect
import os
import sys


def append_path(path):
    """ Given a path string, append it to sys.path """
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


def get_current_path(index=2):
    """
    Get the caller's path to sys.path
    If the caller is a CLI through stdin, the current working directory is used
    """
    try:
        path = caller_path(index)
    except RuntimeError:
        path = os.getcwd()
    return path


def append_current_path(index=3):
    """
    Append the result of current_path to sys.path
    If the caller is a CLI through stdin, the current working directory is used
    """
    path = get_current_path(index=index)
    append_path(path)
    return path


def get_git_root(index=3):
    """
    Get the path of the git root directory of the caller's file
    Raises a RuntimeError if a git repository cannot be found
    """
    path = get_current_path(index=index)
    while True:
        git_path = os.path.join(path, '.git')
        if os.path.isdir(git_path):
            return path
        if os.path.dirname(path) == path:
            raise RuntimeError("Cannot find git root")
        path = os.path.split(path)[0]


def append_git_root(index=4):
    """
    Append the result of get_git_root to sys.path
    Raises a RuntimeError if a git repository cannot be found
    """
    path = get_git_root(index=index)
    append_path(path)
    return path
