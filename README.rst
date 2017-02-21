=========================================
Cookiecutter PyPackage for lts-workflows
=========================================

Cookiecutter_ template for a lts-workflows_ Python package. See
https://github.com/audreyr/cookiecutter.

* GitHub repo: https://github.com/percyfal/cookiecutter-pypackage/
* Documentation: https://cookiecutter-pypackage.readthedocs.io/
* Free software: BSD license
* Pytest_ runner: Supports `unittest`, `pytest`, `nose` style tests and more
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_

Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/percyfal/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Run `tox` to make sure all tests pass.
* Release your package the standard Python way.

  
Alternatives
------------

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `audreyr/cookiecutter-pypackage`_: The original pypackage, uses unittest
for testing and other minor changes.
  

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

  
.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _`audreyr/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _Bumpversion: https://github.com/peritus/bumpversion
.. _PyPi: https://pypi.python.org/pypi
.. _Pytest: http://pytest.org/
.. _PyPy: http://pypy.org/
.. _Wheel: http://pythonwheels.com
.. _lts-workflows: http://lts-workflows.readthedocs.io/en/latest/
