#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import knowledgebase

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = knowledgebase.__version__

if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

install_requires = []

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='django-knowledgebase',
    version=version,
    description="""A knowledgebase made with Django""",
    long_description=readme + '\n\n' + history,
    author='Julio Marquez',
    author_email='j@bazzite.com',
    url='https://github.com/bazzite/django-knowledgebase',
    packages=[
        'knowledgebase',
    ],
    include_package_data=True,
    install_requires=install_requires,
    license="Apache License 2.0",
    zip_safe=False,
    keywords='django-knowledgebase',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
