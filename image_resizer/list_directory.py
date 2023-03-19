from os import listdir
from os.path import isfile, join
from PIL import Image
import os

def is_image(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))

start_path = 'E:/images'

all_paths = [start_path]

i = 0

while i < len(all_paths):
    onlyfolders = [f for f in listdir(all_paths[i]) if not isfile(join(all_paths[i], f))]

    for folder in onlyfolders:
        folder_path = join(all_paths[i], folder)

        if folder_path not in all_paths and folder != 'resize':
            all_paths.append(join(all_paths[i], folder))
    
    i += 1

print("-"*100)

image_size = (1680, 1050)

for path in all_paths:
    print("Scanning path: ", path)

    all_files = listdir(path)

    for file in all_files:
        file_path = join(path, file)
        if isfile(file_path) and is_image(file_path):
            i = Image.open(file_path)
            file_name, file_extension = os.path.splitext(file)
            i.thumbnail(image_size)
            if not os.path.exists(path + '/resize'):
                os.makedirs(path + '/resize')
            print('saving file: ', file_name)
            i.save(path + '/resize/{}_small{}'.format(file_name, file_extension))

    print("-"*100)

