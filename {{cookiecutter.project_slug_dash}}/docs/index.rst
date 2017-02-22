{{ cookiecutter.project_name }} documentation
==========================================================

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


{{ cookiecutter.project_short_description }}
	      
Contents:

.. toctree::
   :maxdepth: 2

   installation
   usage
   configuration
   workflow
   readme
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}
   authors
   {% endif -%}
   history

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
