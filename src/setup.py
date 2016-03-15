# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="pyzap",
    version="0.3",
    packages=['pyzap'],
    install_requires=['beautifulsoup4', 'logbook', 'requests', 'tqdm', 'pies', 'click', 'fuzzywuzzy',
                      'pandas', 'gevent', 'grequests', 'html5lib'],
    # google is used for translate api
    tests_require=['pytest', 'betamax', 'google-api-python-client'],
    author="OmerBA",
    description="Search Zap without a hassle",
    entry_points={
        'console_scripts': [
            'pyzap = cli:cli_main',
        ],
    },
    keywords="zap shopping",
)
