#!/usr/bin/env python3

import pygame
from pygame.locals import *
from unit_operations import *
from key_bindings import *

def init_key_bindings():
    current_keys = key_bindings()
    return current_keys


def key_event(key, unit_list, key_bindings):
        if (key == key_bindings.MENU):
            print ('need to implement a menu')
        elif (key == key_bindings.TEST_SPAWN_RIGHT):
            unit_list = add_units(unit_list, 'unit')
        elif (key == key_bindings.CAMERA_DOWN):
            unit_list = move_units(unit_list, 'S', unit_list[0].instanceID)
        elif (key == key_bindings.CAMERA_UP):
            unit_list = move_units(unit_list, 'N', unit_list[0].instanceID)
        elif (key == key_bindings.CAMERA_RIGHT):
            unit_list = move_units(unit_list, 'E', unit_list[0].instanceID)
        elif (key == key_bindings.CAMERA_LEFT):
            unit_list = move_units(unit_list, 'W', unit_list[0].instanceID)
        elif (key == key_bindings.DELETE or key_bindings.ALT_DELETE):
            unit_list = delete_units(unit_list, unit_list[0].instanceID)