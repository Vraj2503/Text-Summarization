import os
import zipfile
import urllib.request as request
from wordSummerizer.logging import logger
from wordSummerizer.utils.common import get_size
from pathlib import Path
from wordSummerizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                self.config.source_url, 
                self.config.local_data_file)
            
            logger.info(f"{filename} download! with following info: {headers}")
        else:
            logger.info(f"The file already exists at {get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)