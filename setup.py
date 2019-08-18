from setuptools import setup, find_packages

setup(
    name = "pydeplist",
    version = "0.0.1",
    author = "yuukidach",
    author_email = "chendamailbox@foxmail.com",
    decription = "A tool to list tree of all the python dependencies which are in GitHub.",
    url = "https://github.com/yuukidach/pydeplist",

    packages = find_packages(),
    py_modules = ["pydeplist"],
    entry_points = {
        'console_scripts': [
            'pydeplist=pydeplist:main'
        ]
    },
)