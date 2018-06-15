# -*- coding: utf-8 -*-

from setuptools import setup

from eosiopy import VERSION
import sys
from os.path import join, dirname
from setuptools import setup, find_packages

VERSION = (0, 0, 5)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open( 'README.md',"r")
long_description = f.read().strip()
f.close()
setup(
    name='eosiopy',
    version=__versionstr__,
    description='Python library of the EOS.IO project.',
    long_description=long_description,
    url='https://github.com/eosmoto/eosiopy',
    author='eosmoto',
    author_email = "eosmoto@163.com",
    license='GPL-3.0',
    packages=['eosiopy'],

    install_requires=('requests', 'base58'),
    zip_safe=False,
    keywords=['eos', 'eosio', 'eosiopy', 'eospython', 'pythoneos', 'python eos', 'eos python'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: POSIX',
        'Operating System :: MacOS'
    ],
)
