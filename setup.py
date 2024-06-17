''' 
Short description of setup.py:
-The setup.py file configures the distribution of Python packages, specifying metadata, dependencies, and included files.
-It facilitates installation with tools like pip and defines executable scripts. Essential for creating easily distributable and installable packages.


Short description of libraries used:
-Python setuptools library provides utilities for packaging, distributing, and installing Python projects, simplifying the management of dependencies and project setup.
-Python typing library provides support for type hints, allowing developers to statically declare types for variables, function parameters, and return values, enhancing code readability and maintainability.

'''
from setuptools import setup, find_packages

# Command to install packages
# pip3 install -e .
requirements = [
    "pandas==2.2.2",
    "scikit-learn==1.5.0"
]

# Setup configuration
setup(
    name='LifeExpectancy',
    version='0.0.1',
    author='Victor L. Castro',
    author_email='victorlcastro.dsa@gmail.com',
    packages=find_packages(),
    install_requires = requirements,
    python_requires='>=3.11',
)
