==============
EECS 268 Lab 4
==============
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

Pre-reqs
========
* Python ^3.9

  * I chose this version, because it is the minimum for functools.cache

* I use `poetry`_ as the package manager, all deps are for development only

  * `black`_ for formatting
  * `docutils`_ and `esbonio`_ for reStructuredText files
  * `coverage`_ for testing

.. _poetry: https://github.com/python-poetry/poetry
.. _black: https://github.com/psf/black
.. _docutils: https://docutils.sourceforge.io/
.. _esbonio: https://github.com/swyddfa/esbonio
.. _coverage: https://github.com/nedbat/coveragepy

Run from source
===============
..  code-block:: shell

  # testing
  chmod +x scripts/test.sh
  scripts/test.sh

  # or using python3 directly
  python3 exercise#/exercise#.py
  # or if you have python aliased/sym-linked to 3.8^
  python exercise#/exercise#.py
  # or use appropriate virtual env
  # with poetry it is as follows
  poetry install
  poetry shell
  python3 exercise#/exercise#.py
  exit # leave virtual shell
