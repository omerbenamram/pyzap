from __future__ import absolute_import, unicode_literals, print_function, division
from setuptools import setup, find_packages

setup(
    name="pyzap",
    version="0.1",
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'logbook', 'requests', 'tqdm', 'pies'],
    tests_require=['pytest'],
    author="OmerBA",
    description="Search Zap without a hassle",
    keywords="zap shopping",
)
