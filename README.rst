SysPath
=======

|Codeship Status for albertyw/syspath| |Dependency Status| |Code Climate| |Test Coverage|

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

.. |Codeship Status for albertyw/syspath| image:: https://app.codeship.com/projects/8d31dab0-c698-0135-edff-328cb0679be8/status?branch=master
   :target: https://codeship.com/projects/261214
.. |Dependency Status| image:: https://gemnasium.com/badges/github.com/albertyw/syspath.svg
   :target: https://gemnasium.com/github.com/albertyw/syspath
.. |Code Climate| image:: https://codeclimate.com/github/albertyw/syspath/badges/gpa.svg
   :target: https://codeclimate.com/github/albertyw/syspath
.. |Test Coverage| image:: https://codeclimate.com/github/albertyw/syspath/badges/coverage.svg
   :target: https://codeclimate.com/github/albertyw/syspath/coverage
