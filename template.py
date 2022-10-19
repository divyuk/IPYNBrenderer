from asyncio.log import logger
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s: %(levelname)s]: %(message)s")

while True:
    project_name = input("Enter the Project name: ")
    if project_name !='':
        break
logging.info(f"Creating project by name: {project_name}")
# List of files :
list_of_files=[
    ".github/workflows/.gitkeep", # For github actions
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh", # for basic env setup
    "requirements.txt",
    "requirements_dev.txt", # for testing 
    "setup.py",
    "pyproject.toml",
    "setup.cfg", 
    "tox.ini" # to test in multiple env
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
        
    # when you rerun the code it erases all the previous files
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
            
    else:
        logging.info(f"File is already present at : {filepath}")
            
            
            