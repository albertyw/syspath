SysPath
=======

[![PyPI](https://img.shields.io/pypi/v/syspath.svg)]( https://pypi.python.org/pypi/syspath/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/syspath)
![PyPI - License](https://img.shields.io/pypi/l/syspath)

[![Build Status](https://drone.albertyw.com/api/badges/albertyw/syspath/status.svg)](https://drone.albertyw.com/albertyw/syspath)
[![Maintainability](https://qlty.sh/gh/albertyw/projects/syspath/maintainability.svg)](https://qlty.sh/gh/albertyw/projects/syspath)
[![Code Coverage](https://qlty.sh/gh/albertyw/projects/syspath/coverage.svg)](https://qlty.sh/gh/albertyw/projects/syspath)


SysPath is a package to easily set common paths into `sys.path`. Instead
of having to do a lot of path manipulation to properly import files, a
file can import from SysPath instead.

Installation
------------

```bash
pip install syspath
```

Usage
-----

To append the current file's directory to `sys.path`:

```python
import syspath
syspath.append_current_path()
# or
from syspath import current_path
```

To append the current file's parent directory to `sys.path`:

```python
import syspath
syspath.append_parent_path()
# or
from syspath import parent_path
```

To append the current file's git repository root to `sys.path`:

```python
import syspath
syspath.append_git_root()
# or
from syspath import git_root
```

Each of the shortcut modules also provide a `path` variable that can be
used to get the path added.

Development
-----------

```bash
pip install -e .[test]
ruff check .
mypy .
coverage run -m unittest
coverage report -m
ruff check .
```

Publishing
----------

1.  Update `CHANGELOG.md`
2.  Update `syspath/__version__.py`
3.  Commit, tag with the version number, and push
