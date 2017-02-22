.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Issues
~~~~~~~~~~~~~~

Report issues at https://bitbucket.org/{{ cookiecutter.bitbucket_organization }}/{{ cookiecutter.bitbucket_username }}/{{ cookiecutter.project_slug }}/issues.

Get Started!
------------

Ready to contribute? Here's how to set up `{{ cookiecutter.project_slug }}` for local development.

1. Fork the `{{ cookiecutter.project_slug }}` repo on Bitbucket.
2. Clone your fork locally::

    $ git clone git@bitbucket.org:your_name_here/{{ cookiecutter.project_slug }}.git

3. Install your local copy into a conda environment. Assuming you have
   conda installed, this is how you set up your fork for local
   development::

    $ conda env create -n {{ cookiecutter.project_slug }}
    $ source activate {{ cookiecutter.project_slug }}/
    $ cd {{ cookiecutter.project_slug }}/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass
   flake8 and the tests::

    $ flake8 {{ cookiecutter.project_slug }} tests
    $ python setup.py test or py.test

   To get flake8, just pip or conda install them into your conda
   environment.

6. Commit your changes and push your branch to Bitbucket::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the Bitbucket website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. If applicable, the pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.

Tips
----

To run a subset of tests::

    $ pytest tests.test_{{ cookiecutter.project_slug }}
