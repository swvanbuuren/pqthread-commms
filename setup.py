#!/usr/bin/python
from setuptools import setup, find_namespace_packages

setup(
    name='pqthread-comms',
    version='0.1',
    author='Sietze van Buuren',
    author_email='s.van.buuren@gmail.com',
    packages=find_namespace_packages(include=['pqthread_comms', 'pqthread_comms.*']),
    python_requires=">=3.8",
    package_dir={"pqthread_comms": "pqthread_comms"},
    url='https://github.com/swvanbuuren/pqthread_comms',
    license='LICENSE',
    description='Pqthreads-comms facilitates communication between QThreads in python ',
    long_description=open('README.md').read(),
    install_requires=['PySide2',]
)
