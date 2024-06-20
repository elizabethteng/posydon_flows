#!/usr/bin/env python

from setuptools import setup

setup(
    name='posydon_flows',
    version='0.0',
    author = 'Philipp Moura Srivastava, Elizabeth Teng',
    packages = ['posydon_flows'],
    install_requires=["numpy",
                      "scipy",
                      "scikit_learn",
                      "posydon"],
    extras_require=dict(
        test=["scipy", "nbconvert", "nbstrip", "ipykernel"]
    ),
)