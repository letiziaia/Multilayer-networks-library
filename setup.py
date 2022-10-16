#! /usr/bin/env python
# vim: set fileencoding=utf-8

from setuptools import setup


setup(
    name="pymnet",
    version="0.1",
    description="Library for analysing multilayer networks",
    url="https://bitbucket.org/bolozna/multilayer-networks-library",
    author="Mikko Kivelä",
    author_email="mikko.kivela@iki.fi",
    install_requires=[
        "numpy",
        "scipy",
        "pybind11",
        "Cython",
        "networkx",
        "matplotlib<=3.3.0",
    ],
    packages=[
        "pymnet",
        "pymnet.tests",
        "pymnet.visuals",
        "pymnet.visuals.drawbackends",
        "pymnet.isomorphisms",
        "pymnet.graphlets",
    ],
)
