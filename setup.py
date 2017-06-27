#!/usr/bin/env python
import os, sys
from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit(0)

if os.path.exists('README.rst'):
    with open('README.rst') as f:
        long_description = f.read()
else:
    long_description = ''

simplecv = __import__('simplecv') 
VERSION = simplecv.get_version()

with open('requirements.txt') as fp:
    install_requires = fp.read()

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
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ),
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.rst'],
        'simplecv': ['templates/simplecv/*'],
    },
    install_requires=install_requires
)
