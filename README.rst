⚠️ This repository is still underconstruction DO NOT USE ⚠️

Pypackage
=========

.. image:: https://img.shields.io/github/v/release/12rambau/pypackage?logo=github&logoColor=white
   :alt: GitHub release (with filter)
   :target: https://github.com/12rambau/pypackage/releases

.. image:: https://img.shields.io/github/actions/workflow/status/12rambau/pypackage/unit.yaml?logo=github&logoColor=white
   :alt: GitHub Workflow Status (with event)
   :target: https://github.com/12rambau/pypackage/actions/workflows/unit.yaml

.. image:: https://img.shields.io/readthedocs/12rambau-pypackage?logo=readthedocs&logoColor=white
   :alt: Read the Docs
   :target: https://12rambau-pypackage.readthedocs.io/en/latest/


The skeleton of a ``Sphinx`` extention ready to be shipped in the ``sphinxcontrib`` organisation. It contains:

- ``pre-commit`` hooks (`prettier <https://prettier.io/>`__, `ruff <https://beta.ruff.rs/docs/>`__, `black <https://black.readthedocs.io>`__)
- ``nox`` sessions (doc, `pytest <https://docs.pytest.org>`__, `mypy <https://mypy.readthedocs.io>`__)
- A test structure carefully designed for ``Sphinx`` extentions based on the ``sphinx`` pytest fixture and `pytest-regressions <https://pytest-regressions.readthedocs.io/en/latest/>`__
- a documentation structure based on `Sphinx <https://www.sphinx-doc.org>`__ using the `pydata-sphinx-theme <https://pydata-sphinx-theme.readthedocs.io>`__
- a complete github folder (README, LICENSE, etc...)
- github actions (test, coverage, mypy, lint, release)
- ready to publish on `pipy <https://pypi.org/>`__
- ready to document on `readthedocs <https://readthedocs.org/>`__
- ready to report on `codecov <https://app.codecov.io>`__
- easy contribution using GitHub codespaces.

Demonstration
-------------

The package end result is demonstrated in the `sphinxcontrib-skeleton <https://github.com/sphinx-contrib/sphinxcontrib-skeleton>`__ repository.

Usage
-----

#.  Define an extension name. It can be anything with any normal character (`w+ <regexr.com/7aj95>`__) like "Extension Skeleton".

#.  Init an empty github repository with the slug name of your extention. A slug should only use lower case characters and replace all spaces with ``-`` like "extention-skeleton". To match the name of the package, the repository should be prefixed with "sphinxcontrib-" like "sphinxcontrib-extention-skeleton".

#.  Enable the repository on codecov and add a ``CODECOV_TOKEN`` github action env variable. With the generated token from codecov.

#.  Start a new readthedocs project hooked to the repository. in the admin tick the "build on PR" option.

#.  In your local computer start the project by running the following code. Set the same names as in the github repository.

    .. note::
        You will need to install 2 extra python libs if it's not already done, ``copier`` and ``jinja2-time``.

        .. code-block:: console

            pip install copier jinja2-time

    .. code-block:: console

        copier copy --trust gh:sphinx-contrib/copier-sphinxcontrib sphinxcontrib-<extention-skeleton>

#.  Go to the folder and init the git project:

    .. code-block:: console

        cd sphinxcontrib-<extention-skeleton>
        git init

#.  Run ``nox`` tests to see if everything is working. This command will run the 4 nox sessions (lint, tests, mypy, docs)

    .. code-block:: console

        nox

#.  Install pre-commits:

    .. code-block:: console

        pre-commit install

#.  Push to distant repository following Github instructions

    .. code-block:: console

        git add .
        git commit -m "build: initial commit"
        git remote add origin git@github.com:<username>/sphinxcontrib-<extention-skeleton>.git
        git branch -M main
        git push -u origin main

#.  Once you are ready to make a release (or a pre-release to lock the name), Create a new project on pipy by running the first push yourself using version number ``0.0.0``:

    .. code-block:: console

        python -m build
        twine upload dist/**

#.  Modify the lib as you see fit

#.  Update version with commitizen tools:

    .. code-block:: console

        cz bump

#.  Add a token to a new github action env variable ``PYPI_PASSWORD`` from your pypi profile. limit the scope to this repository only.

#.  Start a new release in github and let actions do the rest

#. The generated package will automatically detect new releases of the template and create update PR. follow the instructions in the issue to update your project.
