#!/usr/bin/env python3
from logger import logging
import uuid
from asset_load import load_image

class menu_object:
    def __init__(self,window_hight=800, window_width=600):
        self.button_width = 100
        self.button_hight = 32
        self.button_dementions = (self.button_width, self.button_hight)
        self.menu_position_y = (window_hight/2)-(self.button_hight*3/2)
        self.menu_position_x = (window_width/2)-(self.button_width/2)
        self.find_game_button = menu_button_object('find_game_button',(self.menu_position_x, self.menu_position_y), self.button_dementions)
        self.settings_button = menu_button_object('settings_button', (self.menu_position_x, self.menu_position_y+10+self.button_hight), self.button_dementions)
        self.exit_button = menu_button_object('exit_button', (self.menu_position_x, self.menu_position_y+20+self.button_hight*2), self.button_dementions)
        self.pos = (self.menu_position_y, self.menu_position_x)


class menu_button_object:
    def __init__(self, name, pos, button_dementions):
        self.name=name
        self.image = load_image(name, file_path='assets/menus')
        self.rect = self.image.get_rect().move(pos)
        self.pos = pos

class backgroundObject:
    def __init__(self, image):
        self.image = image