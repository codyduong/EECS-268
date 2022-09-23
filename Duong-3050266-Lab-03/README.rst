==============
EECS 268 Lab 3
==============

Pre-reqs
========
* Python ^3.8

  * I chose this version, because IIRC it is the lab version. Or under it...
  * It might work on lower versions ¯\\_(ツ)_/¯

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

  # using script
  chmod +x scripts/main.sh
  scripts/main.sh

  # or using python3 directly
  python3 main.py
  # or if you have python aliased/sym-linked to 3.10^
  python main.py
  # or use appropriate virtual env
  # with poetry it is as follows
  poetry shell
  python3 main.py
  exit # leave virtual shell
