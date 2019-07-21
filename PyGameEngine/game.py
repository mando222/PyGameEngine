#!/usr/bin/env python3

########################################
# This is a first crack at a python game.
# The idea is to have a full RTS style 
# game by the end of my work.
# Author mando222 7/14/2019
# python version 2.9
# using https://www.pygame.org/docs/tut/
########################################
import pygame
from pygame.locals import *
from config_reader import *
from logger import *
from units import *
from asset_load import *
from event import *
from init_dir import *

init_dirs()
initConfig() #read startup options from config file
log_file=read_config('config', 'logging', 'log_file', 'string')
log_dir=read_config('config', 'logging', 'log_dir', 'string')
log_level=read_config('config', 'logging', 'log_level', 'string')
logging_mode=read_config('config', 'logging', 'logging_mode', 'string')
initLogging(log_file, log_dir, log_level,logging_mode) #start the logger
initStatus = pygame.init() #start pygame modules
logging.info('Game Starting with %i moduals Succeding and %i Failures', initStatus[0], initStatus[1])

display_width = read_config('config', 'graphics', 'display_width', 'int')
display_height = read_config('config', 'graphics', 'display_height', 'int')
logging.info('Screen resolution set to %i x %i', display_width, display_height)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PyGameEngine')
logging.info('Game Has Started Without Errors')
clock = pygame.time.Clock()

#Setup background
background = load_image('whitebackground')
game_display.blit(background, (0, 0))

#Setup global arrays
unit_list = []
running = True
   
def render_units(unit_list):    
    for unit in unit_list:
        game_display.blit(background, unit.pos, unit.pos)
    for unit in unit_list:
        if unit.state== 'alive':
            unit.move()
            game_display.blit(unit.image, unit.pos)
    pygame.display.update()
    pygame.time.delay(100)
    
while running:
    logging.debug("tick")
    event_handler(unit_list)
    render_units(unit_list)
    clock.tick(144)
