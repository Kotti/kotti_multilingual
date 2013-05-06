# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

import os

from setuptools import find_packages
from setuptools import setup

project = 'kotti_multilingual'
version = '0.1a1'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

setup(
    name=project,
    version=version,
    description="Language Section content type for Kotti",
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Pylons",
        "Framework :: Pyramid",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: User Interfaces",
    ],
    keywords='kotti theme',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/disko/kotti_multilingual',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Babel',
        'Kotti',
    ],
    entry_points={},
    message_extractors={
        'kotti_multilingual': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
        ]
    },
)
