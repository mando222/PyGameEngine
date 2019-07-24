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
def add_units(unit_list, name, faction='default'):
    unit_image = load_image(name)
    new_unit = unitObject(name, faction, unit_image)
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
                unit.destroy()