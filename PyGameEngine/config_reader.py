#!/usr/bin/env python3

#import ConfigParser
from pathlib import Path
import configparser

##########################################
# Initialization of the config file.  
# Checks for the config file and 
# if it isn't there creates it.
##########################################
def initConfig():
    fileName = 'config.cfg'
    HERE = Path(__file__).parent.resolve()
    PATH = HERE / fileName
    if PATH.exists():
        print ('config file found')
    else:
        print ('creating config file')
        config = configparser.ConfigParser()
        config.add_section('graphics')
        config.add_section('sound')
        config.add_section('difficulty')
        config.add_section('logging')
        config.set('graphics', 'display_width', '800')
        config.set('graphics', 'display_height', '600')
        config.set('sound', 'volume', '10')
        config.set('difficulty', 'difficulty', 'hard')
        config.set('logging', 'log_file', 'system.log')
        config.set('logging', 'log_level', 'INFO')
        config.set('logging', 'logging_mode', 'a')
        with open(PATH, 'wb') as configfile:
            config.write(configfile)

##########################################
# Reads a value from the config file.
# sectionName is the name of the section in the file
# tag is the key of the config value
# typeVal is the type (string, int, float, bool) of the value
##########################################    
def readConfig(sectionName, tag, typeVal):
    fileName = 'config.cfg'
    config = configparser.ConfigParser()
    config.read(fileName)
    if typeVal== 'int':
        configValue = config.getint(sectionName, tag)
    elif typeVal== 'string':
        configValue = config.get(sectionName, tag)
    elif typeVal== 'bool':
        configValue = config.getboolean(sectionName, tag)
    elif typeVal== 'float':
        configValue = config.getfloat(sectionName, tag)
    print ("config values read %s", configValue)
    # logging.debug("config values read %s", configValue)
    return configValue


##########################################
# changes a value in the config file from the game settings
# sectionName the name of the section
# tag is the key that you are changing to value for
# value is the new value to set
##########################################
def changeSetting(sectionName, tag, value):
    fileName = 'config.cfg'
    config.set(sectionName, tag, value)
    logging.debug("config values read %s, %s, %s", sectionName, tag, value)
    with open(fileName, 'wb') as configfile:
        config.write(configfile)
