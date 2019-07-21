#!/usr/bin/env python3

#import ConfigParser
from pathlib import Path
from configparser import ConfigParser

##########################################
# Initialization of the config file.  
# Checks for the config file and 
# if it isn't there creates it.
##########################################
def initConfig():
    fileName = './config/config.cfg'
    HERE = Path(__file__).parent.resolve()
    PATH = HERE / fileName
    if PATH.exists():
        print ('config file found')
    else:
        print ('creating config file')
        config = ConfigParser()
        config['graphics'] = {
            'display_width':'800',
            'display_height':'600'
        }
        config['sound'] = {
            'volume':'10'
        }
        config['difficulty'] = {
            'difficulty':'hard'
        }
        config['logging'] = {
            'log_file':'system.log',
            'log_level':'INFO',
            'logging_mode':'a'
        }
        with open(PATH, 'w') as configfile:
            config.write(configfile)

##########################################
# Reads a value from the config file.
# sectionName is the name of the section in the file
# tag is the key of the config value
# typeVal is the type (string, int, float, bool) of the value
##########################################    
def readConfig(sectionName, tag, typeVal):
    fileName = './config/config.cfg'
    parser = ConfigParser()
    parser.read(fileName)
    if typeVal== 'int':
        configValue = parser.getint(sectionName, tag)
    elif typeVal== 'string':
        configValue = parser.get(sectionName, tag)
    elif typeVal== 'bool':
        configValue = parser.getboolean(sectionName, tag)
    elif typeVal== 'float':
        configValue = parser.getfloat(sectionName, tag)
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
    fileName = './config/config.cfg'
    config = ConfigParser()
    config.set(sectionName, tag, value)
    logging.debug("config values read %s, %s, %s", sectionName, tag, value)
    with open(fileName, 'wb') as configfile:
        config.write(configfile)
