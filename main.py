import argparse
import os
from data_folder_setup.projectsetup import ProjectSetup

print("Welcome! Time to download files and create folders")

parser = argparse.ArgumentParser()

parser.add_argument("-b", "--base_folder", help="Base Directory where folders will be created", type=str)
parser.add_argument("-u", "--url", help="Write URL", type=str)
parser.add_argument("-t", "--type", help="Type of File (Zip or File)", type=str)
args = parser.parse_args()

if args.base_folder:
    names = ["Datasets", "Models", "Figures"]
    base_folder = args.base_folder.replace(" ", "")

    setup = ProjectSetup(base_path=base_folder)
    setup.create_folders(names)

    if args.url:
        url = args.url.replace(" ", "")
        if args.type:
            if args.type is "Zip":
                setup.download_zip_file(url, names[0], "zipfile")
            elif args.type is "File":
                setup.download_single_file(url=url, folder=names[0])
        else:
            print("You did not include a file type ('Zip' or 'File')")
else:
    print("Try again with a base folder")
