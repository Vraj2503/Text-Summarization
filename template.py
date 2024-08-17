import os
from pathlib import Path
import logging 

#used to log the information for debugging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s:')

project_name = 'wordSummerizer'

#Used to get the files that are required to deploy the project
list_of_files = [
    '.github/workflows/.gitkeep',    #keeps the folder that is empty, which is usually ignored by git
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yaml",
    "params.yaml",      #to store the parameters that are required for the project
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py", #used to setup local packages
    "research/trials.ipynb"
]
# To handle the paths in all operating systems
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory for the file: {filepath}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as file:
            pass
        logging.info(f'Created empty file: {filepath}')
    else:
        logging.info(f'File already exists: {filepath}')


