import os

from setuptools import setup, find_packages


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, 'r') as f:
        return f.read()


setup(
    name="stere",
    version="0.1.0",
    description="A nice way of implementing the Page Object pattern.",
    long_description=read('README.rst'),
    author="Joshua Fehler",
    author_email="jsfehler@gmail.com",
    license="MIT",
    url="https://github.com/jsfehler/stere",
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ),
)
