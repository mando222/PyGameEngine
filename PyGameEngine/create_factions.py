#!/usr/bin/env python3

import os
import pygame
import uuid
from pygame.locals import *
from units import *
from asset_load import *
from unit_stat_values import *
import configparser
from logger import logging

##########################################
# creates a faction file
# factino_name is the name of the faction
##########################################
def create_faction(faction_name):
    file_name = './factions/'+faction_name+'.fac'
    base_dir = Path(__file__).parent.resolve()
    file_path = base_dir / file_name
    if file_path.exists():
        logging.info("error faction file for %s already exists", faction_name)
        logging.info("Need to impliment error handling base_dir")
    else:
        logging.info("creating faction file %s", faction_name)
        faction_file = configparser.ConfigParser()
        faction_file.read(file_path)
        faction_file.add_section('faction_meta')
        faction_id = uuid.uuid4().hex
        faction_file.set('faction_meta', 'name', faction_name)
        faction_file.set('faction_meta', 'id', faction_id)
        faction_file.set('faction_meta', 'points', '1000')
        with open(file_path, 'w') as write_file:
            faction_file.write(write_file)
        logging.info("Faction %s Created", faction_name)

##########################################
# creates a unit entry in a faction file
# factino_name is the name of the faction
# name is the name of the unit being created
##########################################
def create_unit(faction_name, name):
    file_name = './factions/'+faction_name+'.fac'
    base_dir = Path(__file__).parent.resolve()
    file_path = base_dir / file_name
    parser = configparser.ConfigParser()
    parser.read(file_path)
    if file_path.exists():
        if parser.get(name, name).exists(): # check if the units section has been made
            logging.info("error unit %s already exists", name)
            logging.info("Need to impliment error handling base_dir")
        else:
            parser.add_section(name)
            parser.set(name, 'name', name)
            unit_id = uuid.uuid4().hex
            parser.set(name, 'id', unit_id)
            parser.set(name, 'point_alowance', '100')
            with open(file_path, 'w') as write_file:
                parser.write(write_file)
            logging.info("Unit %s Created", name)
    else:
        logging.info("Base faction doesn't exist")

##########################################
# edits a unit entry in a faction file
# action is the type of operation to do
# faction_name is the name of the faction that owns the unit
# name is the name of the unit
# tag is the name of the atribute to be edited
# value='none' if aplicable is the value to set the tag to
##########################################
def edit_unit(action, faction_name, name, tag, value='none'):
    file_name = './factions/'+faction_name+'.fac'
    base_dir = Path(__file__).parent.resolve()
    file_path = base_dir / file_name
    parser = configparser.ConfigParser()
    parser.read(file_path)
    if parser.get(name, name).exists():
        if action == 'remove':
            parser.remove_option(name, tag)
            logging.info("removed unit %s tag %s", name, tag)
        elif action == 'add':
            parser.set(name, tag, value)
            logging.info("added unit %s tag %s", name, tag)
        elif action == 'edit':
            parser.set(name, tag, value)
            logging.info("edited unit %s tag %s", name, tag)
        with open(file_path, 'w') as write_file:
            parser.write(write_file)
    else:
        logging.info("error unit %s doesn't exist", name)
        logging.info("Need to impliment error handling base_dir")

#testing code need to remove once done
create_faction('testfaction')
#create_unit('testunit', 'testfaction')
