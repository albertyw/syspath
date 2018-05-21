SysPath
=======

|PyPI| |Python Versions|

|Codeship Status for albertyw/syspath| |Dependency Status| |Code Climate| |Test Coverage|

SysPath is a package to easily set common paths into ``sys.path``.  Instead of
having to do a lot of path manipulation to properly import files, a file can
import from SysPath instead.

Installation
------------

.. code:: bash

    pip install syspath

Usage
-----

To append the current file's directory to ``sys.path``:

.. code:: python

    import syspath
    syspath.append_current_path()
    # or
    from syspath import current_path

To append the current file's parent directory to ``sys.path``:

.. code:: python

    import syspath
    syspath.append_parent_path()
    # or
    from syspath import parent_path

To append the current file's git repository root to ``sys.path``:

.. code:: python

    import syspath
    syspath.append_git_root()
    # or
    from syspath import git_root

Development
-----------

Syspath should work with both python 2 and 3.

.. code:: bash

    pip install -r requirements-test.txt
    pip install -r requirements-test-python3.txt
    mypy syspath/syspath.py
    coverage run setup.py test
    coverage report
    flake8

Publishing
----------

.. code:: bash

    pip install twine
    python setup.py sdist bdist_wheel
    twine upload dist/*

.. |PyPI| image:: https://img.shields.io/pypi/v/syspath.svg
   :target: https://pypi.python.org/pypi/syspath/
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/syspath.svg
   :target: https://github.com/albertyw/syspath
.. |Codeship Status for albertyw/syspath| image:: https://app.codeship.com/projects/8d31dab0-c698-0135-edff-328cb0679be8/status?branch=master
   :target: https://codeship.com/projects/261214
.. |Dependency Status| image:: https://pyup.io/repos/github/albertyw/syspath/shield.svg
   :target: https://pyup.io/repos/github/albertyw/syspath/
.. |Code Climate| image:: https://codeclimate.com/github/albertyw/syspath/badges/gpa.svg
   :target: https://codeclimate.com/github/albertyw/syspath
.. |Test Coverage| image:: https://codeclimate.com/github/albertyw/syspath/badges/coverage.svg
   :target: https://codeclimate.com/github/albertyw/syspath/coverage
