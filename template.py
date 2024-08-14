import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s:')
# this is an information level log that logs the error message with time stamp

project_name = 'mlproject'

list_of_files = [
    ".github/workflows/.gitkeep", # this is a dummy file to keep the directory structure
    f"src/{project_name}/__init__.py", # this is aconstructor file to create a local package
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    filepath = Path(filepath) #converts forward slashes in the list to the windows path
    filedir, filename = os.path.split(filepath) #splits the path into directory and file name

    if filedir != "": #if the directory is not empty
        os.makedirs(filedir,exist_ok=True) #creates the directory if it does not exist
        logging.info(f"Created {filedir} directory for the {filename} file") 
        #logs the directory creation

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): 
        #if the file does not exist or is empty
        with open(filepath, "w") as f: #open the file in write mode
            pass #pass the file
            logging.info(f"Created file: {filename} at {filepath}") #log the file creation

    else: #if the file already exists
        logging.info(f"{filename} already exists at {filepath}") #log the file already exists

