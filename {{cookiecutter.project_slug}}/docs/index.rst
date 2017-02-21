Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================

.. image:: https://readthedocs.org/projects/{{ cookecutter.project_slug }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Contents:

.. toctree::
   :maxdepth: 2

   installation
   usage
   configuration
   workflow
   readme
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors{% endif -%}
   history

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
