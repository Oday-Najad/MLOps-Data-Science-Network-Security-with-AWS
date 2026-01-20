from setuptools import setup, find_packages
from typing import List


req_list: List[str] = []


def get_requirements() -> List[str]:
    """This function will return the list of requirements"""
    try:
        with open("requirements.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                req = line.strip()
                if req and req != '-e .':
                    req_list.append(req)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    return req_list


setup(
    name="network_security_project",
    version="0.1.0",
    author="Oday Najad",
    author_email="oday.najad@lau.edu",
    packages=find_packages(),
    install_requires=get_requirements(),
)
