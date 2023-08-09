from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    
    requirement_list:List[str] = []
    # Read the requirements.txt file
    with open('requirements.txt', 'r') as file:
        for line in file:
            requirement_list.append(line.strip())

setup(
    name="sensor",
    version="0.0.1",
    author="Om Singh",
    author_email="omsingh072001@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)

