''' 
Description of setup.py

The setup.py file configures the distribution of Python packages, specifying metadata, dependencies, and included files.
It facilitates installation with tools like pip and defines executable scripts. Essential for creating easily distributable and installable packages.

'''
# Importing functions for setup configuration
from setuptools import setup, find_packages
from typing import List

# Function creation and adjustment for getting the requirements
HYPEN_E_DOT = '-e .' 

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


# Setup configuration
setup(
    name = 'LifeExpectancy',
    version = '0.0.1',
    author = 'Victor L. Castro',
    author_email = 'victorlcastro.dsa@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    
    
)