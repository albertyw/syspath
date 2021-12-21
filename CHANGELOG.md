Changelog
=========

v2.0.6 (2021-12-20)
-------------------

 - Officially support python 3.10
 - CI optimizations
 - Update dependencies


v2.0.5
------

 - Test updates
 - Switch from Codeship to Drone CI
 - Update dependencies


v2.0.4
------

 - Add support for python 3.9
 - Switch CI back from CircleCI to Codeship
 - Switch README to markdown
 - Update dependencies


v2.0.3
------

 - Add "Typed" to python package classifier
 - Fix imports to prevent type errors in dependent code
 - Switch CI from Codeship to CircleCI
 - Update dependencies


v2.0.2
------

 - Fix setup.py package data path
 - Update dependencies


v2.0.1
------

 - Export type annotations so they are available to dependent code
 - Update dependencies


v2.0.0
------

 - Drop support for python 2
 - Update dependencies


v1.1.1
------

 - Update dependencies
 - Formatting


v1.1.0
------

 - Add path variable to shortcut modules
 - Update dependencies
 - Make syspath not add duplicate paths


v1.0.1
------

 - Switch from gemnasium to pyup
 - Dependency updates
 - README updates


v1.0.0
------

 - Add importing parent paths
 - Make append_path and caller_path functions private
 - Add mypy annotations
 - Update readme


v0.1.1
------

 - Add optional index to git_root functions so thtat it finds the caling function correctly
 - Fix setup.py packaging so that syspath can be imported correctly


v0.1.0
------

 - Add ability to add git root to current path
 - Restructure code so that paths can be read but not necessarily added to sys.path
 - Return added paths


v0.0.1
------

 - Iniitial release
 - Includes being able to add current importer's directory to path
 - Supports setting path based on explicit function call or from import
