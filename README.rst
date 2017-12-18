SysPath
=======

Development
-----------

.. code:: bash

    pip install -r requirements-test.txt
    coverage run setup.py test
    coverage report
    flake8

Publishing
----------

.. code:: bash

    pip install twine
    python setup.py sdist bdist_wheel
    twine upload dist/*
