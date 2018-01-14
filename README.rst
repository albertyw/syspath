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

.. code:: bash

    pip install -r requirements-test.txt
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
.. |Dependency Status| image:: https://gemnasium.com/badges/github.com/albertyw/syspath.svg
   :target: https://gemnasium.com/github.com/albertyw/syspath
.. |Code Climate| image:: https://codeclimate.com/github/albertyw/syspath/badges/gpa.svg
   :target: https://codeclimate.com/github/albertyw/syspath
.. |Test Coverage| image:: https://codeclimate.com/github/albertyw/syspath/badges/coverage.svg
   :target: https://codeclimate.com/github/albertyw/syspath/coverage
