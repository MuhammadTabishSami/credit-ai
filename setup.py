from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

# Creating function for required packages:
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of the requirements.
    '''
    requirements=[]
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] # removes slashesh from packages being installed in requirements.txt
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='Credit Decisioning/Risk Assesment Machine Learning Project',
    version = '0.0.1',
    author='Muhammad Tabish Sami',
    author_email='muhammadtabishsami@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') #function that will fetch the required libraries from requirements.txt    

)


