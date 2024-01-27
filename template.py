import os  # Importing the os module for operating system functionalities
from pathlib import Path  # Importing Path class from pathlib module for working with file paths
import logging  # Importing logging module for logging messages

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')  # Configuring logging format

project_name = "titanicSpaceShip"  # Defining the project name

# List of files to be created or checked
list_of_files = [
    ".github/workflows/.gitkeep",  # -- this is for github workflow setup ci/cid
    f"src/{project_name}/__init__.py",  # Initializing the project's source code package
    f"src/{project_name}/components/__init__.py",  # Initializing components package
    f"src/{project_name}/utils/__init__.py",  # Initializing utilities package
    f"src/{project_name}/config/__init__.py",  # Initializing configuration package
    f"src/{project_name}/config/configuration.py",  # Configuration file for the project
    f"src/{project_name}/pipeline/__init__.py", # Pipeline of data ingestion and best model.
    f"src/{project_name}/entity/__init__.py",  # Initializing entity package
    f"src/{project_name}/constants/__init__.py",  # Initializing constants package
    "config/config.yaml",  # Configuration YAML file
    "dvc.yaml",  # DVC (Data Version Control) configuration file
    "params.yaml",  # Parameters YAML file
    "requirements.txt",  # Python dependencies requirements file
    "setup.py",  # Setup script for packaging the project
    "research/trails.ipynb",  # Jupyter notebook for research trails
    "templates/index.html",  # HTML template file
    "torchserve/models/.keep",  # Placeholder file for models directory
    "torchserve/utils/.keep",  # Placeholder file for utilities directory
    "torchserve/model-store/.keep"  # Placeholder file for model store directory
]

# Iterating over each file in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Converting the file path to a Path object
    filedir, filename = os.path.split(filepath)  # Splitting the file path into directory and filename

    # Create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Creating directory if it doesn't exist
        logging.info(f"Creating directory: {filedir} for file: {filename}")  # Logging directory creation
    
    # Create empty file if it doesn't exist or if it's empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Creating empty file
        logging.info(f"Creating empty file: {filepath}")  # Logging file creation
    
    else:
        logging.info(f"{filename} is already existing")  # Log message indicating file existence
