#  two arguments, the folder and the new folder that I want to create
#  ('Pokedex' 'new')

import sys
import os
from PIL import Image

#  grab first and second argument
actualFolder = sys.argv[1]
newFolder = sys.argv[2]

if not os.path.exists(newFolder):
    try:
        os.makedirs(newFolder)
    except OSError:
        print(f'Creation of the directory {newFolder} has failed.')
        
for filename in os.listdir(actualFolder):
    img = Image.open(f'{actualFolder}\{filename}')
    clean_name = os.path.splitext(filename)[0]

    img.save(f'{newFolder}\{clean_name}.png', 'png')
    print(f'{filename} has been converted!')