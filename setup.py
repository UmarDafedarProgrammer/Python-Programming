# setup.py
# run form base folder 
# pip install -e .
from setuptools import setup, find_packages

setup(
    name='UserPackages', ##Namespace/placeholder
    version='0.1',
    packages=find_packages(),
)