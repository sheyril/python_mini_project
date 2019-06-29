import os
import shutil
from pathlib import Path, PurePosixPath
import argparse

parser = argparse.ArgumentParser(
                    description='Moves files from a specified directory into folders organised by type')
parser.add_argument('-v', '--verbose',
                    help='increase output verbosity', action="store_true")
parser.add_argument('-d', '--dirrectory',
                    help='Input target directory, default: current working directory',
                    default=Path.cwd())
parser.add_argument('-f', '--filename',
                    help='Input main file name, default: File ',
                    default='File')
args = parser.parse_args()
if args.verbose:
    print('verbosity turned on')

given_dir = args.directory

if not Path(given_dir).is_dir():
    print("Invalid directory")
    quit()
# to set cwd to the given dir
if Path.cwd() != given_dir:
    if args.verbose:
        print('changing directory to given directory')
    os.chdir(Path(given_dir))


# to create the main folder
Path(args.filename).mkdir(parents=True, exist_ok=True)


# to create the sub folders:
def create_folders(folder):
    os.chdir(given_dir + '/' + args.filename)
    Path(folder).mkdir(parents=True, exist_ok=True)


ext_dict = {}
folders_dict = {'Audio': ['.mp3'], 'Documents': ['.pdf', '.txt', '.xlsx'],
                'Videos': ['.mp4', '.mkv'], 'Compressed': ['.zip'],
                'Installation': ['.pkg', '.exe', '.dmg'], 'Miscellaneous': ['other']}

for folder, extentions in folders_dict.items():
    create_folders(folder)
    for extention in extentions:
        ext_dict[extention] = folder


def segregate(file, extention):
    inp_file = Path.cwd().joinpath(file)
    if args.verbose:
        print("inp file: ", inp_file)

    if extention in ext_dict:
        try:
            out_file = Path.cwd().joinpath(ext_dict[extention])
            shutil.move(str(inp_file), str(out_file))
            if args.verbose:
                print("moved")
        except FileExistsError:
            print('File already exists')
    else:
        try:
            print(Path.cwd())
            out_file = Path.cwd().joinpath(ext_dict['other'])
            shutil.move(str(inp_file), str(out_file))
            if args.verbose:
                print("moved")
        except FileExistsError:
            print('File already exists')


def get_files(directory):
    for file in Path(directory).iterdir():
        print(file)
        if file.is_file():
            segregate(file, PurePosixPath(file).suffix)


get_files(given_dir)

if args.verbose:
    print('Done!')


