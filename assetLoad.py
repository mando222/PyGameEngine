#!/usr/bin/python

import os, sys
import pygame
from pygame.locals import *

##########################################
# Loads an bmp image from a file
# name is the name of the file - extention
########################################## 
def load_image(name):
    fullname = os.path.join('assets', name+'.bmp')
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    return image