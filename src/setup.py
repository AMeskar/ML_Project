# Responsable to build the ML application as a package
# I can use it in the deployemnet
from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]: # List here is undefined, using from typing import List will define it
    
    """
    This function purpose is to store the libraries names in one list 
    
    """
    
    i = "-e ." # This command will automatically trigger the setup file whenever u want to install the requirements, its inside the requiremsnts
    
    out = []  
      
    with open(file_path) as req_obj: # now we read the function
        
        requirements = req_obj.readlines() # The requiremnt.text is a list of libraries, basicall we want to create a list requ["pandas", "seaborn", "numpy", ...]
        
        #out = [req for req in requirements] # now using this we will get a list ['numpy \n', 'seaborn\n', 'pandas'], \n this will block ur installing, need to replaced by an empty space
        
        out = [req.replace("\n", "") for req in requirements] # ['numpy ', 'seaborn', 'pandas']
        
        if i in out: out.remove(i) # ['numpy ', 'seaborn', 'pandas', '-e .'], '-e .' we should remove it
        
# This is our setup file as its main purpuso to build packages/Folders as a whole

setup(
    
    name= "ML_Project", # Name of the project
    
    version= "0.0.1",
    
    description= "End to End Machine Learning Project with deployment", 
    
    author= "AMeskar",
    
    author_email= "Meskar192@gmail.com", 
    
    packages= find_packages(), # This one is to find the folders you want to build, Those folders will have a python file called __init__.py, basically the setup file recognize this file and make the folder to be build for you ML app

    install_requires = get_requirements('requirements.txt') # This is function to automotize the workflow, each project is built by libraries and we need to set a strategy to build this libraries easier

)