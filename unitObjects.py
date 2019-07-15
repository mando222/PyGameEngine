#!/usr/bin/python

import pygame
from pygame.locals import *
from logger import *
from units import *
from assetLoad import *
import numpy as np


##########################################
# Builds an array of all active units
########################################## 
def add_units(unit_list, name):
    unit_image = load_image(name)
    new_unit = unitObject(unit_image, 1, 1)
    unit_list.append(new_unit)
    return unit_list

def delete_units(unit_list):
    unit1 = load_image('unit')
    first_unit = unitObject(unit1, 1, 1)
    second_unit = unitObject(unit1, 10, 1)
    unit_list = [first_unit,second_unit]
    return unit_list