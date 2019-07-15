#!/usr/bin/python

import pygame
from pygame.locals import *
from logger import *
from units import *
from assetLoad import *

##########################################
# Builds an array of all active units
########################################## 
def update_units():
    unit1 = load_image('unit')
    first_unit = unitObject(unit1, 1, 1)
    second_unit = unitObject(unit1, 10, 1)
    unit_list = [first_unit,second_unit]
    return unit_list