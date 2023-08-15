#!/usr/bin/env python3

import os.path

from setuptools import find_packages, setup


def _read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ""


setup(
    name="sanic-oauth",
    version="0.5.3",
    license="MIT",
    long_description=_read("README.rst"),
    keywords=["asyncio", "http", "oauth", "sanic"],
    author="Lewis Gaul",
    packages=find_packages(),
    author_email="lewis.gaul@gmail.com",
    url="https://github.com/LewisGaul/sanic-oauth",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Framework :: AsyncIO",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    install_requires=[
        "aiohttp",
        "yarl",
    ],
)
