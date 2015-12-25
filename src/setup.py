from setuptools import setup, find_packages

setup(
    name="pyzap",
    version="0.1",
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'logbook'],
    tests_require=['pytest'],
    author="OmerBA",
    description="Search Zap without a hassle",
    keywords="zap shopping",
)
