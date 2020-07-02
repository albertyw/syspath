import inspect
import os
import sys


def _append_path(new_path: str) -> None:
    """ Given a path string, append it to sys.path """
    for path in sys.path:
        path = os.path.abspath(path)
        if new_path == path:
            return
    sys.path.append(new_path)


def _caller_path(index: int) -> str:
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


def get_current_path(index: int = 2) -> str:
    """
    Get the caller's path to sys.path
    If the caller is a CLI through stdin, the current working directory is used
    """
    try:
        path = _caller_path(index)
    except RuntimeError:
        path = os.getcwd()
    return path


def append_current_path(index: int = 3) -> str:
    """
    Append the result of current_path to sys.path
    If the caller is a CLI through stdin, the current working directory is used
    """
    path = get_current_path(index=index)
    _append_path(path)
    return path


def get_git_root(index: int = 3) -> str:
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


def append_git_root(index: int = 4) -> str:
    """
    Append the result of get_git_root to sys.path
    Raises a RuntimeError if a git repository cannot be found
    """
    path = get_git_root(index=index)
    _append_path(path)
    return path


def get_parent_path(index: int = 2) -> str:
    """
    Get the caller's parent path to sys.path
    If the caller is a CLI through stdin, the parent of the current working
    directory is used
    """
    try:
        path = _caller_path(index)
    except RuntimeError:
        path = os.getcwd()
    path = os.path.abspath(os.path.join(path, os.pardir))
    return path


def append_parent_path(index: int = 3) -> str:
    """
    Append the result of parent_path to sys.path
    If the caller is a CLI through stdin, the parent of the current working
    directory is used
    """
    path = get_parent_path(index=index)
    _append_path(path)
    return path
