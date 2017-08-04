#!/usr/bin/env python

import sys
from setuptools import setup

install_requires = [
]

setup(name="deepmoon",
      version="0.3.7",
      author="Paul Fitzpatrick",
      author_email="paulfitz@alum.mit.edu",
      description="The deep learning framework from beyond the moon",
      packages=['deepmoon'],
      entry_points={
          "console_scripts": [
              "deepmoon=deepmoon.main:main"
          ]
      },
      install_requires=install_requires,
      extras_require={
      },
      tests_require=[
      ],
      test_suite="nose.collector",
      url="https://github.com/paulfitz/deepmoon"
)
