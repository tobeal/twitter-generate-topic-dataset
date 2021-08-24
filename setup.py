#!/usr/bin/python3
# Copyright 2021 AIR INSTITUTE
# See LICENSE for details.

import io

from setuptools import setup, find_packages


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()

def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs


setup(
    name='twitter-generate-topic-dataset',
    version='1.0',
    packages=find_packages(),
    license='LICENSE.md',
    author='AIR INSTITUTE',
    author_email='albertomonfdez@usal.es',
    description='',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=requirements(filename='requirements.txt'),
    data_files=[],
    entry_points={
        'console_scripts': [
            'twitter-generate-topic-dataset=twitter_dataset.run:main'
        ],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers"
    ],
    python_requires='>=3',
    extras_require={
        "tests": requirements(filename='requirements.txt'),
        "docs": requirements(filename='requirements.txt')
    },
   
)