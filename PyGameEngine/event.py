#!/usr/bin/env python3

import pygame
from units import *
from unit_operations import *
from pygame.locals import *
from logger import logging
from key_actions import *

def event_handler(unit_list, key_bindings):
    for event in pygame.event.get():
        logging.debug(event)        
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            key_event(event.key, unit_list, key_bindings)