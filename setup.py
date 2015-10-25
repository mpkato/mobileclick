# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name        = "mobileclick",
    description = "mobileclick provides baseline methods and utility scripts for the NTCIR-12 MobileClick-2 task",
    author      = "Makoto P. Kato",
    author_email = "kato@dl.kuis.kyoto-u.ac.jp",
    license     = "MIT License",
    url         = "https://github.com/mpkato/mobileclick",
    version='0.2.0',
    packages=[
        'mobileclick',
        'mobileclick.nlp',
        'mobileclick.methods',
        'mobileclick.scripts'
        ],
    install_requires = [
        'BeautifulSoup',
        'nltk>=3.1',
        'numpy'],
    entry_points = {
        'console_scripts': [
            'mobileclick_download_training_data=mobileclick.scripts.mobileclick_download_training_data:main',
            'mobileclick_download_test_data=mobileclick.scripts.mobileclick_download_test_data:main',
            'mobileclick_random_ranking_method=mobileclick.scripts.mobileclick_random_ranking_method:main',
            'mobileclick_lang_model_ranking_method=mobileclick.scripts.mobileclick_lang_model_ranking_method:main',
            'mobileclick_random_summarization_method=mobileclick.scripts.mobileclick_random_summarization_method:main',
            'mobileclick_lang_model_summarization_method=mobileclick.scripts.mobileclick_lang_model_summarization_method:main',
            'mobileclick_lang_model_two_layer_summarization_method=mobileclick.scripts.mobileclick_lang_model_two_layer_summarization_method:main',
            ],
    },
    tests_require=['nose']
)
