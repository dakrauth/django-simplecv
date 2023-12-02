#!/usr/bin/env python
import os, sys
from setuptools import setup, find_packages

if os.path.exists('README.rst'):
    with open('README.rst') as f:
        long_description = f.read()
else:
    long_description = ''

simplecv = __import__('simplecv') 
VERSION = simplecv.get_version()


setup(
    name='django-simplecv',
    version=VERSION,
    url='https://github.com/dakrauth/django-simplecv',
    author='David A Krauth',
    author_email='dakrauth@gmail.com',
    description=simplecv.__doc__,
    long_description=long_description,
    platforms=['any'],
    license='MIT License',
    classifiers=(
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ),
    packages=find_packages(),
    install_requires=[
        "Django>=3.2,<5.0",
        "reportlab==4.0.7",
        "pdfdocument==4.0",
        "python-docx==1.1.0",
        "pydocx==0.9.10",
    ],
    include_package_data=True,
    package_data={
        '': ['*.rst'],
        'simplecv': ['templates/simplecv/*'],
    },
)
