.. highlight:: shell

============
Installation
============


Stable release
--------------

To install {{ cookiecutter.project_slug }}, run this command in your terminal:

.. code-block:: console

    $ conda install {{ cookiecutter.project_slug_dash }}

This is the preferred method to install {{ cookiecutter.project_slug }}, as it will
always install the most recent stable release.

From sources
------------

The sources for {{ cookiecutter.project_slug }} can be downloaded from the `Bitbucket repo`_.

.. code-block:: console

    $ git clone git@bitbucket.org:{{ cookiecutter.bitbucket_organization }}/{{ cookiecutter.project_slug }}.git

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Bitbucket repo: https://bitbucket.org/scilifelab-lts/{{ cookiecutter.project_slug_dash }}

Tests
======

If :mod:`{{ cookiecutter.project_slug }}` has been installed as a module, run

.. code-block:: console

   $ pytest -v -s --pyargs {{ cookiecutter.project_slug }}

In order to load the pytest options provided by the module, the full
path to the test suite needs to be given:

.. code-block:: console

   $ pytest -v -s -rs /path/to/{{ cookiecutter.project_slug }}/tests
   
