#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import versioneer
from os.path import realpath, dirname, relpath, join
from setuptools import setup

ROOT = dirname(realpath(__file__))

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pyyaml>=3.11',
    'lts-workflows',
    # TODO: put package requirements here
]

test_requirements = [
    'snakemake>=3.10',
    # TODO: put package test requirements here
]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}


package_data = []

def package_path(path, filters=()):
    if not os.path.exists(path):
        raise RuntimeError("packaging non-existent path: %s" % path)
    elif os.path.isfile(path):
        package_data.append(relpath(path, '{{ cookiecutter.project_slug }}'))
    else:
        for path, dirs, files in os.walk(path):
            path = relpath(path, 'lts_workflows_sm_scrnaseq')
            for f in files:
                if not filters or f.endswith(filters):
                    package_data.append(join(path, f))

suffixes = ('.rule', '.settings', '.sm', '.yaml', 'Snakefile', '.csv')
package_path(join(ROOT, "{{ cookiecutter.project_slug }}"), suffixes)

setup(
    name='{{ cookiecutter.project_slug }}',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + history,
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=[
        '{{ cookiecutter.project_slug }}',
    ],
    package_dir={'{{ cookiecutter.project_slug }}':
                 '{{ cookiecutter.project_slug }}'},
    package_data={'{{ cookiecutter.project_slug }}': package_data},
    include_package_data=True,
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
