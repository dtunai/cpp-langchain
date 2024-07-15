import os
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cpp_langchain",
    version="0.1.0",
    author="0xdti",
    author_email="dogukanutuna@gmail.com",
    description="Packaged C/C++ executor support for Langchain.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0xdti/cpp-langchain",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
