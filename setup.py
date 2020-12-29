#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

PKG_NAME = "ebiritch"


# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
#
# release markers:
#   X.Y
#   X.Y.Z   # For bugfix releases
#
# pre-release markers:
#   X.YaN   # Alpha release
#   X.YbN   # Beta release
#   X.YrcN  # Release Candidate
#   X.Y     # Final release

VERSION = "0.1a0"


setup(name=PKG_NAME,
      version=VERSION,
      description="Yet Another Implementation of The Bridge Card Game",
      url="http://github.com/itnok/ebiritch",
      author="Simone Conti @itnok",
      author_email="s.conti@itnok.com",
      license="MIT",
      packages=[PKG_NAME],
      zip_safe=False)
