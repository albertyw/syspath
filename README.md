SysPath
=======

[![PyPI](https://img.shields.io/pypi/v/syspath.svg)]( https://pypi.python.org/pypi/syspath/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/syspath)
![PyPI - License](https://img.shields.io/pypi/l/syspath)

[![Build Status](https://drone.albertyw.com/api/badges/albertyw/syspath/status.svg)](https://drone.albertyw.com/albertyw/syspath)
[![Dependency Status](https://pyup.io/repos/github/albertyw/syspath/shield.svg)](https://pyup.io/repos/github/albertyw/syspath/)
[![Code Climate](https://codeclimate.com/github/albertyw/syspath/badges/gpa.svg)](https://codeclimate.com/github/albertyw/syspath)
[![Code Climate Test Coverage](https://codeclimate.com/github/albertyw/syspath/badges/coverage.svg)](https://codeclimate.com/github/albertyw/syspath/coverage)


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
python setup.py develop
pip install -r requirements-test.txt
flake8
mypy syspath --strict
coverage run -m unittest
coverage report
flake8
```

Publishing
----------

```bash
pip install twine
python setup.py sdist bdist_wheel
twine upload dist/*
```
