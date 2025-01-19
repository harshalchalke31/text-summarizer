import os
from pathlib import Path
import logging

# creating logging string
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name='textSummarizer'

list_of_files=[
    ".github/workflows/.gitkeep",      # for CI/CD deployment
    # files for the local package creation
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

# create the list of files
if __name__=="__main__":
    for filepath in list_of_files:
        filepath = Path(filepath)  # convert the filepath in supported OS format
        filedir,filename = filepath.parent, filepath.name

        if filedir!="":
            filedir.mkdir(parents=True,exist_ok=True)
            logging.info(f'Creating Directory: {filedir} for {filename}.')
        
        if (not filepath.exists()) or (os.path.getsize(filepath)==0):
            filepath.touch()
            logging.info(f"Creating empty file: {filepath}.")
        
        else:
            logging.info(f'{filepath} already exists.')

