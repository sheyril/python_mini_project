import os
import shutil

# print (os.getcwd())
given_dir = input('Enter the directory path: ')

# to set cwd to the given dir
if os.getcwd() != given_dir:
    # print(os.getcwd())
    print('changing directory to given directory')
    os.chdir(given_dir)

'''# to set cwd to the desktop
if os.getcwd() != '/Users/sheyril/Desktop':
    # print(os.getcwd())
    print('changing directory to desktop')
    os.chdir('/Users/sheyril/Desktop')
'''


# creating folders

def create_folders():

    # to create the main folder
    try:
        os.mkdir('Files')
    except FileExistsError:
        print('File already exists')

    # to create the sub folders:
    os.chdir(given_dir + '/Files')
    # print(os.getcwd())

    try:
        os.mkdir('Audio')
    except FileExistsError:
        print('File already exists')
    try:
        os.mkdir('Pictures')
    except FileExistsError:
        print('File already exists')
    try:
        os.mkdir('Videos')
    except FileExistsError:
        print('File already exists')
    try:
        os.mkdir('Documents')
    except FileExistsError:
        print('File already exists')
    try:
        os.mkdir('Compressed')
    except FileExistsError:
        print('File already exists')
    try:
        os.mkdir('Miscellaneous')
    except FileExistsError:
        print('File already exists')
    try:
        os.mkdir('Installation')
    except FileExistsError:
        print('File already exists')


create_folders()


def segregate(file, name, extention):
    # print (name)
    if extention in ['.txt', '.xlsx', '.pdf']:
        try:
            shutil.move(os.path.join(given_dir, file),
                        os.path.join(given_dir, 'Files/Documents'))
        except FileExistsError:
            print('File already exists')
    elif extention in ['.jpg', '.png']:
        try:
            shutil.move(os.path.join(given_dir, file),
                        os.path.join(given_dir, 'Files/Pictures'))
        except FileExistsError:
            print('File already exists')
    elif extention in ['.zip']:
        try:
            shutil.move(os.path.join(given_dir, file),
                        os.path.join(given_dir, 'Files/Compressed'))
        except FileExistsError:
            print('File already exists')
    elif extention in ['.pkg', '.exe', '.dmg']:
        try:
            shutil.move(os.path.join(given_dir, file),
                        os.path.join(given_dir, 'Files/Installation'))
        except FileExistsError:
            print('File already exists')
    elif extention in ['.mkv', 'mp4']:
        try:
            shutil.move(os.path.join(given_dir, file),
                        os.path.join(given_dir, 'Files/Videos'))
        except FileExistsError:
            print('File already exists')
    elif extention in ['.mp3']:
        try:
            shutil.move(os.path.join(given_dir, file),
                        os.path.join(given_dir, 'Files/Audio'))
        except FileExistsError:
            print('File already exists')
    else:
        try:
            shutil.move(os.path.join(given_dir, file),
                        os.path.join(given_dir, 'Files/Miscellaneous'))
        except FileExistsError:
            print('File already exists')


# os.chdir('/Users/sheyril/Desktop')
files_list = os.listdir(given_dir)
files_list.remove('.DS_Store')
files_list.remove('Files')
#print(files_list)

for file in files_list:
    name, extention = os.path.splitext(file)
    # print("this is the name: ", name)
    # print("this is the extention: ", extention)
    segregate(file, name, extention)
print('Done!')
