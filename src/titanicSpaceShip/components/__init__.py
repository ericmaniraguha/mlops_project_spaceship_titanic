
#Python module that handles data ingestion from a Cassandra database into a local CSV file. 
import os  # Importing the os module for working with operating system functionalities
import urllib.request as request  # Importing the request module from urllib to make HTTP requests
import zipfile  # Importing the zipfile module for working with ZIP archives
from titanicSpaceShip import logger  # Importing the logger module from the titanicSpaceShip package
from titanicSpaceShip.utils.common import get_size  # Importing the get_size function from the common module in the utils subpackage
from titanicSpaceShip.entity.config_entity import DataIngestionConfig  # Importing the DataIngestionConfig class from the config_entity module in the entity subpackage
import time  # Importing the time module for working with time-related functions
import csv  # Importing the csv module for reading and writing CSV files
from pathlib import Path  # Importing the Path class from the pathlib module for working with file paths
from cassandra.cluster import Cluster  # Importing the Cluster class from the cassandra.cluster module for connecting to a Cassandra cluster
from cassandra.auth import PlainTextAuthProvider  # Importing the PlainTextAuthProvider class from the cassandra.auth module for providing plain text authentication
import json  # Importing the json module for working with JSON data

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        delay = 5  # Define the initial delay for retrying connections
        max_retries = 1  # Define the maximum number of retry attempts
        for _ in range(max_retries):  # Loop through the retry attempts
            try:
                if not os.path.exists(self.config.local_data_file):  # Check if the local data file does not exist
                    # Define the cloud configuration with secure connect bundle information
                    cloud_config= {
                        'secure_connect_bundle': self.config.cloud_config_zipfile
                    }
                    # Read authentication credentials from the JSON token file
                    with open(self.config.authentication_token) as f:
                        secrets = json.load(f)
                    CLIENT_ID = secrets["clientId"]  # Extract the client ID
                    CLIENT_SECRET = secrets["secret"]  # Extract the client secret

                    # Create an authentication provider with the extracted credentials
                    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
                    # Create a connection to the Cassandra cluster using the cloud configuration and authentication provider
                    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
                    session = cluster.connect()

                    # Execute a query to fetch data from the Cassandra database
                    row = session.execute('SELECT * FROM "prediction"."data"')
                    if row:  # If data is fetched successfully
                        # Specify the CSV file path
                        csv_file_path = self.config.local_data_file

                        # Write fetched data to a CSV file
                        with open(csv_file_path, 'w', newline='') as csv_file:
                            writer = csv.writer(csv_file)
                            
                            # Write header
                            writer.writerow(row[0]._fields)
                            
                            # Write data
                            for each in row:
                                writer.writerow(each)
                            # Log information about successful data download
                            logger.info(f"{self.config.local_data_file} downloaded from Astra DB with following info: \n {row[0]._fields}")
                    else:
                        # Log error if unable to connect to the database
                        logger.info(f"An Error occurred while connecting to the database")
                    
                else:
                    # Log information if the file already exists
                    logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
            except Exception as e:
                # Log delay for the next attempt in case of exception
                logger.info(f"Delay for next attempt {e}")
                time.sleep(delay)  # Sleep for the delay period before the next attempt
                delay *= 2  # Double the delay for each attempt
        else:
            # Log failure to connect to the database after maximum retry attempts
            logger.info(f"Failed connecting to Astra/Cassandra DB after {max_retries} attempt")

def decodeData(data) -> dict:
    decodedFeatures = {}  # Initialize an empty dictionary to store decoded features
    for key, val in data.items():  # Iterate through each key-value pair in the input data dictionary
        if key in ['Age','RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']:  # Check if the key corresponds to numerical features
            val = [float(val[0])]  # Convert the value to float and wrap it in a list
        elif key in ["CryoSleep", "VIP"]:  # Check if the key corresponds to categorical features
            val = [val[0]]  # Wrap the value in a list
        decodedFeatures[key] = val  # Add the decoded feature to the dictionary
    logger.info("Data was decoded")  # Log information about the decoding process
    return decodedFeatures  # Return the decoded features as a dictionary
