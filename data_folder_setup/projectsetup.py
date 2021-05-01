import requests
import os
from urllib.request import urlopen
from zipfile import ZipFile


class ProjectSetup:
    def __init__(self, base_path):
        self.base_path = base_path

    def create_folder(self, name):
        if not os.path.isdir(os.path.join(self.base_path, name)):
            os.mkdir(os.path.join(self.base_path, name))
            print(f"{name} Folder Created Successfully")
        else:
            print(f"{name} Folder already exists")

    def create_folders(self, names):
        print(type(names))
        if type(names) != list:
            raise ValueError("Invalid Datatype. Use create_folder() instead.")

        for name in names:
            self.create_folder(name)

    def download_single_file(self, url, folder, filename=None):
        result = requests.get(url)
        base_folder = os.path.join(self.base_path, folder)

        if filename is None:
            file_name = url.split("/")[-1]
            filename = file_name

        with open(os.path.join(base_folder, filename), "wb") as f:
            f.write(result.content)
        print("File Creation Successful")

    def download_zip_file(self, url, folder, file_name):
        base_folder = os.path.join(self.base_path, folder)
        zipresp = urlopen(url)

        with open(os.path.join(base_folder, file_name), "wb") as f:
            f.write(zipresp.read())

        os.mkdir(os.path.join(base_folder, f"{file_name}_unzipped"))
        zf = ZipFile(os.path.join(base_folder, file_name))
        zf.extractall(os.path.join(base_folder, f"{file_name}_unzipped"))
        zf.close()

        print("File Successfully Downloaded")
