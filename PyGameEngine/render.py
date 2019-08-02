 #!/usr/bin/env python3
import pygame
from pygame.locals import *
from logger import *
 
class render():   
    def __init__(self, game):
        if game.game_state == 'main_menu':
            game.game_display.blit(game.background, game.main_menu.find_game_button.pos)
            game.game_display.blit(game.main_menu.find_game_button.image, game.main_menu.find_game_button.pos)
            game.game_display.blit(game.background, game.main_menu.settings_button.pos)
            game.game_display.blit(game.main_menu.settings_button.image, game.main_menu.settings_button.pos)
            game.game_display.blit(game.background, game.main_menu.exit_button.pos)
            game.game_display.blit(game.main_menu.exit_button.image, game.main_menu.exit_button.pos)
        elif game.game_state == 'pause_menu':
            game.game_display.blit(game.background, game.pause_menu.resume_button.pos)
            game.game_display.blit(game.pause_menu.resume_button.image, game.pause_menu.resume_button.pos)
            game.game_display.blit(game.background, game.pause_menu.settings_button.pos)
            game.game_display.blit(game.pause_menu.settings_button.image, game.pause_menu.settings_button.pos)
            game.game_display.blit(game.background, game.pause_menu.exit_button.pos)
            game.game_display.blit(game.pause_menu.exit_button.image, game.pause_menu.exit_button.pos)
        elif game.game_state == 'in_game':
            game.game_display.blit(game.background, (0, 0))
            for unit in game.unit_list:
                game.game_display.blit(game.background, unit.pos, unit.pos)
            for unit in game.unit_list:
                if unit.state== 'alive':
                    game.game_display.blit(unit.image, unit.pos)
        pygame.display.update()
        pygame.time.delay(100)