#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='bowtie-content',
    version='0.0.1',
    packages=['bowtie_content'],
    include_package_data=True,
    zip_safe=False,
    license='MIT License',
    description='Django-Bowtie content component',
    long_description=readme(),
    url='https://github.com/django-bowtie/bowtie-content/',
    author='Rense VanderHoek',
    author_email='rense@me.com',
    install_requires=['django', 'six'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2 :: Only'
    ],
)
