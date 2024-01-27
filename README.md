## Project README

### MLOPS Project: Titanic

This project demonstrates the implementation of MLOps techniques for the Titanic dataset using various technologies. It involves deploying a machine learning model with PyTorch and Flask on AWS while utilizing Cassandra as the database. The primary goal is to establish a streamlined pipeline for model development and deployment.

### Technologies Used:
1. **AWS**: Deployment platform for hosting the machine learning model.
2. **PyTorch and Flask**: Frameworks used for building and serving the machine learning model.
3. **Cassandra DB**: Database management system employed for data storage and retrieval.

### Steps:

***Data Source**: `https://www.kaggle.com/competitions/spaceship-titanic/data?select=train.csv`

1. **Initialize Project Structure**:
   - Create a template and initialize the project directory structure with placeholder files. This step sets up the groundwork for the project.
   
2. **Set Up Conda Environment**:
   - Within the project terminal (VS Code), create a Conda environment:
     - `conda create -n titanicspaceship python=3.11`
   - Activate the environment:
     - `conda activate titanicspaceship` (or `source activate titanicspaceship` for Windows)
   - Execute `python template.py` to initialize the project files.
   
3. **Install Project Requirements**:
   - Install the necessary Python packages and dependencies required for the project.

4. **Configuration - setup.py**:
   - Utilize `setup.py` to configure the project description.

5. **Install Necessary Packages**:
   - Run `pip install -r requirements.txt` to install the required Python packages listed in `requirements.txt`.

These steps ensure a structured approach to project initialization and environment setup, laying the foundation for subsequent development and deployment tasks.
