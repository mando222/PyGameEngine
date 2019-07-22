#!/usr/bin/env python3

import numpy as np
import uuid
import pygame
from pygame.locals import *
from units import *
from asset_load import *
from logger import logging


##########################################
# addes a unit to the unit_list array
########################################## 
def add_units(unit_list, name, faction='default', height=1, speed=1, state='alive'):
    unit_image = load_image(name)
    unit_instanceID = uuid.uuid4().hex
    new_unit = unitObject(unit_instanceID, name, faction, unit_image, height, speed, 'alive')
    unit_list.append(new_unit)
    return unit_list


##########################################
# directionally moves a unit from the unit list by unit_instanceID
########################################## 
def move_units(unit_list, direction, unit_instanceID):
    for unit in unit_list:
        if unit.instanceID == unit_instanceID: 
                unit.move(direction)


##########################################
# deletes a unit from the unit list by unit_instanceID
########################################## 
def delete_units(unit_list, unit_instanceID):
    for unit in unit_list:
        if unit.instanceID == unit_instanceID:
            unit.state = 'dead'   
            logging.info('Unit %s dead', unit_instanceID)
    return unit_list