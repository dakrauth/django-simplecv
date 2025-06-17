django-simplecv
===============

A simple Django app for rendering CV's / Résumés into HTML, PDF,
MS Word docx, and plain text formats.

The management command ``simplecv`` will also (batch) convert a specified CV file.

Installation
------------

Preferably, create a new virtual environment.

Until a more robust, well-tested code base is completed, install directly from 
the GitHub repository::

    pip install -e git+https://github.com/dakrauth/django-simplecv.git#egg=simplecv

Or, download and/or fork::

    git clone https://github.com/dakrauth/django-simplecv.git
    pip install -r django-simplecv/requirements.txt


Usage
-----

Add ``simplecv`` to the your project's ``settings.INSTALLED_APPS``

License
-------

django-simplecv is available under the `MIT license`_.

.. _MIT license: LICENSE
