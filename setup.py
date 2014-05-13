#!/usr/bin/env python
from setuptools import setup

NAME = 'magpie'
DESCRIPTION = 'magpie: [ma]rkdown, [g]it, [pie]thon'
VERSION = open('VERSION').read().strip()
LONG_DESC = open('README.rst').read()
LICENSE = open('LICENSE').read()

setup(
    name=NAME,
    version=VERSION,
    author='Charles Thomas',
    author_email='ch@rlesthom.as',
    packages=['web'],
    url='https://github.com/charlesthomas/%s' % NAME,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESC,
    scripts=['bin/pdf_scraper.py',
             'bin/email_notes.py'],
    entry_points='''
    [console_scripts]
    magpie = magpie.web.server:main
    ''',
    classifiers=[]
)
