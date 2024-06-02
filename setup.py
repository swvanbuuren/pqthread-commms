""" Package setup for pqthread-comms """

from setuptools import setup, find_namespace_packages

with open('requirements.txt', mode='r', encoding='utf-8') as file:
    REQUIREMENTS = file.readlines()

with open('README.md', mode='r', encoding='utf-8') as file:
    README = file.read()

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
    description='Expose class interfaces from the main GUI Thread in another QThread in Qt for Python',
    long_description=README,
    install_requires=REQUIREMENTS,
)
