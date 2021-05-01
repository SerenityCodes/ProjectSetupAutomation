import argparse
from data_folder_setup.projectsetup import ProjectSetup

print("Welcome! Time to download files and create folders")

parser = argparse.ArgumentParser()

parser.add_argument("-b", "--base_folder", help="Base Direcctory where folders will be created", type=str)
parser.add_argument("-u", "--url", help="Write URL", type=str)
args = parser.parse_args()

if args.base_folder:
    names = ["Datasets", "Models", "Figures"]
    base_folder = args.base_folder.replace(" ", "")

    setup = ProjectSetup(base_path=base_folder)
    setup.create_folders(names)

    if args.url:
        url = args.url.replace(" ", "")
        setup.download_single_file(url=url, folder=names[0])
else:
    print("Try again with a base folder")