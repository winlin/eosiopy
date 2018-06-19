from setuptools import setup

from eosiopy import VERSION

setup(
    name='eosiopy',
    version=VERSION,
    description='Python library of the EOS.IO project.',
    long_description='Python library of the EOS.IO project..',
    url='https://github.com/eosmoto/eosiopy',
    author='eosmoto',
    license='GPL-3.0',
    packages=['eosiopy'],
    include_package_data=True,
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
