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
from init_dir import *
import socket
import select
import random
import time
from key_bindings import key_bindings
from unit_operations import *
from key_actions import *
from menu import menu_object


class game_engine:
    def __init__(self):
        init_dirs()
        self.running_config = config_reader() #read startup options from config file
        self.log_file = self.running_config.read_config('logging', 'log_file', 'string')
        self.log_dir = self.running_config.read_config('logging', 'log_dir', 'string')
        self.log_level = self.running_config.read_config('logging', 'log_level', 'string')
        self.logging_mode = self.running_config.read_config('logging', 'logging_mode', 'string')
        initLogging(self.log_file, self.log_dir, self.log_level,self.logging_mode) #start the logger
        self.initStatus = pygame.init() #start pygame modules
        self.key_bindings = key_bindings()
        logging.info('Game Starting with %i moduals Succeding and %i Failures', self.initStatus[0], self.initStatus[1])

        self.display_width = self.running_config.read_config('graphics', 'display_width', 'int')
        self.display_height = self.running_config.read_config('graphics', 'display_height', 'int')
        logging.info('Screen resolution set to %i x %i', self.display_width, self.display_height)

        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('PyGameEngine')
        logging.info('Game Has Started Without Errors')
        self.clock = pygame.time.Clock()

        #Networking support 



        #Setup background
        self.background = load_image('whitebackground')
        self.menu_background = load_image('whitebackground')
        self.game_display.blit(self.menu_background, (0, 0))

        #Setup global arrays
        self.unit_list = []
        self.running = True
        self.game_state = 'main_menu'
        self.menu=menu_object(self.display_height, self.display_width)
        
    def render_units(self):   
        if self.game_state == 'main_menu':
            self.game_display.blit(self.menu_background, self.menu.find_game_button.pos)
            self.game_display.blit(self.menu.find_game_button.image, self.menu.find_game_button.pos)
            self.game_display.blit(self.menu_background, self.menu.settings_button.pos)
            self.game_display.blit(self.menu.settings_button.image, self.menu.settings_button.pos)
            self.game_display.blit(self.menu_background, self.menu.exit_button.pos)
            self.game_display.blit(self.menu.exit_button.image, self.menu.exit_button.pos)
        elif self.game_state == 'play_menu':
            print('need to impliment')
        elif self.game_state == 'in_game':
            for unit in self.unit_list:
                self.game_display.blit(self.background, unit.pos, unit.pos)
            for unit in self.unit_list:
                if unit.state== 'alive':
                    self.game_display.blit(unit.image, unit.pos)




        pygame.display.update()
        pygame.time.delay(100)
    

    def event_handler(self):
        for event in pygame.event.get():
            logging.debug(event)        
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if self.game_state == 'main_menu':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  
                        button_clicked = [button for button in [self.menu.find_game_button,self.menu.settings_button,self.menu.exit_button] if button.rect.collidepoint(event.pos)]
                        for button in button_clicked:
                            print('clicked button', button.name)
                            if button.name == 'find_game_button':
                                self.game_state = 'in_game'
                            elif button.name == 'settings_button':
                                print('need to implement settings')
                            elif button.name == 'exit_button':
                                pygame.quit()
                                quit()
            elif self.game_state == 'play_menu':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # Left click
                        print('mouseclick', event.button)
                        print('pos', event.pos) 
            elif self.game_state == 'in_game':
                if event.type == pygame.KEYDOWN:
                    game_state = key_event(event.key, self.unit_list, self.key_bindings)
                    if not game_state == 0:
                        self.game_state = game_state
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # Left click
                        clicked_units = [unit for unit in self.unit_list if unit.rect.collidepoint(event.pos)]
                        for unit in clicked_units:
                            print('clicked unit', unit)
                        print('mouseclick', event.button)
                        print('pos', event.pos) 
                    elif event.button == 2: # middle mouse clicked
                        print('mouseclick', event.button)
                        print('pos', event.pos)
                    elif event.button == 3: # Left click
                        print('mouseclick', event.button)
                        print('pos', event.pos)

    def run(self):
            logging.debug("tick")
            self.event_handler()
            self.render_units()
            self.clock.tick(144)


game_instance = game_engine()
while game_instance.running:
    game_instance.run()