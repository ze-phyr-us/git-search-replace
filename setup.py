#!/usr/bin/env python

from distutils.core import setup

setup(
    name='git-search-replace',
    version='1.0.0',
    author='alonid',
    author_email='alonid@gmail.com',
    packages=['gitsearchreplace', 'bin'],
    scripts=['bin/git-search-replace.py'],
    url='https://github.com/da-x/git-search-replace',
    license='LICENSE.txt',
    description='a utility on top of git for project-wide '
                'search-and-replace that includes filenames too',
    long_description=open('README.md').read(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
    ],
)
