#!/usr/bin/env python3

#import ConfigParser
from pathlib import Path
from configparser import ConfigParser


class config_reader:
    def __init__(self):
        self.file_name = './config/config.cfg'
        self.HERE = Path(__file__).parent.resolve()
        self.PATH = self.HERE / self.file_name
        self.parser = ConfigParser()
        if self.PATH.exists():
            print ('main config file found')
        else:
            print ('creating config file')
            self.parser['graphics'] = {
                'display_width':'800',
                'display_height':'600'
            }
            self.parser['sound'] = {
                'volume':'10'
            }
            self.parser['difficulty'] = {
                'difficulty':'hard'
            }
            self.parser['logging'] = {
                'log_file':'system.log',
                'log_dir':'./logs/',
                'log_level':'INFO',
                'logging_mode':'a'
            }
            with open(self.PATH, 'w') as configfile:
                self.parser.write(configfile)
    ##########################################
    # Reads a value from the config file.
    # sectionName is the name of the section in the file
    # tag is the key of the config value
    # typeVal is the type (string, int, float, bool) of the value
    ##########################################    
    def read_config(self, section_name, tag, typeVal):
        self.parser.read(self.file_name)
        if typeVal== 'int':
            configValue = self.parser.getint(section_name, tag)
        elif typeVal== 'string':
            configValue = self.parser.get(section_name, tag)
        elif typeVal== 'bool':
            configValue = self.parser.getboolean(section_name, tag)
        elif typeVal== 'float':
            configValue = self.parser.getfloat(section_name, tag)
        print ("config values read", tag, ':', configValue)
        # logging.debug("config values read %s", configValue)
        return configValue

    ##########################################
    # changes a value in the config file from the game settings
    # sectionName the name of the section
    # tag is the key that you are changing to value for
    # value is the new value to set
    ##########################################
    def changeSetting(self, sectionName, tag, value):
        self.parser.set(sectionName, tag, value)
        logging.debug("config values read %s, %s, %s", sectionName, tag, value)
        with open(self.file_name, 'wb') as configfile:
            self.parser.write(configfile)
