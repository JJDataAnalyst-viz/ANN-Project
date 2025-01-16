from setuptools import setup,find_packages
from typing import List


def get_requirements(path: str)-> List[str]:
    packages = []
    with open(path,'r') as f:
        for i in f:
            if i.strip() == '-e .':
                continue
            packages.append(i.strip())
        return packages
    


setup(
    name = 'ANN_DeepLearning',
    version='0.0.1',
    description='Provide package for ANN learning',
    author = 'SciOpsEngineer',
    author_email='kubajedrych100@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)