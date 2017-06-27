django-simplecv
===============

A simple Django app for rendering JSON-based CV's / Résumés into HTML, PDF,
MS Word docx, and plain text formats.

The simple JSON schema is exemplified in ``simplecv.utils.JSON_TEMPLATE``.

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

* Add ``simplecv`` to the your project's ``settings.INSTALLED_APPS``
* For a default CV, create a JSON file matching the simple schema on your system
* Add ``SIMPLECV_FILENAME = '<path/to/cv.json>'`` to your settings

License
-------

django-simplecv is available under the [MIT](django-simplecv/LICENSE) license.
