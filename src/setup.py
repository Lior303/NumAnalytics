'''
Created on Oct 30, 2018

@author: Pavel Shvarchov
'''
from setuptools import setup, find_packages

setup(
    name='PolynomHalf',
    version='0.1',
    packages=find_packages(exclude=['test']),
    license='',
    author='Shvarpa',
    author_email='Shvarpa@gmail.com',
    description='Polynomial root solver by halving method',
    install_requires=[
                        'numpy'
                      ],
)