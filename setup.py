import os
from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    INSTALL_REQUIRES = f.read().splitlines()

# INSTALL_REQUIRES = [
#     'asdasd',
#     'fqwfqfq',
#     'qwfqw'
# ]

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()


setup(
    name = "pydeplist",
    version = "0.0.1",
    author = "Da Chen",
    author_email = "chendamailbox@foxmail.com",
    description = "A tool to list tree of all the python dependencies which are in GitHub.",
    url = "https://github.com/yuukidach/pydeplist",

    packages = find_packages(),
    install_requires = INSTALL_REQUIRES,
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    entry_points = {
        'console_scripts': [
            'pydeplist=pydeplist.cli.cli:run'
        ]
    },
)