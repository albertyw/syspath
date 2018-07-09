Changelog
=========

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
