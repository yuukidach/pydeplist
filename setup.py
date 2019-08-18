import os
from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    INSTALL_REQUIRES = f.read().splitlines()

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()


setup(
    name = "pydeplist",
    version = "0.0.1",
    author = "yuukidach",
    author_email = "chendamailbox@foxmail.com",
    description = "A tool to list tree of all the python dependencies which are in GitHub.",
    url = "https://github.com/yuukidach/pydeplist",

    packages = find_packages(),
    install_requires = INSTALL_REQUIRES,
    long_description = LONG_DESCRIPTION,
    entry_points = {
        'console_scripts': [
            'pydeplist=pydeplist.cli.cli:run'
        ]
    },
)