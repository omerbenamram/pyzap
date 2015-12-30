from __future__ import absolute_import, unicode_literals, print_function, division
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="pyzap",
    version="0.1",
    packages='pyzap',
    install_requires=['beautifulsoup4', 'logbook', 'requests', 'tqdm', 'pies', 'click', 'fuzzywuzzy',
                      'pandas'],
    tests_require=['pytest', 'betamax'],
    author="OmerBA",
    description="Search Zap without a hassle",
    entry_points={
        'console_scripts': [
            'pyzap = cli:cli_main',
        ],
    },
    keywords="zap shopping",
)
