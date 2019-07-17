#!/usr/bin/env python3

import os
import ConfigParser
import pygame
import uuid
from pygame.locals import *
from logger import *
from units import *
from assetLoad import *
from unit_stat_values import *


##########################################
# creates a unit entry in a faction file
# factino_name is the name of the faction
# name is the name of the unit being created
##########################################
def create_unit(faction_name, name):
    fileName = faction_name+'.fac'
    HERE = Path(__file__).parent.resolve()
    faction_path = os.path.join(HERE, "faction")
    PATH = faction_path / fileName
    faction_file = ConfigParser.RawConfigParser()
    faction_file.read(fileName)
    if faction_file.get(name, name).exists(): # check if the units section has been made
        logging.info("error unit %s already exists", name)
        logging.info("Need to impliment error handling here")
    else:
        faction_file.add_section(name)
        faction_file.set(name, 'name', name)
        unit_id = uuid.uuid4().hex
        faction_file.set(name, 'id', unit_id)
        faction_file.set(name, 'point_alowance', points.UNIT_ALLOWANCE)
        with open(fileName, 'wb') as file:
            faction_file.write(file)
        logging.info("Unit %s Created", name)

##########################################
# edits a unit entry in a faction file
# action is the type of operation to do
# faction_name is the name of the faction that owns the unit
# name is the name of the unit
# tag is the name of the atribute to be edited
# value='none' if aplicable is the value to set the tag to
##########################################
def edit_unit(action, faction_name, name, tag, value='none'):
    fileName = faction_name+'.fac'
    HERE = Path(__file__).parent.resolve()
    faction_path = os.path.join(HERE, "faction")
    PATH = faction_path / fileName
    faction_file = ConfigParser.RawConfigParser()
    faction_file.read(fileName)
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
        with open(faction_file, 'wb') as file:
            config.write(file)
    else:
        logging.info("error unit %s doesn't exist", name)
        logging.info("Need to impliment error handling here")

##########################################
# creates a faction file
# factino_name is the name of the faction
##########################################
def create_faction(faction_name):
    fileName = faction_name+'.fac'
    faction_path = os.path.join(Path(__file__).parent.resolve(), "faction", fileName)
    print faction_path
    PATH = faction_path / fileName
    if PATH.exists():
        logging.info("error faction file for %s already exists", faction_name)
        logging.info("Need to impliment error handling here")
    else:
        print 'creating faction file'
        config = ConfigParser.RawConfigParser()
        config.add_section('faction_meta')
        faction_id = uuid.uuid4().hex
        config.set('faction_meta', 'name', faction_name)
        config.set('faction_meta', 'id', faction_id)
        config.set('faction_meta', 'points', points.FACTION_ALLOWANCE)
        with open(fileName, 'wb') as file:
            config.write(file)
        logging.info("Faction %s Created", faction_name)

#testing code need to remove once done
create_faction('testfaction')
#create_unit('testunit', 'testfaction')
