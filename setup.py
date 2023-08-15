from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function is going to return a list of required packages
    '''
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            print(HYPHEN_E_DOT)
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements   
    
setup (
    name="mlproject",
    version='0.0.1',
    author="Hilton",
    author_email='hma68@hotmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    #install_requires=['pandas','numpy','seaborn','matplotlib','scikit-learn','xgboost','Flask']
)