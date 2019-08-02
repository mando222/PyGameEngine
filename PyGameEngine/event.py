#!/usr/bin/env python3
import pygame
from pygame.locals import *
from logger import *
from key_actions import *


class event_handler:
    def __init__(self, game):

        for event in pygame.event.get():
            logging.debug(event)        
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if game.game_state == 'main_menu':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  
                        button_clicked = [button for button in [game.main_menu.find_game_button,game.main_menu.settings_button,game.main_menu.exit_button] if button.rect.collidepoint(event.pos)]
                        for button in button_clicked:
                            print('clicked button', button.name)
                            if button.name == 'find_game_button':
                                game.game_state = 'in_game'
                                game.game_display.blit(game.background, (0, 0))
                            elif button.name == 'settings_button':
                                print('need to implement settings')
                            elif button.name == 'exit_button':
                                pygame.quit()
                                quit()
            elif game.game_state == 'pause_menu':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # Left click
                        button_clicked = [button for button in [game.pause_menu.resume_button,game.pause_menu.settings_button,game.pause_menu.exit_button] if button.rect.collidepoint(event.pos)]
                        for button in button_clicked:
                            if button.name == 'resume_button':
                                game.game_state = 'in_game'
                                game.game_display.blit(game.background, (0, 0))
                            elif button.name == 'settings_button':
                                print('need to implement settings')
                            elif button.name == 'exit_button':
                                game.game_state = 'main_menu'
                                game.game_display.blit(game.background, (0, 0))
            elif game.game_state == 'in_game':
                if event.type == pygame.KEYDOWN:
                    game_state = key_event(event.key, game.unit_list, game.key_bindings)
                    if not game_state == 0:
                        game.game_state = game_state
                        game.game_display.blit(game.background, (0, 0))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # Left click
                        clicked_units = [unit for unit in game.unit_list if unit.rect.collidepoint(event.pos)]
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