==============
EECS 268 Lab 5
==============

Pre-reqs
========
* Python ^3.10

* I use `poetry`_ as the package manager, all deps are for development only

  * `black`_ for formatting
  * `docutils`_ and `esbonio`_ for reStructuredText files
  * `coverage`_ for testing
  * `pyright`_ for static type checking

.. _poetry: https://github.com/python-poetry/poetry
.. _black: https://github.com/psf/black
.. _docutils: https://docutils.sourceforge.io/
.. _esbonio: https://github.com/swyddfa/esbonio
.. _coverage: https://github.com/nedbat/coveragepy
.. _pyright: https://github.com/microsoft/pyright

Run from source
===============
..  code-block:: shell

  # or using python3 directly
  python3 main.py
  # or if you have python aliased/sym-linked to 3.10^
  python main.py
  # or use appropriate virtual env
  # with poetry it is as follows
  poetry install
  poetry shell
  python main.py
  exit # leave virtual shell

Testing
=======
..  code-block:: shell

  chmod +x scripts/test.sh
  scripts/test.sh

Format w/ Black
===============
..  code-block:: shell

  chmod +x scripts/format.sh
  scripts/format.sh

Development
===========
..  code-block:: shell
  
  chmod +x scripts/dev.sh
  scripts/dev.sh