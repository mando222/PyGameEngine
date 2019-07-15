#!/usr/bin/python

import pygame
from pygame.locals import *
from configReader import *
from logger import *

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
logging.info('Game Has Started Without Errors')

            
pygame.display.set_caption('Our Game')


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

while True:
    logging.debug("tick")
    event_handler()
    
    pygame.display.update()
