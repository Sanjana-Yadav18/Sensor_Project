from setuptools import find_packages,setup
from typing import List

def get_reqiurements(file_path: str) -> list[str]:
    requirements = []
    with open (file_path) as file_obj:
        requirements  =file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        return requirements 

setup(
    name='Fault Detection',
    version= '0.0.1',
    author = 'Sanjana',
    author_email= 'sanjanaydv3@gmail.com',
    install_requirements = get_reqiurements('requirements.txt'),
    packages= find_packages()
)