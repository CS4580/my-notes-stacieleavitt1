"""Download data from our server
"""

SERVER_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'
import requests
import os

def download_file(url, file_name):
    # TODO: Download to pwd
    response = requests.get(url)

    if response.status_code == 200:
        cwd = os.getcwd()
        filepath = os.path.join(cwd, file_name)
        with open(filepath, "wb") as file:
            file.write(response.content)
        if type(file_name) == zip:
            unzip_file(file_name)

        print(f'File downloaded to: {filepath}')
    else:
        print(f'Error downloading file: {response.status_code}')

    pass

def unzip_file(file_name):
    # TODO: Unzip file
    
    pass


def main():
    """Driven Function
    """
    data01 = 'pandas01Data.zip'
    download_file(SERVER_URL, data01)
    


if __name__ == '__main__':
    main()
    