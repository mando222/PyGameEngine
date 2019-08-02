#!/usr/bin/env python3

import os, sys
import pygame
from pygame.locals import *
from pathlib2 import Path
from logger import logging

##########################################
# Loads an bmp image from a file
# name is the name of the file - extention
########################################## 
def load_image(name, colorkey=None, file_path='assets'):
    filetypes=['.png','.bmp','.jpg']
    for ext in filetypes:
        if Path(os.path.join(file_path, name+ext)).is_file():
            fullname = os.path.join(file_path, name+ext)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        logging.info('Cannot load image: %s', name)
        raise SystemExit(message)
    image = image.convert()
    # image = image.convert_alpha()
    #set colorkey
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image