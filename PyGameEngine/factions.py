#!/usr/bin/env python3
import os
import pygame
import uuid
from pygame.locals import *
from units import *
from asset_load import *
import configparser
from logger import logging


class faction_object:
    def __init__(self, faction_name):
        self.faction_name=faction_name
        self.file_name = './factions/'+self.faction_name+'.fac'
        self.base_dir = Path(__file__).parent.resolve()
        self.PATH = self.base_dir / self.file_name
        self.parser = configparser.ConfigParser()
        if self.PATH.exists():
            self.load_faction()
        else:
            self.create_faction()
            self.load_faction()

    ##########################################
    # loads a faction file
    # factino_name is the name of the faction
    ##########################################
    def load_faction(self):
        if self.PATH.exists():
            self.parser.read(self.PATH)
            self.name=self.parser.get('faction_meta', 'name')
            self.faction_id=self.parser.get('faction_meta', 'faction_id')
            self.points=self.parser.get('faction_meta', 'points')

            #need logic to parse unit info here

        else:
            logging.info("Faction %s doesn't exist", self.faction_name)
            logging.info("Creating Faction %s", self.faction_name)
            self.create_faction()

    ##########################################
    # creates a faction file
    # factino_name is the name of the faction
    ##########################################
    def create_faction(self):
        if self.PATH.exists():
            logging.info("error faction file for %s already exists", self.faction_name)
            logging.info("Need to impliment error handling base_dir")
        else:
            logging.info("creating faction file %s", self.faction_name)
            self.parser.read(self.PATH)
            self.parser['faction_meta'] = {
                'name':self.faction_name,
                'faction_id':uuid.uuid4().hex,
                'points':'1000'  
            }
            with open(self.PATH, 'w') as configfile:
                self.parser.write(configfile)
            logging.info("Faction %s Created", self.faction_name)

    ##########################################
    # creates a unit entry in a faction file
    # factino_name is the name of the faction
    # name is the name of the unit being created
    ##########################################
    def create_unit(self, name):
        self.parser.read(self.PATH)
        if self.PATH.exists():
            print('faction file exists')
        else:
            logging.info("Faction %s doesn't exist", self.faction_name)
            logging.info("Creating Faction %s", self.faction_name)
            self.create_faction()

        # if self.parser.get(name, name).exists(): # check if the units section has been made
        #     logging.info("error unit %s already exists", self.faction_name)
        # else:
        self.parser[name] = {
            'name':name,
            'id':uuid.uuid4().hex,
            'point_alowance':'100'  
        }
        with open(self.PATH, 'w') as write_file:
            self.parser.write(write_file)
        logging.info("Unit %s Created", name)
    
    ##########################################
    # edits a unit entry in a faction file
    # action is the type of operation to do
    # faction_name is the name of the faction that owns the unit
    # name is the name of the unit
    # tag is the name of the atribute to be edited
    # value='none' if aplicable is the value to set the tag to
    ##########################################
    def edit_unit(self, action, name, tag, value='none'):
        self.parser.read(self.PATH)
        if self.parser.get(name, name).exists():
            if action == 'remove':
                self.parser.remove_option(name, tag)
                logging.info("removed unit %s tag %s", name, tag)
            elif action == 'add':
                self.parser.set(name, tag, value)
                logging.info("added unit %s tag %s", name, tag)
            elif action == 'edit':
                self.parser.set(name, tag, value)
                logging.info("edited unit %s tag %s", name, tag)
            with open(self.PATH, 'w') as write_file:
                self.parser.write(write_file)
        else:
            logging.info("error unit %s doesn't exist", name)
            logging.info("Need to impliment error handling base_dir")


new_faction = faction_object('nord')
new_faction.create_faction()
new_faction.create_unit('berzerker')


print(new_faction.faction_name)
print(new_faction.faction_id)
print(new_faction.points)
