from setuptools import setup,find_packages
from typing import List 


Hyphen = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function is used to read a file 
    '''
    requirements_lst =[]
    with open(file_path) as file:
        lines = file.readlines()
        requirements_lst = [line.replace("\n","") for line in lines]

    if Hyphen in requirements_lst:
        requirements_lst.remove(Hyphen)

    return requirements_lst


setup(
    name="Heart-Disease-Prediction",
    version="0.0.1",
    author="Diksha",
    author_email="dikshaydv2006@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)