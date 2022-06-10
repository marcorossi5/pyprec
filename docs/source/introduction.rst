Getting Started
===============

Installation
------------

The ``pyprec`` package is open source and available at https://github.com/marcorossi5/pyprec.git

The package can be installed manually:

.. code-block:: bash

  git clone https://github.com/marcorossi5/pyprec.git
  cd pyprec
  pip install -e .

Motivation
----------

Creating Python packages base structure is a repetitive work that can be
automatized with the ``pyprec`` software

Creating a new project from repo
--------------------------------

``pyprec`` automates the creation of Python Packages from a fresh new GitHub
repository.

The idea is that most of the packages share a similar structure, which requires
to tweak just a few variables (e.g. `package name`, `author name` etc.).

To start creating your python package repository structure, just run ``pyprec``
command and answer the prompted questions.

Python publish workflow
-----------------------

``pyprec`` creates a GitHub workflow to publish automatically the new package on
`PyPi <https://pypi.org>`_ every time a new release is being created.

In order to activate this automatic functionality, though, the user has to store
username and passwords secrets of his PyPi account. This will ensure that the
information will be kept encrypted all along the publishing procedure.

Secrest must be stored in the package GitHub repository. For information, follow
the instruction at this
`link <https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository>`_.

How to cite pyprec?
===================

When using this software in your research, please cite the following publication:

.. image:: https://zenodo.org/badge/501281838.svg
   :alt: zenodo_badge
   :target: https://zenodo.org/badge/latestdoi/501281838

BibTex

.. code-block:: bash
  
  @software{Rossi_pyprec_2022,
    author = {Rossi, Marco},
    license = {MIT},
    month = {6},
    title = {{pyprec}},
    url = {https://github.com/marcorossi5/pyprec},
    version = {1.0.0},
    year = {2022}
  }

How to contribute?
==================

For more information on how to contribute, email the author at
`marco.rossi@cern.ch <marco.rossi@cern.ch>`_.

FAQ
===

Refer to examples in the
`GitHub <https://github.com/marcorossi5/pyprec/tree/main/examples>`_ folder for more
information.