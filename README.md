## Project README

### MLOPS Project: Titanic

This project demonstrates the implementation of MLOps techniques for the Titanic dataset using various technologies. It involves deploying a machine learning model with PyTorch and Flask on AWS while utilizing Cassandra as the database. The primary goal is to establish a streamlined pipeline for model development and deployment.

### Technologies Used:
1. **AWS**: Deployment platform for hosting the machine learning model.
2. **PyTorch and Flask**: Frameworks used for building and serving the machine learning model.
3. **Cassandra DB**: Database management system employed for data storage and retrieval.

### Steps:
### I. Configurations

**Data Source**: `https://www.kaggle.com/competitions/spaceship-titanic/data?select=train.csv`

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

### II. Data Preprocessing

1. **Loading Dataset into `search >> train.ipynb`**:
   - Load the dataset into the specified Jupyter notebook for training.

2. **Create new dataset after cleaning called `data.csv`**:
   - Perform data cleaning operations and create a new dataset named `data.csv`.

3. **Load our dataset into the Database**:
   - Utilize [DataStax](https://www.datastax.com/) or similar database management system to load the dataset.

4. **Load our cleaned dataset, create and load them to the new database created at `astra.datastax.com`**:
   - Load the cleaned dataset into the new database created at `astra.datastax.com`.

5. **Generate and Download the `bundle`**:
   - Navigate to `Region` >> `Download SCB` >> Download `URL Secure bundle` to generate and download the bundle.

6. **Generate and Download `tokens`**:
   - Generate and download necessary tokens for authentication.

7. **Install the `pip install cassandra-driver` and setup the connection**:
   - Install the `cassandra-driver` using `pip install cassandra-driver` and set up the connection as per the documentation provided in the Astra documentation.

8. **Copy and Paste Downloaded Files: Token and Bundle into Our Project Files**:
   - Copy and paste the downloaded token `titanic_spaceship_db-token.json` and bundle `secure-connect-titanic-spaceship-db.zip` files into the appropriate location within our project files.

These steps facilitate the preprocessing and preparation of the dataset for further analysis and modeling.

