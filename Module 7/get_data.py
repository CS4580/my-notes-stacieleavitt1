"""
Download data from a URL and save it to a local file. When needed, the file will be extracted from compressed format.
"""

import pandas as pd
import numpy as np
import requests
import shutil
import os, sys
import zipfile

SERVER_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data'

def extract_zip_file(zip_path):
    """Extract a ZIP file to the current working directory.

    Args:
        zip_path (str): Zip file absolute path
    """

    print(f"Extracting {zip_path}")
    # Get the current working directory
    extract_path = os.getcwd()

    # Open the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract all the contents to the current working directory
        zip_ref.extractall(extract_path)
        print(f"File unzipped successfully and extracted to {extract_path}")
        # List the extracted file
        print(f"Extracted files: {zip_ref.namelist()}")
    # Delete the zip file
    os.remove(zip_path)

#TODO: Create a function to download the files from Kaggle directly by passing the dataset name

#def download_kaggle(set_name):
 #   """Download a Kaggle dataset and save it to a local file.

  #  Args:
   #     set_name (API command): API command from desired dataset
    #"""


def download_dataset(url, dataset_file):
    """_Download a ZIP file from a URL and save it to a local file.

    Args:
        url (url): File URL to download 
    """
    # Get the current working directory
    dest_path = os.path.join(os.getcwd(), os.path.basename(url))

    # Send a GET request to the URl
    response = requests.get(url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        #open the destination file in write-binary mode
        with open(dest_path, 'wb') as out_file:
            # Copy the response content to the destination file
            shutil.copyfileobj(response.raw, out_file)
        print(f"File downloaded successfully and saved to {dest_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

    # Check file extension. If it is a ZIP file, extract it
    if dest_path.endswith('.zip'):
        extract_zip_file(dest_path)

def load_data(file_path, index_col=None):
    if not file_path.endswith('.csv'):
        print(f'File {file_path} is not a valid CSV file')
        raise ValueError
    if not os.path.exists(file_path):
        print(f'File {file_path} does not exist')
        raise FileNotFoundError
    if index_col:
        df = pd.read_csv(file_path, index_col=index_col)
    else:
        df = pd.read_csv(file_path)

    return df


def main():
    """
    TBD: Method DocString
    """

    # If no arguments are provided, print a usage message
    # if len(sys.argv) < 2:
    #     print("Usage: python download_data.py <data_file>")
    #     sys.exit(1)

    # data01 = f'{SERVER_URL}/pandas01Data.zip'
    #Take data file as input parameter
    data_file = 'movies.csv'
    print(f"Data file: {data_file}")
    data01 = f'{SERVER_URL}/{data_file}'
    download_dataset(data01, data_file)
    data = load_data(data_file, index_col='IMDB_id')


if __name__ == '__main__':
    main()