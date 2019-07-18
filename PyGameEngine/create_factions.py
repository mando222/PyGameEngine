#!/usr/bin/env python3

import os
import pygame
import uuid
from pygame.locals import *
from logger import *
from units import *
from asset_load import *
from unit_stat_values import *
# python 2 dependencies
import ConfigParser
# python 3 dependencies
#import configparser

##########################################
# creates a faction file
# factino_name is the name of the faction
##########################################
def create_faction(faction_name):
    file_name = faction_name+'.fac'
    file_path = os.path.join(Path(__file__).parent.resolve(), "faction", file_name)
    print (file_path)
    if file_path.exists():
        logging.info("error faction file for %s already exists", faction_name)
        logging.info("Need to impliment error handling base_dir")
    else:
        logging.info("creating faction file %s", faction_name)
        faction_file = ConfigParser.RawConfigParser()
        faction_file.add_section('faction_meta')
        faction_id = uuid.uuid4().hex
        faction_file.set('faction_meta', 'name', faction_name)
        faction_file.set('faction_meta', 'id', faction_id)
        faction_file.set('faction_meta', 'points', points.FACTION_ALLOWANCE)
        with open(file_name, 'wb') as write_file:
            faction_file.write(write_file)
        logging.info("Faction %s Created", faction_name)

##########################################
# creates a unit entry in a faction file
# factino_name is the name of the faction
# name is the name of the unit being created
##########################################
def create_unit(faction_name, name):
    file_name = faction_name+'.fac'
    base_dir = Path(__file__).parent.resolve()
    file_path = base_dir / file_name
    faction_file = ConfigParser.RawConfigParser()
    faction_file.read(file_name)
    if file_path.exists():
        if faction_file.get(name, name).exists(): # check if the units section has been made
            logging.info("error unit %s already exists", name)
            logging.info("Need to impliment error handling base_dir")
        else:
            faction_file.add_section(name)
            faction_file.set(name, 'name', name)
            unit_id = uuid.uuid4().hex
            faction_file.set(name, 'id', unit_id)
            faction_file.set(name, 'point_alowance', points.UNIT_ALLOWANCE)
            with open(file_name, 'wb') as write_file:
                faction_file.write(write_file)
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
    file_name = faction_name+'.fac'
    base_dir = Path(__file__).parent.resolve()
    file_path = base_dir / file_name
    faction_file = ConfigParser.RawConfigParser()
    faction_file.read(file_name)
    if faction_file.get(name, name).exists():
        if action == 'remove':
            config.remove_option(name, tag)
            logging.info("removed unit %s tag %s", name, tag)
        elif action == 'add':
            faction_file.set(name, tag, value)
            logging.info("added unit %s tag %s", name, tag)
        elif action == 'edit':
            faction_file.set(name, tag, value)
            logging.info("edited unit %s tag %s", name, tag)
        with open(faction_file, 'wb') as write_file:
            faction_file.write(write_file)
    else:
        logging.info("error unit %s doesn't exist", name)
        logging.info("Need to impliment error handling base_dir")

#testing code need to remove once done
create_faction('testfaction')
#create_unit('testunit', 'testfaction')
