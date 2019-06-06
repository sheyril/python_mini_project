import os
import shutil

# print (os.getcwd())

given_dir = input('Enter the directory path: ')

while not os.path.exists(given_dir):
    print ('Please enter a valid path ')
    given_dir = input('Enter the directory path: ')


# to set cwd to the given dir
if os.getcwd() != given_dir:
    # print(os.getcwd())
    print('changing directory to given directory')
    os.chdir(given_dir)


# to create the main folder
try:
    os.mkdir('Files')
except FileExistsError:
    print('File already exists')

# creating folders


def create_folders(folder):

    # to create the sub folders:
    os.chdir(given_dir + '/Files')
    # print(os.getcwd())

    try:
        os.mkdir(folder)
    except FileExistsError:
        print('File already exists')


ext_dict = {}

folders_dict = {'Audio': ['.mp3'], 'Documents': ['.pdf', '.txt', '.xlsx'],
                'Videos': ['.mp4', '.mkv'], 'Compressed': ['.zip'],
                'Installation': ['.pkg', 'exe', 'dmg'], 'Miscellaneous': []}

for folder, extentions in folders_dict.items():

    create_folders(folder)
    # print (folder, extentions)
    for extention in extentions:
        ext_dict[extention] = folder
# print (ext_dict)


def segregate(file, name, extention):
    # print (name)
    if extention in ext_dict:
        try:
            shutil.move(os.path.join(given_dir, file),
                        os.path.join(given_dir, 'Files/' + ext_dict[extention]))
        except FileExistsError:
            print('File already exists')


# os.chdir('/Users/sheyril/Desktop')
files_list = os.listdir(given_dir)
files_list.remove('.DS_Store')
files_list.remove('Files')
# print(files_list)

for file in files_list:
    name, extention = os.path.splitext(file)
    # print("this is the name: ", name)
    # print("this is the extention: ", extention)
    segregate(file, name, extention)
print('Done!')
