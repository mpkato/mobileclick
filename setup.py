# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name        = "mobileclick",
    description = "mobileclick provides baseline methods and utility scripts for the NTCIR-12 MobileClick-2 task",
    author      = "Makoto P. Kato",
    author_email = "kato@dl.kuis.kyoto-u.ac.jp",
    license     = "MIT License",
    url         = "https://github.com/mpkato/mobileclick",
    version='0.0.1',
    packages=['mobileclick'],
    package_data={'chainer.requirements': ['cuda-requirements.txt']},
    tests_require=['nose'],
)
