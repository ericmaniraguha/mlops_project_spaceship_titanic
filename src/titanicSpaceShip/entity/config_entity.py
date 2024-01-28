from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path  # Root directory where data will be stored
    local_data_file: Path  # Path to the local data file to be ingested
    cloud_config_zipfile: Path  # Path to the zipfile containing cloud configuration
    authentication_token: Path  # Path to the authentication token file
