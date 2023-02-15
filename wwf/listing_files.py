import os
from pathlib import Path

def printline(content = None):
    if content is not None:
        print(f'\n{content}\n')
    else:
        print('=>' * 10)

# list all files in a directory

printline('listing all filles in a directory')

basepath = 'my_directory/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)

printline()

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)

printline()

basepath = Path('my_directory')
files_in_basepath = basepath.iterdir()

for item in files_in_basepath:
    if item.is_file():
        print(item.name)

# listing all subdirectories

printline('listing all subdirectories')

basepath = 'my_directory'

for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        print(entry)

printline()

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)

printline()

basepath = Path('my_directory')

for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)

# getting file attributes

printline('getting file attributes')


print('this has been added')

print('this will be a pull request')


# 'somethig from here'






















