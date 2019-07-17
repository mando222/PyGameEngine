#!/usr/bin/python

import pygame
from pygame.locals import *
from logger import *
from units import *
from assetLoad import *
import ConfigParser
import uuid

def create_unit(faction, name):
    fileName = faction+'.fac'
    HERE = Path(__file__).parent.resolve()
    PATH = HERE / 'factions'/ fileName
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
        with open(fileName, 'wb') as file:
            faction_file.write(file)
        logging.info("Unit %s Created", name)  

def edit_unit(action, faction, name, tag, value='none'):
    fileName = faction+'.fac'
    HERE = Path(__file__).parent.resolve()
    PATH = HERE / 'factions'/ fileName
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
    else:
        logging.info("error unit %s doesn't exist", name)
        logging.info("Need to impliment error handling here")

def create_faction(name):
    fileName = name+'.fac'
    HERE = Path(__file__).parent.resolve()
    PATH = HERE / 'factions' / fileName
    print PATH
    if PATH.exists():
        logging.info("error faction file for %s already exists", name)
        logging.info("Need to impliment error handling here")
    else:
        print 'creating faction file'
        config = ConfigParser.RawConfigParser()
        config.add_section('faction_meta')
        faction_id = uuid.uuid4().hex
        config.set('faction_meta', 'name', name)
        config.set('faction_meta', 'id', faction_id)
        config.set('faction_meta', 'points', '1000')
        with open(fileName, 'wb') as file:
            config.write(file)
        logging.info("Faction %s Created", name)

#testing code need to remove once done
#create_faction('testfaction')
#create_unit('testunit', 'testfaction')