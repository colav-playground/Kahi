#!/usr/bin/env python3
# coding: utf-8

# Copyright (c) Colav.
# Distributed under the terms of the Modified BSD License.

from setuptools import setup, find_packages

import os
import sys
import codecs


v = sys.version_info


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


shell = False
if os.name in ('nt', 'dos'):
    shell = True
    warning = "WARNING: Windows is not officially supported"
    print(warning, file=sys.stderr)


def main():
    setup(
        # Application name:
        name="Kahi",

        # Version number (initial):
        version=get_version('kahi/_version.py'),

        # Application author details:
        author="Gerardo",
        author_email="gerardo.gutierrez@udea.edu.co",

        # Packages
        packages=find_packages(exclude=['tests']),

        # Include additional files into the package
        include_package_data=True,

        # Details
        url="https://github.com/colav-playground/scienti",
        #scripts=['bin/hunabku_server', 'bin/hunabku_loader'],
        #
        license="BSD",

        description="ETL for bibliographic data",

        long_description=open("README.md").read(),

        long_description_content_type="text/markdown",

        # Dependent packages (distributions)
        install_requires=[
        'pymongo',
	    'iso3166==1.0.1',
	    'iso-639==0.4.5',
	    'langdetect',
	    'currencyconverter',
	    'joblib',
        ],
    )


if __name__ == "__main__":
    main()
