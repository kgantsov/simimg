#!/usr/bin/env python
""" Setup file for Simimg package """


from distutils.core import setup

setup(
    name='simimg',
    version='0.1',
    description='Simimg package',
    long_description="Find similar images",
    author='Gantsov Konstantin',
    author_email='k.gantsov@gmail.com',
    packages=['simimg'],

    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ),
    license="GPL-2"
)
