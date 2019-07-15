#!/usr/bin/python

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
from configReader import *
from logger import *
from units import *
from assetLoad import *

initConfig()
log_file=readConfig('logging', 'log_file', 'string')
log_level=readConfig('logging', 'log_level', 'string')
logging_mode=readConfig('logging', 'logging_mode', 'string')
initLogging(log_file,log_level,logging_mode)
initStatus = pygame.init()

logging.info('Game Starting with %i moduals Succeding and %i Failures', initStatus[0], initStatus[1])

display_width = readConfig('graphics', 'display_width', 'int')
display_height = readConfig('graphics', 'display_height', 'int')
logging.info('Screen resolution set to %i x %i', display_width, display_height)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PyGameEngine')
logging.info('Game Has Started Without Errors')

#Loading assets
unit1 = load_image('unit')
background = load_image('whitebackground')
game_display.blit(background, (0, 0))


first_unit = GameObject(unit1, 1, 1)
second_unit = GameObject(unit1, 10, 1)


unit_list = [first_unit,second_unit]

def event_handler():
    for event in pygame.event.get():
        logging.debug(event)        
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN and (event.key == K_ESCAPE):
            print 'escape'
        elif event.type == KEYDOWN and (event.key == K_f):
            print 'f'

def render_units():
    for unit in unit_list:
        game_display.blit(background, unit.pos, unit.pos)
    for unit in unit_list:
        unit.move()
        game_display.blit(unit.image, unit.pos)
    pygame.display.update()
    pygame.time.delay(100)
    
while True:
    logging.debug("tick")
    event_handler()
    render_units()
