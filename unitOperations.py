#!/usr/bin/python

import pygame
from pygame.locals import *
from logger import *
from units import *
from assetLoad import *
import numpy as np
import uuid


##########################################
# addes a unit to the unit_list array
########################################## 
def add_units(unit_list, name):
    unit_image = load_image(name)
    unit_instanceID = uuid.uuid4().hex
    new_unit = unitObject(unit_instanceID, name, unit_image, 1, 1, 'alive')
    unit_list.append(new_unit)
    return unit_list

##########################################
# deletes a unit from the unit list by unit_instanceID
########################################## 
def delete_units(unit_list, unit_instanceID):
      
    for unit in unit_list:
        if unit.instanceID == unit_instanceID:
            unit.state = 'dead'   
            logging.info('Unit %s dead', unit_instanceID)\
    return unit_list