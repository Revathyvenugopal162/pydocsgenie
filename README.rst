PyDocsGenie
=========

PyDocsGenie is a python coding helper that automatically generates docstrings for the code you input to it. It uses the OpenAI API for this end.


How to install
--------------

Installation can be performed by running:

.. code:: bash

    cd pydocsgenie
    python -m pip install .


Run the GUI
-----------

The project includes a GUI where you can paste your code and it will generate the docstrings for it. To run the GUI,
you can run the following command after installing the project in your environment:

.. code:: bash

    pydocsgenie
    

Style and Testing
-----------------

If required, you can always call the style commands (`black`_, `isort`_,
`flake8`_...) or unit testing ones (`pytest`_) from the command line. However,
this does not guarantee that your project is being tested in an isolated
environment, which is another reason to consider using `tox`_.


Documentation
-------------

For building documentation, you can either run the usual rules provided in the
`Sphinx`_ Makefile, such us:

.. code:: bash

    python -m pip install .[doc]
    make -C doc/ html

    # subsequently open the documentation with (under Linux):
    your_browser_name doc/html/index.html

Distributing
------------

If you would like to create either source or wheel files, start by installing
the building requirements:

.. code:: bash

    python -m pip install .

Then, you can execute:

    .. code:: bash

        python -m build
        python -m twine check dist/*


.. LINKS AND REFERENCES
.. _black: https://github.com/psf/black
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _isort: https://github.com/PyCQA/isort
.. _PyAnsys Developer's guide: https://dev.docs.pyansys.com/
.. _pre-commit: https://pre-commit.com/
.. _pytest: https://docs.pytest.org/en/stable/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _pip: https://pypi.org/project/pip/
.. _tox: https://tox.wiki/
.. _venv: https://docs.python.org/3/library/venv.html
