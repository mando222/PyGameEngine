#!/usr/bin/env python3

import pygame
from logger import *
from units import *
from unit_operations import *
from pygame.locals import *

def event_handler(unit_list):
    for event in pygame.event.get():
        logging.debug(event)        
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN and (event.key == K_ESCAPE):
            print ('need to implement a menu')
        elif event.type == KEYDOWN and (event.key == K_f):
            unit_list = add_units(unit_list, 'unit')
        elif event.type == KEYDOWN and (event.key == K_d):
            unit_list = add_units(unit_list, 'unit',direction='E')
        elif event.type == KEYDOWN and (event.key == K_BACKSPACE or K_DELETE):
            unit_list = delete_units(unit_list, unit_list[0].instanceID)