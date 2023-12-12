"""
Copyright (C) 2019  Patrick Schwab, ETH Zurich

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions
 of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
from distutils.core import setup
from setuptools import find_packages

setup(
    name='cxplain',
    version='1.0.3',
    packages=find_packages(),
    url='http://schwabpatrick.com',
    author='Patrick Schwab',
    author_email='patrick.schwab@hest.ethz.ch',
    license="MIT License",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "six >= 1.16.0",
        "scikit-learn >= 1.3.0",
        "numpy >= 1.25.2",
        "scipy"
    ],
    tests_require=[
        "nose"
    ],
    extra_packages={
        "matplotlib": ["matplotlib"],
        "tensorflow": ["tensorflow>=2.15.0"],
        "tensorflow_gpu": ["tensorflow-gpu>=2.12.0"]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
