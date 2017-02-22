{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

{{ cookiecutter.project_name }}
========================================================================

{% if is_open_source %}
.. image:: https://anaconda.org/{{ cookiecutter.bitbucket_username }}/lts-workflows/badges/version.svg
	   :target: https://anaconda.org/percyfal/lts-workflows

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

.. image:: https://pyup.io/repos/bitbucket/{{ cookiecutter.bitbucket_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/bitbucket/{{ cookiecutter.bitbucket_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO
