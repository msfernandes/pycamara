# -*- coding: utf8 -*-
#
# This file were created by Python Boilerplate. Use boilerplate to start simple
# usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/python-boilerplate/
#

import os
from setuptools import setup, find_packages


# Meta information
name = 'pycamara'
project = 'pycamara'
author = 'Matheus Fernandes'
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)


# Save version and author to __meta__.py
with open(os.path.join(dirname, 'src', project, '__meta__.py'), 'w') as F:
    F.write('__version__ = %r\n__author__ = %r\n' % (version, author))

INSTALL_DEPS = [
    'requests>=2.11.1',
    'pytz>=2017.2',
    'python-dateutil>=2.6.0',
]

setup(
    # Basic info
    name=name,
    version=version,
    author=author,
    author_email='matheus.souza.fernandes@gmail.com',
    url='https://github.com/msfernandes/pycamara',
    description='Easy access to Camara dos Deputados open data API',
    long_description=open('README.md').read(),

    # Classifiers (see https://pypi.python.org/pypi?%3Aaction=list_classifiers)
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],

    # Packages and depencies
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=INSTALL_DEPS,

    # Other configurations
    zip_safe=False,
    platforms='any',
)
