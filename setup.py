#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="pySOFA",
    version="0.0.1",
    authors="Jean Ibarz",
    author_email="joerg.encke@tum.de",

    description="SOFA API",
    license="GPLv3+",
    url="https://github.com/mrkrd/thorns, https://github.com/jeanibarz/pySOFA",
    download_url="https://github.com/mrkrd/thorns/tarball/master",
    packages=find_packages(),

    platforms=["Linux", "Windows"],
    install_requires=["tables", "scipy", "numpy"],
)
