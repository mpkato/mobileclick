# -*- coding:utf-8 -*-
from setuptools import setup

with open('README.md') as description_file:
    long_description = description_file.read()

setup(
    name        = "mobileclick",
    description = "mobileclick provides baseline methods and utility scripts for the NTCIR-12 MobileClick-2 task",
    long_description=long_description,
    author      = "Makoto P. Kato",
    author_email = "kato@dl.kuis.kyoto-u.ac.jp",
    license     = "MIT License",
    url         = "https://github.com/mpkato/mobileclick",
    version='0.1.1',
    packages=[
        'mobileclick',
        'mobileclick.nlp',
        'mobileclick.methods',
        'mobileclick.scripts'
        ],
    install_requires = ['BeautifulSoup', 'nltk', 'numpy'],
    entry_points = {
        'console_scripts': [
            'mobileclick_download_data=mobileclick.scripts.mobileclick_download_data:main',
            'mobileclick_random_ranking_method=mobileclick.scripts.mobileclick_random_ranking_method:main',
            'mobileclick_lang_model_ranking_method=mobileclick.scripts.mobileclick_lang_model_ranking_method:main'
            ],
    },
    tests_require=['nose']
)
