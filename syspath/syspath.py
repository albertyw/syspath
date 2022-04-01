import inspect
from pathlib import Path
import sys


def _append_path(new_path: Path) -> None:
    """ Given a Path, append it to sys.path """
    for path_str in sys.path:
        path = Path(path_str).resolve()
        if new_path == path:
            return
    sys.path.append(str(new_path))


def _caller_path(index: int) -> Path:
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
    path = Path(filename).resolve().parent
    return path


def get_current_path(index: int = 2) -> Path:
    """
    Get the caller's path to sys.path
    If the caller is a CLI through stdin, the current working directory is used
    """
    try:
        path = _caller_path(index)
    except RuntimeError:
        path = Path.cwd()
    return path


def append_current_path(index: int = 3) -> Path:
    """
    Append the result of current_path to sys.path
    If the caller is a CLI through stdin, the current working directory is used
    """
    path = get_current_path(index=index)
    _append_path(Path(path))
    return path


def get_git_root(index: int = 3) -> Path:
    """
    Get the path of the git root directory of the caller's file
    Raises a RuntimeError if a git repository cannot be found
    """
    path = Path(get_current_path(index=index))
    while True:
        git_path = path / '.git'
        if git_path.is_dir():
            return path
        if path.parent == path:
            raise RuntimeError("Cannot find git root")
        path = path.parent


def append_git_root(index: int = 4) -> Path:
    """
    Append the result of get_git_root to sys.path
    Raises a RuntimeError if a git repository cannot be found
    """
    path = get_git_root(index=index)
    _append_path(Path(path))
    return path


def get_parent_path(index: int = 2) -> Path:
    """
    Get the caller's parent path to sys.path
    If the caller is a CLI through stdin, the parent of the current working
    directory is used
    """
    try:
        path = _caller_path(index)
    except RuntimeError:
        path = Path.cwd()
    path = path.parent.resolve()
    return path


def append_parent_path(index: int = 3) -> Path:
    """
    Append the result of parent_path to sys.path
    If the caller is a CLI through stdin, the parent of the current working
    directory is used
    """
    path = get_parent_path(index=index)
    _append_path(Path(path))
    return path
